'''
This is example configuration for Stratum server.
Please rename it to config.py and fill correct values.
'''

# ******************** GENERAL SETTINGS ***************

# Enable some verbose debug (logging requests and responses).
DEBUG = False

# Destination for application logs, files rotated once per day.
LOGDIR = 'log/'

# Main application log file.
LOGFILE = 'stratum.log' #'stratum.log'

# Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGLEVEL = 'DEBUG'

# Logging Rotation can be enabled with the following settings
# It if not enabled here, you can set up logrotate to rotate the files.
# For built in log rotation set LOG_ROTATION = True and configrue the variables
LOG_ROTATION = True
LOG_SIZE = 10485760 # Rotate every 10M
LOG_RETENTION = 10 # Keep 10 Logs

# How many threads use for synchronous methods (services).
# 30 is enough for small installation, for real usage
# it should be slightly more, say 100-300.
THREAD_POOL_SIZE = 300

# RPC call throws TimeoutServiceException once total time since request has been
# placed (time to delivery to client + time for processing on the client)
# crosses _TOTAL (in second).
# _TOTAL reflects the fact that not all transports deliver RPC requests to the clients
# instantly, so request can wait some time in the buffer on server side.
# NOT IMPLEMENTED YET
#RPC_TIMEOUT_TOTAL = 600

# RPC call throws TimeoutServiceException once client is processing request longer
# than _PROCESS (in second)
# NOT IMPLEMENTED YET
#RPC_TIMEOUT_PROCESS = 30

# Do you want to expose "example" service in server?
# Useful for learning the server,you probably want to disable
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
# ******************** SSL SETTINGS ******************

# Private key and certification file for SSL protected transports
# You can find howto for generating self-signed certificate in README file
SSL_PRIVKEY = 'server.key'
SSL_CACERT = 'server.crt'

# ******************** TCP SETTINGS ******************

# Enables support for socket encapsulation, which is compatible
# with haproxy 1.5+. By enabling this, first line of received
# data will represent some metadata about proxied stream:
# PROXY <TCP4 or TCP6> <source IP> <dest IP> <source port> </dest port>\n
#
# Full specification: http://haproxy.1wt.eu/download/1.5/doc/proxy-protocol.txt
TCP_PROXY_PROTOCOL = False

# ******************** HTTP SETTINGS *****************

# Keepalive for HTTP transport sessions (at this time for both poll and push)
# High value leads to higher memory usage (all sessions are stored in memory ATM).
# Low value leads to more frequent session reinitializing (like downloading address history).
HTTP_SESSION_TIMEOUT = 3600 # in seconds

# Maximum number of messages (notifications, responses) waiting to delivery to HTTP Poll clients.
# Buffer length is PER CONNECTION. High value will consume a lot of RAM,
# short history will cause that in some edge cases clients won't receive older events.
HTTP_BUFFER_LIMIT = 10000

# User agent used in HTTP requests (for both HTTP transports and for proxy calls from services)
USER_AGENT = 'Stratum/0.1'

# Provide human-friendly user interface on HTTP transports for browsing exposed services.
BROWSER_ENABLE = True

# ******************** *COIND SETTINGS ************

# Hostname and credentials for one trusted Bitcoin node ("Satoshi's client").
# Stratum uses both P2P port (which is 8333 everytime) and RPC port
DAEMON_TRUSTED_HOST = '127.0.0.1'
DAEMON_TRUSTED_PORT = 8332 # RPC port
DAEMON_TRUSTED_USER = 'stratum'
DAEMON_TRUSTED_PASSWORD = '***somepassword***'

# ******************** OTHER CORE SETTINGS *********************
# Use "echo -n '<yourpassword>' | sha256sum | cut -f1 -d' ' "
# for calculating SHA256 of your preferred password
ADMIN_PASSWORD_SHA256 = None # Admin functionality is disabled
#ADMIN_PASSWORD_SHA256 = '9e6c0c1db1e0dfb3fa5159deb4ecd9715b3c8cd6b06bd4a3ad77e9a8c5694219' # SHA256 of the password

# IP from which admin calls are allowed.
# Set None to allow admin calls from all IPs
ADMIN_RESTRICT_INTERFACE = '127.0.0.1'

# Use "./signature.py > signing_key.pem" to generate unique signing key for your server
SIGNING_KEY = None # Message signing is disabled
#SIGNING_KEY = 'signing_key.pem'

# Origin of signed messages. Provide some unique string,
# ideally URL where users can find some information about your identity
SIGNING_ID = None
#SIGNING_ID = 'stratum.somedomain.com' # Use custom string
#SIGNING_ID = HOSTNAME # Use hostname as the signing ID

# *********************** IRC / PEER CONFIGURATION *************

IRC_NICK =  "stratum%s" # Skip IRC registration
#IRC_NICK = "stratum" # Use nickname of your choice

# Which hostname / external IP expose in IRC room
# This should be official HOSTNAME for normal operation.
#IRC_HOSTNAME = HOSTNAME

# Don't change this unless you're creating private Stratum cloud.
#IRC_SERVER = 'irc.freenode.net'
#IRC_ROOM = '#stratum-mining-nodes'
#IRC_PORT = 6667

# Hardcoded list of Stratum nodes for clients to switch when this node is not available.
PEERS = [
    {
        'hostname': 'stratum.bitcoin.cz',
        'trusted': True, # This node is trustworthy
        'weight': -1, # Higher number means higher priority for selection.
                      # -1 will work mostly as a backup when other servers won't work.
                      # (IRC peers have weight=0 automatically).
    },
]


'''
DATABASE_DRIVER = 'MySQLdb'
DATABASE_HOST = 'palatinus.cz'
DATABASE_DBNAME = 'marekp_bitcointe'
DATABASE_USER = 'marekp_bitcointe'
DATABASE_PASSWORD = '**empty**'
'''

POOL_TARGET = 4

# ******************** Adv. DB Settings *********************
#  Don't change these unless you know what you are doing

DB_LOADER_CHECKTIME = 15    # How often we check to see if we should run the loader
DB_LOADER_REC_MIN = 1       # Min Records before the bulk loader fires
DB_LOADER_REC_MAX = 50      # Max Records the bulk loader will commit at a time

DB_LOADER_FORCE_TIME = 300      # How often the cache should be flushed into the DB regardless of size.

DB_STATS_AVG_TIME = 300     # When using the DATABASE_EXTEND option, average speed over X sec
                #   Note: this is also how often it updates
DB_USERCACHE_TIME = 600     # How long the usercache is good for before we refresh


