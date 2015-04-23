# -*- coding: utf-8 -*-

__author__ = 'Matthias Bussonnier'
__email__ = 'bussonniermatthias@gmail.com'
__version__ = '0.1.0'

import sys
import os
from os.path import expanduser
import configparser
import io
import argparse

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
    parser_add = subparsers.add_parser('add',
            help="register a package on PyPI without uploading any files"
    )

    parser_add.add_argument('dir')

    args = parser.parse_args()

    if args.dir:
        directory = os.path.abspath(expanduser(args.dir))
        if not os.path.isdir(directory):
            sys.exit('%s is not a directory'%directory)
        with _config() as config:
            if not 'mornings' in config.sections():
                config['mornings'] = {}
            config['mornings'][directory] = 'true'



        
    



if __name__ =='__main__':
    main()
