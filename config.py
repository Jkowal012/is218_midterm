# config.py

import os

# Determine the environment: 'development' or 'production'
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

if ENVIRONMENT == 'production':
    DEBUG = False
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'app.log'  # Log file for production
    # Other production-specific settings can be added here
else:
    DEBUG = True
    LOG_LEVEL = 'DEBUG'
    LOG_FILE = 'app_dev.log'  # Log file for development
    # Other development-specific settings can be added here
