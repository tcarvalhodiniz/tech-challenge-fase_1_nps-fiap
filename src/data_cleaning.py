import pandas as pd
import os

def load_raw_data(file_name):
    """
    Carrega um ficheiro da pasta data/raw.
    """
    path = os.path.join("..", "data", "raw", file_name)
    if file_name.endswith('.csv'):
        return pd.read_csv(path)
    elif file_name.endswith('.xlsx'):
        return pd.read_excel(path)
    else:
        print("Formato de ficheiro não suportado.")
        return None