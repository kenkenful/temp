
from compatilib.BaseClass import BaseClass
from compatilib.const.path import (
    LOG_PATH_WINDOWS
    #FIGURE_PATH,
    #KFTT_TOK_CORPUS_PATH,
    #NN_MODEL_PICKLES_PATH,
    #TANAKA_CORPUS_PATH,
)

import os
import inspect

class WinPart(BaseClass):

    def __init__(self):
        self.set_logname(inspect.stack()[1].filename)
        self.logger = self.get_logger(__name__, LOG_PATH_WINDOWS)

    def func(self):
        #logger = self.get_logger(__name__)
        self.logger.info('Part')


"""
if __name__ == '__main__':
    sys = WinSystem()
    sys.func()
"""