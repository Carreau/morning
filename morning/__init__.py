# -*- coding: utf-8 -*-
"""
A simple module to do repetitive tasks in the morning. 

Targeted as updating git repos.

"""

__author__ = 'Matthias Bussonnier'
__email__ = 'bussonniermatthias@gmail.com'
__version__ = '0.1.0'

version = __version__

import sys
import os
from os.path import expanduser
import configparser
import io
import argparse

import logging
log = logging.getLogger()
log.setLevel(10)

class _config(object):

    def __enter__(self):
        self.config = configparser.ConfigParser()
        self.config.read(expanduser('~/.morning'))

        return self.config

    def __exit__(self, *args_):
        with io.open(expanduser('~/.morning'),'w') as f:
            self.config.write(f)
        



def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands', dest='subcmd')
    parser_add = subparsers.add_parser('add',help='')
    parser_list = subparsers.add_parser('list',help='')
    

    parser_add.add_argument('dir')

    args = parser.parse_args()

    if args.subcmd == 'dir':
        directory = os.path.abspath(expanduser(args.dir))
        if not os.path.isdir(directory):
            sys.exit('%s is not a directory'%directory)
        with _config() as config:
            if not 'mornings' in config.sections():
                config['mornings'] = {}
            config['mornings'][directory] = 'true'

    elif args.subcmd == 'list':
        with _config() as config:
            for k in config['mornings'].keys():
                print(k)
                log.debug('%s' %(k))

    else :
        from subprocess import Popen
        log.info('no arguments, will update all things.')
        with _config() as config:
            for k in config['mornings'].keys():
                print('will update git in {}'.format(k))
                Popen(['git','fetch','origin'],cwd=k)




        
    



if __name__ =='__main__':
    main()
