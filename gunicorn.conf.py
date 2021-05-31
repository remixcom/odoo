import multiprocessing
import os

bind = os.environ['HOST'] + ':' + os.environ['PORT']
pidfile = '.gunicorn.pid'
workers = multiprocessing.cpu_count() * + 1
timeout = 720
max_requests = 8000
HOST = '127.0.0.1'
ODOO_ADDONS = '/opt/odoobeanstalk/odoo/addons'
RDS_HOSTNAME = 'odoo-prod.cspn35gmswug.us-east-1.rds.amazonaws.com'
RDS_PORT = '5432'
RDS_USERNAME = 'odoobeanstalk'
RDS_PASSWORD = 'StradivariuS'
PORT = '8069'
#############################
#CUSTOM REMIX CONFIG
#############################
admin_passwd = 'StradivariuS'
#############################
logfile = '/var/log/odoobeanstalk/odoo.log'
data_dir = '/mnt/efs'
#############################
proxy_mode = True
xmlrpc_interface = '0.0.0.0'
netrpc_interface = '0.0.0.0'
#############################
#############################
#Multiprocessing Config
#############################
#800-1.5GB
limit_memory_hard = 1572864000
limit_memory_soft = 838860800
limit_request = 8000
limit_time_cpu = 600
limit_time_real = 1200
limit_time_real_cron = 3600
max_cron_threads = 1
workers = 6
db_maxconn = 30