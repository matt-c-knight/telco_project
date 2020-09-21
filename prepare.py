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