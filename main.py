#!/usr/bin/env python3

import argparse
from src.create_sub_data import create_sub_data
from src.rewrite import rewrite
from src.analysis import run_analysis

parser = argparse.ArgumentParser(
        prog='Mattias',
        description='run the project all once in a single script.'
)

parser.add_argument("-d", "--data_path", nargs='?', help="Path of input CSV.")
parser.add_argument("-e", "--extract", nargs='?', help="Size of the extraction")
parser.add_argument("-r", "--rewrite", action="store_true", help="Rewrite the database into fuzzy database.")
parser.add_argument("-a", "--analysis", action="store_true", help="Run analysis.")

args = parser.parse_args()

if __name__ == "__main__":
    data_path = args.data_path
    if args.extract:
        size = int(args.extract)
        extract_path = f"{data_path.split('.')[0]}_extract_{size}.csv"
    else:
        extract_path = data_path
    L = extract_path.split("_")
    L[-2] = "fuzzy"
    fuzzy_path = "_".join(L)

    if args.extract:
        create_sub_data(size, data_path, extract_path)
    if args.rewrite:
        rewrite(extract_path, fuzzy_path)
    if args.analysis:
        run_analysis(fuzzy_path)
