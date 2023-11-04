from sklearn.feature_selection import SelectKBest, chi2
import pandas as pd
import numpy as np


def preprocess(df):
    # Remove irrelevant columns
    df = df.drop(['bite_date', 'vaccination_date', 'BreedIDDesc', 'victim_zip', 'AdvIssuedYNDesc',
                  'quarantine_date', 'DispositionIDDesc', 'head_sent_date', 'release_date', 'color', 'ResultsIDDesc'], axis=1)

    # impute
    df['vaccination_yrs'].fillna(df['vaccination_yrs'].mean(), inplace=True)
    df['GenderIDDesc'].replace('UNKNOWN', 'FEMALE')
    df['GenderIDDesc'].fillna('FEMALE')
    df['SpeciesIDDesc'].fillna('DOG')
    df.dropna(inplace=True)

    # one-hot encoding
    df = pd.get_dummies(df, columns=['GenderIDDesc', 'WhereBittenIDDesc'])

    # top 5 features

    X = df.drop('SpeciesIDDesc', axis=1)
    y = df['SpeciesIDDesc']
    selector = SelectKBest(chi2, k=5)
    X_new = selector.fit_transform(X, y)

    df.to_csv('res_dpre.csv', index=False)
