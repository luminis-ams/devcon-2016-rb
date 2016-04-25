# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <markdowncell>

# # Jupyter

# <codecell>

a = 1

# <codecell>

a

# <codecell>

a = a + 1

# <markdowncell>

# # Python

# <codecell>

import sys

# <codecell>

sys.version

# <markdowncell>

# ## Lists

# <codecell>

l = [4, 2, 3]

# <codecell>

l

# <codecell>

l[0] = 1

# <codecell>

l

# <markdowncell>

# ## Slicing makes a (shallow) copy

# <codecell>

m = l[1:-1]

# <codecell>

m

# <codecell>

m[0] = 7

# <codecell>

l

# <codecell>

l[::-1]

# <markdowncell>

# ## Tuples: immutable lists

# <codecell>

t = (1, 2, 3)

# <codecell>

t[0]

# <codecell>

# t[0] = 7 # Will not work!

# <markdowncell>

# ## Dictionaries: hash tables

# <codecell>

d = {'a': 1}

# <codecell>

d['a']

# <codecell>

t in d

# <codecell>

d[t] = 'abc'

# <codecell>

d

# <markdowncell>

# # Numpy

# <codecell>

import numpy as np

# <codecell>

np.version.version

# <markdowncell>

# ## Vectorize

# <codecell>

x = y = np.array(l)

# <codecell>

x

# <codecell>

x + y

# <markdowncell>

# ## Basic slicing creates a view (not a copy)

# <codecell>

z = x[:2]

# <codecell>

z

# <codecell>

z[0] = 7

# <codecell>

x

# <markdowncell>

# ## Advanced slicing creates a copy

# <codecell>

x = np.append(x, np.nan)

# <codecell>

np.isnan(x)

# <codecell>

y = x[~np.isnan(x)]

# <codecell>

y[0] = 17

# <codecell>

x

# <markdowncell>

# ## Lots of useful functions like

# <codecell>

np.mean(y)

# <markdowncell>

# # Pandas

# <codecell>

import pandas as pd
pd.version.version

# <markdowncell>

# ## Dataframes

# <codecell>

df = pd.DataFrame({ 'a' : [0, 1], 'b' : [2, 3]})

# <codecell>

df

# <markdowncell>

# ## Series

# <codecell>

s = pd.Series([5, 4], index=[1, 0])

# <codecell>

s

# <codecell>

df['c'] = s

# <codecell>

df

# <markdowncell>

# ## Indexing columns or rows

# <codecell>

df['b']

# <codecell>

df2 = df[(df['b'] % 2).astype(bool)]

# <codecell>

df2

# <markdowncell>

# ## Label based indexing

# <codecell>

df.loc[0, 'b']

# <codecell>

df.loc[:, ['b', 'a']]

# <markdowncell>

# ## Integer based indexing

# <codecell>

df.iloc[:, ::2]

# <markdowncell>

# ## Copy or view
# 
# Sometimes indexing returns a copy, sometimes a view, so be careful! Pandas will help you with the occasional warning.
