#!/usr/bin/env python3

import pandas as pd
from src.vocabulary import lambda_functions

def rewrite(classic_data_path, fuzzy_data_path):

    df = pd.read_csv(classic_data_path)

    new_columns = {}
    for new_col, func in lambda_functions.items():
        new_columns[new_col] = df.apply(func, axis=1)

    new_df = pd.DataFrame(new_columns)

    new_df.to_csv(fuzzy_data_path, index=False)

