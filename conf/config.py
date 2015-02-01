'''
This is example configuration for Stratum server.
'''

# ******************** BASIC SETTINGS ***************
# These are the MUST BE SET parameters! 
ADMIN_PASSWORD_SHA256 = ''
CENTRAL_WALLET = ''

DAEMON_TRUSTED_HOST = 'localhost'
DAEMON_TRUSTED_PORT = 19334
DAEMON_TRUSTED_USER = 'user'
DAEMON_TRUSTED_PASSWORD = 'pass'

# Coin Algorithm is the option used to determine the algortithm used by stratum
DAEMON_ALGO = 'x11'
DAEMON_REWARD = 'POW'
DAEMON_TX_COMMENT = False
SOLUTION_BLOCK_HASH = True
# ******************** GENERAL SETTINGS ***************
# Set process name of twistd, much more comfortable if you run multiple processes on one machine
STRATUM_MINING_PROCESS_NAME= 'stratum_server'

# Enable some verbose debug (logging requests and responses).
DEBUG = False

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = 'stratum.log'      # eg. 'stratum.log'
LOGLEVEL = 'INFO'
# Logging Rotation can be enabled with the following settings
# It if not enabled here, you can set up logrotate to rotate the files. 
# For built in log rotation set LOG_ROTATION = True and configure the variables
LOG_ROTATION = True
LOG_SIZE = 10485760 # Rotate every 10M
LOG_RETENTION = 10 # Keep 10 Logs

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 100

# ******************** TRANSPORTS *********************
# Hostname or external IP to expose
HOSTNAME = 'localhost'

# Disable the example service
ENABLE_EXAMPLE_SERVICE = False

# Port used for Socket transport. Use 'None' for disabling the transport.
LISTEN_SOCKET_TRANSPORT = 3333
# Port used for HTTP Poll transport. Use 'None' for disabling the transport
LISTEN_HTTP_TRANSPORT = None
# Port used for HTTPS Poll transport
LISTEN_HTTPS_TRANSPORT = None
# Port used for WebSocket transport, 'None' for disabling WS
LISTEN_WS_TRANSPORT = None
# Port used for secure WebSocket, 'None' for disabling WSS
LISTEN_WSS_TRANSPORT = None

# Salt used for Block Notify Password
PASSWORD_SALT = 'some_crazy_string'

# ******************** Database  *********************
# MySQL
DB_MYSQL_HOST = 'localhost'
DB_MYSQL_DBNAME = 'db'
DB_MYSQL_USER = 'user'
DB_MYSQL_PASS = 'pass'
DB_MYSQL_PORT = 3306            # Default port for MySQL

# ******************** Adv. DB Settings *********************
#  Don't change these unless you know what you are doing

DB_LOADER_CHECKTIME = 15        # How often we check to see if we should run the loader
DB_LOADER_REC_MIN = 1          # Min Records before the bulk loader fires
DB_LOADER_REC_MAX = 75          # Max Records the bulk loader will commit at a time
DB_LOADER_FORCE_TIME = 300      # How often the cache should be flushed into the DB regardless of size.
DB_STATS_AVG_TIME = 300         # When using the DATABASE_EXTEND option, average speed over X sec
                                # Note: this is also how often it updates
DB_USERCACHE_TIME = 600         # How long the usercache is good for before we refresh

# ******************** Pool Settings *********************

# User Auth Options
USERS_AUTOADD = False           # Automatically add users to database when they connect.
                                # This basically disables User Auth for the pool.
USERS_CHECK_PASSWORD = False    # Check the workers password? (Many pools don't)

# Transaction Settings
COINBASE_EXTRAS = '/stratum-pool/'  # Extra Descriptive String to incorporate in solved blocks
COINBASE_TX_COMMENT = '/stratum-pool/' # String to incorporate in solved blocks tx comment area
# Coin Daemon communication polling settings (In Seconds)
PREVHASH_REFRESH_INTERVAL = 5   # How often to check for new Blocks
                                # If using the blocknotify script (recommended) set = to MERKLE_REFRESH_INTERVAL
                                # (No reason to poll if we're getting pushed notifications)
MERKLE_REFRESH_INTERVAL = 60    # How often check memorypool
                                # This effectively resets the template and incorporates new transactions.
                                # This should be "slow"

INSTANCE_ID = 31                # Used for extranonce and needs to be 0-31

FORCE_REFRESH_INTERVAL = 300    # How often to 'force' new work if no new blocks 

WORK_EXPIRE = 180               # How long before work expires

# ******************** Pool Difficulty Settings *********************
VDIFF_X2_TYPE = True            # Powers of 2 e.g. 2,4,8,16,32,64,128,256,512,1024
VDIFF_FLOAT = True              # Use float difficulty

SHARE_MULTIPLIER = 256          # SHARE_MULTIPLIER * diff = share diff
POOL_TARGET = 0.00390625 
# X11 diffs 0.00390625=1  0.0078125=2  0.015625=4 0.03125=8 0.0625=16 0.125=32 0.250=64 0.5=128 1=256

VARIABLE_DIFF = True            # Master variable difficulty enable

# Variable diff tuning variables
#VARDIFF will start at the POOL_TARGET. It can go as low as the VDIFF_MIN and as high as VDIFF_MAX
VDIFF_MIN_TARGET = 0.00390625   # Minimum target difficulty same as POOL_TARGET
VDIFF_MAX_TARGET = 1            # Maximum target difficulty 
VDIFF_TARGET_TIME = 15          # Target time per share (i.e. try to get 1 share per this many seconds)
VDIFF_RETARGET_TIME = 90        # Check to see if we should retarget this often
VDIFF_VARIANCE_PERCENT = 30     # Allow average time to very this % from target without retarget

# ******************** Worker Ban Options *********************
ENABLE_WORKER_STATS = False     # Master stats control disable to reduce server load
ENABLE_WORKER_BANNING = True    # Enable/disable temporary worker banning 
WORKER_CACHE_TIME = 600         # How long the worker stats cache is good before we check and refresh
WORKER_BAN_TIME = 300           # How long we temporarily ban worker
INVALID_SHARES_PERCENT = 500    # Allow average invalid shares vary this % before we ban
INVALID_SHARES_SPAM = 200       # Ban if we have this many invalids total before check time


