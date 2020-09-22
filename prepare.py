import pandas as pd
import numpy as np
import sklearn
from acquire import get_telco_data
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def telco_split(df):

    train_validate, test = train_test_split(df, test_size=.2,
                                        random_state=123,
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3,
                                        random_state=123,
                                        stratify=train_validate.churn)
    return train, validate, test


def prep_telco(cached=True):

    df = get_telco_data(cached)
    df = df.drop(columns=['customer_id', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'internet_service_type_id', 'contract_type_id', 'payment_type_id', 'partner', 'dependents', 'multiple_lines', 'streaming_tv', 'streaming_movies', 'total_charges'])
    df_dummies = pd.get_dummies(df.contract_type)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='contract_type')
    df_dummies = pd.get_dummies(df.internet_service_type)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='internet_service_type')
    df_dummies = pd.get_dummies(df.payment_type)
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop(columns='payment_type')
    df.loc[df['phone_service'] == 'No', 'phone_service'] = 0
    df.loc[df['phone_service'] == 'Yes', 'phone_service'] = 1
    df.loc[df['paperless_billing'] == 'No', 'paperless_billing'] = 0
    df.loc[df['paperless_billing'] == 'Yes', 'paperless_billing'] = 1
    df.loc[df['churn'] == 'No', 'churn'] = 0
    df.loc[df['churn'] == 'Yes', 'churn'] = 1
    df_dummies = pd.get_dummies(df.gender)
    df = pd.concat([df, df_dummies], axis=1)
    df.drop(columns='gender')

    return df