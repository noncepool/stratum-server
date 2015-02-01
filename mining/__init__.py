from service import MiningService
from subscription import MiningSubscription
from twisted.internet import defer
from twisted.internet.error import ConnectionRefusedError
import time
import simplejson as json
from twisted.internet import reactor
import threading
from mining.work_log_pruner import WorkLogPruner

@defer.inlineCallbacks
def setup(on_startup):
    '''Setup mining service internal environment.
    You should not need to change this. If you
    want to use another Worker manager or Share manager,
    you should set proper reference to Interfaces class
    *before* you call setup() in the launcher script.'''
    
    import lib.settings as settings
        
    # Get logging online as soon as possible
    import lib.logger
    log = lib.logger.get_logger('mining')

    from interfaces import Interfaces
    
    from lib.block_updater import BlockUpdater
    from lib.template_registry import TemplateRegistry
    from lib.bitcoin_rpc import BitcoinRPC
    from lib.block_template import BlockTemplate
    from lib.coinbaser import SimpleCoinbaser

    bitcoin_rpc = BitcoinRPC(settings.DAEMON_TRUSTED_HOST,
                             settings.DAEMON_TRUSTED_PORT,
                             settings.DAEMON_TRUSTED_USER,
                             settings.DAEMON_TRUSTED_PASSWORD)

    log.info("Connecting to RPC...")

    while True:
        try:
            log.info('Waiting for RPC...')
            result = (yield bitcoin_rpc.getblocktemplate())
            if isinstance(result, dict):
                break
        except:
            time.sleep(1)
        
    log.info('Connected to RPC - Ready to GO!')

    # Start the coinbaser
    coinbaser = SimpleCoinbaser(bitcoin_rpc, getattr(settings, 'CENTRAL_WALLET'))
    (yield coinbaser.on_load)
    
    registry = TemplateRegistry(BlockTemplate,
                                coinbaser,
                                bitcoin_rpc,
                                getattr(settings, 'INSTANCE_ID'),
                                MiningSubscription.on_template,
                                Interfaces.share_manager.on_network_block)
    
    # Template registry is the main interface between Stratum service
    # and pool core logic
    Interfaces.set_template_registry(registry)
    
    # Set up polling mechanism for detecting new block on the network
    # This is just failsafe solution when -blocknotify
    # mechanism is not working properly    
    BlockUpdater(registry, bitcoin_rpc)

    prune_thr = threading.Thread(target=WorkLogPruner, args=(Interfaces.worker_manager.job_log,))
    prune_thr.daemon = True
    prune_thr.start()
    
    log.info("MINING SERVICE IS READY")
    on_startup.callback(True)





