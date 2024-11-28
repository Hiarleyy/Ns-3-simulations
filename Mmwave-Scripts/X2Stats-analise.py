#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#%%
# Importando os dados
df = pd.read_csv("X2Stats.csv", sep=';') 
df.head() #nao sabemos que é 'arrumar' coloquei arbritariamente

# %%
df['TargetCellId'].value_counts()
# %%
