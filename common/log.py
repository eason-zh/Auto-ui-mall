import logging
import os
import time
import colorlog
from config.conf import LOG_DIR

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR':'red',
    'CRITICAL':'red,bg_white',
}

log = logging.getLogger("log_name")

console_handler = logging.StreamHandler()
datime = time.strftime("%Y-%m-%d")
path = LOG_DIR +'/'
if not os.path.exists(path):
    os.makedirs(path)
filename = path + f'run_log_{datime}.log'

file_handler = logging.FileHandler(filename=filename, encoding='utf-8')

log.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

file_formatter = logging.Formatter(
    fmt='[%(levelname)s] [%(asctime)s.%(msecs)03d]:%(message)s %(filename)s -> %(funcName)s line:%(lineno)d',
    datefmt='%Y-%m-%d %H:%M:%S'
)

console_formatter = colorlog.ColoredFormatter(
    fmt = '[%(levelname)s] %(log_color)s[%(asctime)s.%(msecs)03d]:%(message)s %(filename)s -> %(funcName)s line:%(lineno)d',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors=log_colors_config
)
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

if not log.handlers:
    log.addHandler(console_handler)
    log.addHandler(file_handler)

console_handler.close()
file_handler.close()

'''
if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
'''