import pandas as pd

def load_data():
    df = pd.read_csv("power_transmission_projects_balanced_dataset.csv")
    df = df.dropna()
    return df