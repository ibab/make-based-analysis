#!/usr/bin/env python

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
df = df.query(sys.argv[3])
df.to_csv(sys.argv[2])

