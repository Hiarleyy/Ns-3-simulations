import os
import pandas as pd
from tkinter import Tk, filedialog

def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()
    
    # Supondo que a primeira linha contém os cabeçalhos
    headers = lines[0].strip().split()
    max_columns = len(headers)
    
    # Garantir que todas as linhas tenham o mesmo número de colunas que os cabeçalhos
    data = []
    for line in lines[1:]:
        row = line.strip().split()
        if len(row) < max_columns:
            row.extend([''] * (max_columns - len(row)))  # Preencher colunas faltantes com strings vazias
        elif len(row) > max_columns:
            row = row[:max_columns]  # Cortar colunas extras
        data.append(row)
    
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(csv_file, index=False)

def main():
    root = Tk()
    root.withdraw()  # Ocultar a janela principal
    folder_path = filedialog.askdirectory(title="Selecione a Pasta Contendo Arquivos .txt")
    
    if folder_path:
        csv_folder_path = os.path.join(folder_path, "csv")
        os.makedirs(csv_folder_path, exist_ok=True)
        
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                txt_file = os.path.join(folder_path, filename)
                csv_file = os.path.join(csv_folder_path, filename.replace(".txt", ".csv"))
                txt_to_csv(txt_file, csv_file)
                print(f"Convertido {txt_file} para {csv_file}")

if __name__ == "__main__":
    main()