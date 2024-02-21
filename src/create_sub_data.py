#!/usr/bin/env python3

import pandas as pd
import numpy as np


def create_sub_data(size, input_path, output_path):
    df = pd.read_csv(input_path)
    X = np.linspace(0, 1, len(df)) * len(df)
    np.random.shuffle(X)
    X = X[:size].astype(int)
    sdf = df.iloc[X].reset_index(drop=True)
    sdf.to_csv(output_path, index=False)
