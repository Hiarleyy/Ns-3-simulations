import os
import pandas as pd
from collections import Counter

def detect_separator(file_path, sample_size=1024):
    with open(file_path, 'r') as file:
        sample = file.read(sample_size)
    separators = [';', ',', '\t', '\t+' '|', ' ']
    counter = Counter(sample)
    most_common = counter.most_common()
    for sep, _ in most_common:
        if sep in separators:
            return sep
    raise ValueError(f"Não foi possível detectar um separador válido no arquivo {file_path}.")

def read_txt_file(file_path):
    sep = detect_separator(file_path)
    return pd.read_csv(file_path, sep=sep)

def convert_txt_to_csv(directory):
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    csv_directory = os.path.join(directory, 'csv')
    os.makedirs(csv_directory, exist_ok=True)

    for txt_file in txt_files:
        txt_path = os.path.join(directory, txt_file)
        try:
            df = read_txt_file(txt_path)
            csv_file = os.path.splitext(txt_file)[0] + '.csv'
            csv_path = os.path.join(csv_directory, csv_file)
            df.to_csv(csv_path, index=False)  # Use default separator ','
            print(f"Convertido {txt_file} para {csv_file}")
        except Exception as e:
            print(f"Falha ao converter {txt_file}: {e}")

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    convert_txt_to_csv(current_directory)
