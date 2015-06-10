#!/usr/bin/env python

import sys
from root_pandas import *

df = read_root(sys.argv[1], where=sys.argv[3])
df.to_root(sys.argv[2])

