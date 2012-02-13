#!/usr/bin/env python

import shutil
import argparse
import os
import sys
from Cheetah.Template import Template
import base64
import uuid

parser = argparse.ArgumentParser(description='Create a new warm air based application.')
parser.add_argument('application', metavar='A', type=str, 
                   help='Name of your app.')

parser.add_argument('destination', metavar='B', type=str, 
                   help='Directory where new application should be created.')

args = parser.parse_args()

if args.destination[-1] != '/':
    args.destination += '/'


if os.path.exists(args.destination):
    shutil.copytree('src/', args.destination + args.application, 
        ignore=shutil.ignore_patterns('*.pyc','.git*'))
else:
    print "Path %s does not exist" % (args.destination)
    sys.exit(0)

##
## settings.example.py
##
f = open(args.destination + args.application + '/' + 'settings.example.py')
settings = f.read()
f.close()

cookie_secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
name_space = {'cookie_secret': cookie_secret}
t = Template(settings, searchList=[name_space])

print t

