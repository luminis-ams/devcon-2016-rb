# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import sklearn
import sklearn.tree

# <codecell>

sklearn.__version__

# <codecell>

exp_dir = '../../exp/'
df_train = pd.read_csv(exp_dir + 'train.csv', index_col=0)
df_test = pd.read_csv(exp_dir + 'test.csv', index_col=0)

# <markdowncell>

# # Fitting the classifier

# <codecell>

prng = np.random.RandomState(1234567)
clf = sklearn.tree.DecisionTreeClassifier(
        max_depth=3,
        min_samples_leaf=5, 
        class_weight='auto',
        random_state=prng)

# <codecell>

df_train.columns

# <codecell>

df_train.head()

# <codecell>

X_train = df_train.iloc[:, :-2].values

# <codecell>

Y_train = df_train.loc[:, 'predict_has_order'].values

# <codecell>

clf = clf.fit(X_train, Y_train)

# <markdowncell>

# # Predictions for the test set

# <codecell>

X_test = df_test.iloc[:, :-2].values
Y_test = df_test.loc[:, 'predict_has_order'].values

# <codecell>

Y_predict = clf.predict(X_test)

# <codecell>

print(sklearn.metrics.classification_report(Y_test, Y_predict))

# <codecell>

pd.DataFrame({'importance' : clf.feature_importances_},
        index=df_train.columns[:-2])

# <markdowncell>

# # Fitting the regressor

# <codecell>

reg = sklearn.tree.DecisionTreeRegressor(
        max_depth=2, 
        min_samples_leaf=5,
        random_state=prng)

# <codecell>

Y_reg_train = df_train.loc[:, 'predict_revenue']

# <codecell>

reg = reg.fit(X_train, Y_reg_train)

# <markdowncell>

# # Predictions for the test set

# <codecell>

Y_reg_test = df_test.loc[:, 'predict_revenue']

# <codecell>

Y_reg_predictions = reg.predict(X_test)

# <codecell>

mse = sklearn.metrics.mean_squared_error(Y_reg_test, Y_reg_predictions)

# <codecell>

mse

# <codecell>

np.sqrt(mse)

# <codecell>

sklearn.metrics.r2_score(Y_reg_test, Y_reg_predictions)

# <codecell>

pd.DataFrame({'importance' : reg.feature_importances_},
    index=df_train.columns[:-2])
