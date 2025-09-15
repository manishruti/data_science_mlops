import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s" ## It will save time, levelname means whether it's a info or warning or error, module name and message
log_dir = "logs"
log_filepath = os.path.join(log_dir,"logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO, # Sets the **minimum level** of messages to log, INFO` includes INFO, WARNING, ERROR, and CRITICAL.- (If you set it to `DEBUG`, you'd also include debug messages.
    format= logging_str,
    handlers=[  # Where to send the the logs
        logging.FileHandler(log_filepath),# Logs are saved to the file 'logs/logging.log'
        logging.StreamHandler(sys.stdout) # Logs are printed to the console
    ]
)

logger = logging.getLogger("dataScienceLogger")
