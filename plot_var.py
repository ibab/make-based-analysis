#!/usr/bin/env python

import sys
import pandas as pd

INPATH=sys.argv[1]
PLOTPATH=sys.argv[2]
VARIABLE=sys.argv[3]

df = pd.read_csv(INPATH)

import matplotlib.pyplot as plt

df[VARIABLE].hist(bins=100, grid=False, histtype='step')
plt.xlabel('$x$')
plt.tight_layout()
plt.savefig(PLOTPATH)

