#!/usr/bin/env python

import sys
from root_pandas import *

INPATH=sys.argv[1]
PLOTPATH=sys.argv[2]
VARIABLE=sys.argv[3]

df = read_root(INPATH, columns=[VARIABLE])

import matplotlib.pyplot as plt

df[VARIABLE].hist(bins=100, grid=False, histtype='step')
plt.xlabel('$x$')
plt.tight_layout()
plt.savefig(PLOTPATH)

