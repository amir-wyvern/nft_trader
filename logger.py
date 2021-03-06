"""
python version 3.9
"""

import logging

def create_logger(name_log):

    logger = logging.getLogger(name_log)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(f'[%(asctime)-24s] [%(levelname)-8s] [%(lineno)-3d -{name_log:<11}] | %(message)s')
    fh = logging.FileHandler(f'debug_{name_log}.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(level=logging.DEBUG)
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger



