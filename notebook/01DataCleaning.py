# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import pandas as pd

# <codecell>

exp_dir = '../../exp/'

# <codecell>

df = pd.read_csv(exp_dir + 'orders.csv', index_col=0)

# <codecell>

df.head()

# <codecell>

df.describe()

# <markdowncell>

# # Correlations

# <codecell>

df.corr()

# <codecell>

df.drop('base_total_paid', axis=1, inplace=True)

# <codecell>

df.corr()

# <markdowncell>

# # Check units

# <codecell>

df.describe()

# <codecell>

df['total_refunded'] = df['total_refunded'] // 100

# <codecell>

df.describe()

# <codecell>

df.to_csv(exp_dir + 'orders.cleaned.csv', index=0)
