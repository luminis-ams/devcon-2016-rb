# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

%matplotlib inline
import pandas as pd

# <codecell>

orders_path = '../../exp/orders.cleaned.csv'

# <codecell>

df = pd.read_csv(orders_path, index_col=0)

# <codecell>

df.dtypes

# <codecell>

df['created_at'] = pd.to_datetime(df['created_at'])

# <codecell>

df.dtypes

# <markdowncell>

# # Make a time series

# <codecell>

df.index = df['created_at']

# <markdowncell>

# Is it sorted?

# <codecell>

df = df.sort_index()

# <codecell>

tsdf = df.resample('D', how='count')

# <codecell>

tsdf.head()

# <codecell>

tsdf['created_at'].plot(figsize=(16,10))
