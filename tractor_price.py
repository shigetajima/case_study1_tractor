import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm

df = pd.read_csv('../data/Train.csv',usecols=['saledate','YearMade',
    'MachineHoursCurrentMeter','SalePrice','ProductGroup','ProductSize','Enclosure'])

def dummify(df, columns):
    return pd.get_dummies(df, columns=columns)

def data_prep_group_1(df):
    df = df.drop(df[df['YearMade'] < 1800].index,axis=0)
    df['SaleYear'] = df['saledate'].map(lambda x: x[-9:-5]).astype(int)
    df['Age'] =  (df['SaleYear'] - df['YearMade']).astype(int)
    df['MachineHoursCurrentMeter'].fillna(value=0.0,inplace=True)
    # df = dummify(df,['ModelID'])
    df = dummify(df,['ProductGroup','ProductSize','Enclosure'])
    return df

def linear_model_sklearn():
    new_df = data_prep_group_1(df)
    sample = new_df.sample(frac=1)
    y = sample['SalePrice'].values
    X = sample[['YearMade','MachineHoursCurrentMeter','Age']].values
    model = LinearRegression(n_jobs=-1).fit(X,y)
    print model.score(X,y)
    return model

def linear_model_sm():
    new_df = data_prep_group_1(df)
    sample = new_df.sample(frac=1)
    y = sample['SalePrice']
    # Add / remove features. Features with large p-values are removed.
    features = ['YearMade','MachineHoursCurrentMeter','Age']
    features += ['ProductGroup_BL','ProductGroup_MG','ProductGroup_SSL','ProductGroup_TEX','ProductGroup_TTT','ProductGroup_WL']
    features += ['ProductSize_Compact','ProductSize_Large','ProductSize_Large / Medium','ProductSize_Medium','ProductSize_Mini'] # removed 'ProductSize_Small'
    features += ['Enclosure_EROPS','Enclosure_EROPS w AC','Enclosure_OROPS'] # removed 'Enclosure_EROPS AC','Enclosure_None or Unspecified','Enclosure_NO ROPS'
    X = sample[features]
    X = sm.add_constant(X)
    model = sm.OLS(y,X)
    model = model.fit()
    print(model.summary())
    return model

#mod = linear_model_sklearn()
mod = linear_model_sm()
