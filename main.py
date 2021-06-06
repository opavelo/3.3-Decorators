import json
from pprint import pprint
import hashlib
import datetime
import os

def file_link(link_to_logfile):
    def logging(function):
        def function_replaced(*args, **kwargs):
            result = function(*args, **kwargs)
            if not os.path.exists(link_to_logfile):
                os.makedirs(link_to_logfile)
            os.chdir(link_to_logfile)
            f = open(str('log_' + datetime.datetime.now().strftime("%d%m%Y_%H%M%S") + '.txt'), "x")
            date_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            f.writelines(date_time + " Released function: " + function.__name__ + '\n')
            f.write(f'Аргументы вызванной функции: ')
            f.write(*args, **kwargs)
            f.write('\n')
            for line in result:
                f.writelines(str(line) + '\n')
            cwd = os.getcwd()
            print("Current working directory: {0}".format(cwd))
            f.close
            return result
        return function_replaced
    return logging

@file_link('Folder_for_logs')
def my_generator(link):
    with open(link, 'r', encoding='utf-8') as f:
        data = f.readlines()
        hash_list = []
    for line in data:
        line = line.rstrip()
        line_hash = hashlib.md5(line.encode()).hexdigest()
        hash_list.append(line_hash)
    return hash_list

my_generator('file.txt')

