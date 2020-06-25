import pandas as pd

def retorno():
    df = pd.read_excel('/content/gdrive/My Drive/ParceriaBrunoGolfete/variados.xlsx', sheet_name='Variados')
    df_copy = df.copy()
    df.set_index('Data', inplace=True)
    df = df[df.columns[:5]]
    df_ret = df.pct_change()
    df_ret = df_ret.dropna()
    data = df_ret.copy()
    variables = df_ret.columns
    return df_ret