import pandas as pd
import numpy as np

file_path = r"/home/nursss/Загрузки/Telegram Desktop/bank_accounts_big.xlsx"
df_acc = pd.read_excel(file_path, sheet_name='accounts')
df_tx = pd.read_excel(file_path, sheet_name='transactions')

df_acc['open_date'] = pd.to_datetime(df_acc['open_date'])
df_acc['balance_kgs'] = pd.to_numeric(df_acc['balance_kgs'], errors='coerce')
df_acc['balance_kgs'] = pd.to_numeric(df_acc['amount_kgs'], errors='coerce')


df_active = df_acc[df_acc['status'] == "Active"]
print(df_active.head(20))
