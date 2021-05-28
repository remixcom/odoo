# WSGI Handler sample configuration file.
#
# Change the appropriate settings below, in order to provide the parameters
# that would normally be passed in the command-line.
# (at least conf['addons_path'])
#
# For generic wsgi handlers a global application is defined.
# For uwsgi this should work:
#   $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py
#
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn odoo:service.wsgi_server.application -c openerp-wsgi.py

import odoo
import os

#----------------------------------------------------------
# Common
#----------------------------------------------------------
odoo.multi_process = True # Nah!

# Equivalent of --load command-line option
odoo.conf.server_wide_modules = ['base', 'web']
conf = odoo.tools.config

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)

conf['addons_path'] = os.environ['ODOO_ADDONS']

# Optional database config if not using local socket
if 'RDS_HOSTNAME' in os.environ:
    conf['db_host'] = os.environ['RDS_HOSTNAME']
    conf['db_port'] = os.environ['RDS_PORT'] # 5432
    # conf['dbfilter'] = '^odoo11-.*$'
    conf['db_user'] = os.environ['RDS_USERNAME']
    conf['db_password'] = os.environ['RDS_PASSWORD']
    conf['xmlrpc_port'] = os.environ['PORT']
    conf['longpolling_port'] = os.environ['PORT1']

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = odoo.service.wsgi_server.application

odoo.service.server.load_server_wide_modules()

#----------------------------------------------------------
# Gunicorn
#----------------------------------------------------------
# Standard OpenERP XML-RPC port is 8069
HOST = '0.0.0.0'
bind = os.environ['HOST'] + ':' + os.environ['PORT']
pidfile = '.gunicorn.pid'
workers = 6
timeout = 720
max_requests = 8000
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
db_maxconn = 80
