#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Étape 1
def compute_mean_values(df):
    mean = df.mean()
    return mean

def save_mean_json(mean):
    with open("results/mean_results.json", 'w') as fp:
        fp.write(mean.to_json(indent=4))

def compute_balance(distribution):
    balance = {}
    for key in distribution:
        balance[key] = distribution[key].var()
    return balance

def plot_balance_results(balance):
    keys = list(balance.keys())
    values = list(balance.values())
    fig, ax = plt.subplots()
    ax.barh(keys, values, color='skyblue')
    ax.set_title('Features variance')
    fig.tight_layout()
    fig.savefig('results/balance_figure.png')


# Étape 2
def cut(R, v):
    for feature, threshold in v.items():
        R = R[R[feature] > threshold]
    return R

def save_cut_json(cut_df, thresholds):
    name = '-'.join([f"{feature}_{thresholds[feature]}"
                     for feature in thresholds])
    with open(f"results/{name}.json", 'w') as fp:
        fp.write(cut_df.to_json(indent=4))

def is_decimal(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def parse_arguments(arguments):
    L = arguments.split(' ')
    r = {}
    while len(L) >= 2:
        if is_decimal(L[1]):
            r[L[0]] = float(L[1])
        else:
            r[L[0]] = 0
    return r


# Étape 3
"""
def cover(v, R):  # couverture du terme v dans le vecteur de réécriture R
    return R[v.keys()].sum().sum() / len(R.keys())

def dep(R, v, v_prime):
    Rv = cut(R, v)
    a = cover(v_prime, Rv) 
    b = cover(v_prime, R)
    if b == 0:
        return 0
    return a / b 

def assoc(R, v, v_prime):  # correlation entre v_1 et v_2
    d = dep(R, v, v_prime)
    if d <= 1:
        return 0
    return 1 - 1 / d

def fuzzy_implication(R, v, v_prime):  # a function I created
    R1 = R[v.keys()].sum(axis=1)
    R2 = R[v_prime.keys()].sum(axis=1)
    df = pd.DataFrame({"R1": R1, "R2": R2})
    df = df[df["R1"] > 0]
    df["min"] = df.min(axis=1)
    df["norm"] = df["min"] / df["R1"]
    implication = df["norm"].sum() / len(df)
    return implication

def compute_all_v_prime(R, v):
    if type(v) != dict:
        v = {v: 0}
    r = {}
    for t in R.keys():
        v_prime = {t: 0}
        r[t] = fuzzy_correlation(R, v, v_prime)
    return r
"""

def fuzzy_correlation(R, v, v_prime):
    R1 = R[v.keys()].sum(axis=1)
    R2 = R[v_prime.keys()].sum(axis=1)
    return R1.corr(R2)



def compute_correlation_matrix(R):
    corr_matrix = R.corr()

    fig, ax = plt.subplots(figsize=(16, 16))

    im = ax.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.set_label('Correlation')
    ax.set_title('Correlation Matrix')
    ax.set_xticks(range(len(corr_matrix)))
    ax.set_xticklabels(
            corr_matrix.columns, rotation=-90,
            horizontalalignment="left", verticalalignment="top",
            rotation_mode="anchor")
    ax.set_yticks(range(len(corr_matrix)))
    ax.set_yticklabels(corr_matrix.columns)

    plt.tight_layout()

    return fig


def compute_distribution(R):
    original_keys = {}
    for key in R.keys():
        key = key.split('.')[0]
        if key in original_keys:
            continue
        sub_R = R[[k for k in R.keys() if key == k.split('.')[0]]]
        s = sub_R.sum() / len(R)
        original_keys[key] = s
    return original_keys


def compute_fig_distribution(distribution):
    figs = {}
    for name in distribution:
        fig, ax = plt.subplots()
        ax.set_title(f"{name} distribution")
        series = distribution[name]
        names = [n.split('.')[1] for n in series.index]
        ax.bar(names, series.values)
        ax.grid(True)
        fig.tight_layout()
        figs[name] = fig
    return figs



def run_analysis(fuzzy_path):
    # Étape 0
    #original = pd.read_csv(f"{data_path}/flights_extract_{size}.csv")
    R = pd.read_csv(fuzzy_path)

    # Étape 1
    mean = compute_mean_values(R)
    save_mean_json(mean)
    distribution = compute_distribution(R)
    balance = compute_balance(distribution)
    plot_balance_results(balance)

    # Étape 2
    s_1 = {"DayOfWeek.end": 0.5}
    cut_df_1 = cut(R, s_1)
    Rs_1 = save_cut_json(cut_df_1, s_1)
    s_2 = {"DepTime.evening": 0.5}
    cut_df_2 = cut(R, s_2)
    Rs_2 = save_cut_json(cut_df_2, s_2)
    s_3 = {"Distance.long": 0.5, "DepTime.evening": 0.5}
    cut_df_3 = cut(R, s_3)
    Rs_3 = save_cut_json(cut_df_3, s_3)

    # Étape 3

    ## Termes Corrélés
    fig = compute_correlation_matrix(R)
    fig.savefig('results/correlation_matrix.png')
    #fig.show()

    ## Termes Atypiques
    figs = compute_fig_distribution(distribution)
    for name in figs:
        fig = figs[name]
        fig.savefig(f"results/{name}_distribution.png")
        #fig.show()
