import os
import yaml
import numpy as np
import pandas as pd
from tqdm import tqdm
# from sklearn.model_selection import train_test_split


def load_params(param_dir):
    with open(param_dir, 'r') as file:
        params = yaml.safe_load(file)
        
    return params

def read_dataset(dataset_dir):
    dataset = pd.DataFrame()

    for i in tqdm(os.listdir(dataset_dir)):
        dataset = pd.concat([pd.read_csv(dataset_dir + i), dataset], ignore_index=True) # read_csv("data/raw/filename[i]") + current dataset
    
    return dataset

# params_dir = "config/config.yaml"
# params = load_params(params_dir)
# params
# print(params["predictors"])

# dataset = read_dataset(params["dataset_dir"])
# print(dataset.head(4))