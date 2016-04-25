# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

%matplotlib inline
import pandas as pd
import numpy as np

# <codecell>

orders_path = '../../exp/orders.cleaned.csv'
df = pd.read_csv(orders_path)
df['created_at'] = pd.to_datetime(df['created_at'])
df.index = df['created_at']
df = df.sort_index()

# <codecell>

df.head()

# <codecell>

df.shape

# <markdowncell>

# # A helper variable of interest for quick computation

# <codecell>

df['revenue'] = df['total_paid'].fillna(0) - df['total_refunded'].fillna(0)

# <markdowncell>

# # Training period vs (historical) prediction period

# <codecell>

first_of_july = pd.Timestamp('2013-07-01')

# <codecell>

df_spring = df[df['created_at'] < first_of_july]
df_fall = df[df['created_at'] >= first_of_july]

# <markdowncell>

# # Group by customer

# <codecell>

df_spring_by_email = df_spring.groupby('email')

# <codecell>

df_fall = df_fall[df_fall['email'].isin(df_spring_by_email.groups.keys())]

# <codecell>

df_fall_by_email = df_fall.groupby('email')

# <markdowncell>

# # Compute variables we should predict

# <codecell>

df_predict_variables = df_fall_by_email.aggregate({
        'products_ordered' : {'predict_has_order' : lambda x: 1},
        'revenue' : {'predict_revenue' : 'sum'}
    })

# <codecell>

df_predict_variables.describe()

# <codecell>

df_predict_variables = pd.DataFrame({
        'predict_has_order' : df_predict_variables.loc[
                :, ('products_ordered', 'predict_has_order')],
        'predict_revenue' : df_predict_variables.loc[
                :, ('revenue', 'predict_revenue')]
    })

# <codecell>

df_predict_variables.describe()

# <markdowncell>

# # Compute some aggregates as basis for features

# <codecell>

df_spring_variables = df_spring_by_email.aggregate({
        'products_ordered' : {
            'count' : 'count',
            'count_unique' : pd.Series.nunique,
            'days' :lambda x: np.count_nonzero(x.resample('D', how='count'))
        },
        'total_refunded' : 'count',
        'total_canceled' : 'count',
        'revenue' : ['mean', 'sum'],
        'created_at' : {
            'avg_t_between_orders' : lambda x: np.mean(
                    x.values[1:] - x.values[:-1]) 
                            if len(x) > 1 else np.nan,
            't_since_last_order' : lambda x: first_of_july - x[-1]
        }
    })

# <codecell>

df_spring_variables.head()

# <markdowncell>

# # Divide in train and test set

# <codecell>

prng = np.random.RandomState(1234567)

# <codecell>

df_spring_variables['training_set_membership'] = prng.random_sample(
        len(df_spring_variables)) < 0.7

# <markdowncell>

# # Compute features

# <codecell>

df_features = pd.DataFrame({
        'has_more_than_one_order' : (df_spring_variables.loc[:,
                ('products_ordered', 'count')] > 1).astype('int'),
        'has_order_on_more_than_one_day' : (df_spring_variables.loc[:,
                ('products_ordered', 'days')] > 1).astype('int'),
        'has_ordered_diverse_products' : (df_spring_variables.loc[:, 
                ('products_ordered', 'count_unique')] > 1).astype('int'),
        'has_refund' : (df_spring_variables.loc[:,
                ('total_refunded', 'count')] > 0).astype('int'),
        'has_cancel' : (df_spring_variables.loc[:,
                ('total_canceled', 'count')] > 0).astype('int'),
        'mean_revenue' : df_spring_variables.loc[:, ('revenue', 'mean')],
        'is_last_order_long_ago' : (
                df_spring_variables.loc[:,
                        ('created_at', 't_since_last_order')] >
                np.mean(df_spring_variables.loc[
                        df_spring_variables['training_set_membership'],
                        ('created_at', 'avg_t_between_orders')])
        ).astype(int)
    }, index=df_spring_variables.index)

# <codecell>

df_features.describe()

# <markdowncell>

# # Combine features and 'to predict' (dependent) variables

# <codecell>

df_all_variables = pd.concat([df_features, df_predict_variables],
        axis=1, join_axes=[df_features.index]).fillna(0)

# <codecell>

df_all_variables.head()

# <markdowncell>

# # Training set feature correlation with dependents

# <codecell>

df_train = df_all_variables[df_spring_variables['training_set_membership']]

# <codecell>

df_train.corr().loc[:, ['predict_has_order', 'predict_revenue']]

# <markdowncell>

# # Serialize

# <codecell>

df_train.to_csv('../../exp/train.csv')

# <codecell>

df_test = df_all_variables[~df_spring_variables['training_set_membership']]

# <codecell>

df_test.to_csv('../../exp/test.csv')

# <codecell>


