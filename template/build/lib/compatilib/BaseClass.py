import logging
import subprocess
import os
import sys
import time
import platform
import json


class BaseClass(object):
    def __init__(self):
        self.__logname = 'common'
        self.logger = self.get_logger(__name__)
    
    """
    @property
    def logname(self):
        return self.__logname

    @logname.setter
    def logname(self, name):
        self.__logname = name
    """

    def set_logname(self, name: str):
        filename = os.path.basename(name)
        filename_no_extension = os.path.splitext(filename)[0]
        self.__logname = filename_no_extension

    def func(self):
        #logger = self.get_logger(__name__)
        self.logger.info('This is test logger test.')

    def get_logger(self, name, log_name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        format = '%(asctime)s [%(levelname)s] %(filename)s, lines %(lineno)d, %(funcName)s, %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(format, date_format)

        file_handler = logging.FileHandler(log_name + '/' + self.__logname + '.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        return logger

    def run_sync_process(self, **kwargs):
        #logger = self.get_logger(__name__)
        cmd=kwargs.pop('cmd', None)
        self.logger.info(cmd)

        if platform.system() == "Windows":
            creationflags = subprocess.CREATE_NEW_PROCESS_GROUP
        else:
            creationflags = os.setsid()

        try:
            p = subprocess.Popen(cmd,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,          
                            shell = True,
                            universal_newlines= True,
                            creationflags=creationflags)

            while p.poll() is None:
                time.sleep(0.01)

        except KeyboardInterrupt:
            self.logger.exception('keyboard interruppt')
            if p is not None:
                p.terminate()
            raise
        (stdout, stderr) = p.communicate()
        status = p.returncode

        self.logger.info('status :%s' % status)
        self.logger.info('stdout :%s' % stdout) 
        self.logger.info('stderr :%s' % stderr)

        return status, stdout, stderr


    def run_async_process(self, **kwargs):
        #logger = self.get_logger(__name__)
        cmd=kwargs.pop('cmd', None)
        self.logger.info(cmd)

        if platform.system() == "Windows":
            creationflags = subprocess.CREATE_NEW_PROCESS_GROUP
        else:
            creationflags = os.setsid()

        p = subprocess.Popen(cmd,
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,          
                        shell = True,
                        universal_newlines= True,
                        creationflags=creationflags)
        
        return p


    def wait_async_process(self, p):
        #logger = self.get_logger(__name__)

        while p.poll() is None:
            time.sleep(0.01)

        (stdout, stderr) = p.communicate()
        status = p.returncode

        self.logger.info('status :%s' % status)
        self.logger.info('stdout :%s' % stdout) 
        self.logger.info('stderr :%s' % stderr)

        return status, stdout, stderr
    
    def kill_async_process(self, p):
        if p is not None:
            p.terminate()
    

    def generate_dict_json(self, json_file_name):
        if json_file_name is None:
            return None    

        with open(json_file_name) as json_data:
            json_dict = json.load(json_data)
        
        return json_dict


if __name__ == '__main__':
    base = BaseClass()
    p = base.run_async_process(cmd='timeout 5')

    status, stdout,stderr = base.run_sync_process(cmd='timeout 3')

    if not status:
        print(status)
    else:
        print('command fail')

    status, stdout,stderr = base.wait_async_process(p)
    if not status:
        print(status)
    else:
        print('command fail')
