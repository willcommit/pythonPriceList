import argparse
import pandas as pd


def read_excel(fname):
    xl = pd.read_excel(fname, nrows=10)
    # item_numbers = xl['ItemNo']
    # models = xl['Model']

    return xl


if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f", type=str, required=True)
    args = options.parse_args()
    data = read_excel(args.f)
    print(data[0].values)

