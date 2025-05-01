import pandas as pd
import os
import kagglehub
from kagglehub import KaggleDatasetAdapter
import polars as pl
import shutil

# Dowloard data:
path = kagglehub.dataset_download('harshadashirin/inventory-mangement-analysis-sql-based-project')
file_path =  '/Users/moloarmindo/Documents/projetos/data_analytics/inventory_management/data_mining/data'
# Loard the latest version:
def move_file(start_path, and_path):
    # new path
    if not os.path.exists(and_path):
        os.makedirs(and_path)

    for item in os.listdir(start_path):
        start = os.path.join(start_path, item)
        ands = os.path.join(and_path, item)

        # verifica se e um arquivo e move:
        if os.path.isfile(start):
            shutil.move(start, ands)
        elif os.path.isdir(start):
            move_file(start, and_path)    



if __name__ == '__main__':
    move_file(path, file_path)
