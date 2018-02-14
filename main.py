#!/usr/bin/env python
from models import *
import input_processor as ip
import os

DB_FILE = 'db/counter_db.sqlite3'
LOG_FILE = 'log/counter_2018-02-13.log'
os.remove(DB_FILE)
#import ipdb; ipdb.set_trace()
DbActions.create_db()

with open(LOG_FILE) as infile:
    for line in infile:
        ll = ip.LogLine(line)
        ll.populate()