import logging
from cfg.cfg import get_value

def log_error(module, level, error):
    is_enabled = get_value('logging')
    if str(is_enabled) == 'True':
        logging.getLogger()
        logging.basicConfig(handlers=[logging.FileHandler(filename='./data/logs/errorLogs.log', 
                                                 encoding='utf-8', mode='a')], level=logging.ERROR)
        logging.error("{\nModule: "+str(module)+"\nLevel: "+str(level)+"\nError: "+str(error)+"\n}\n--------------------------------------------\n")