import pandas as pd


df = pd.read_excel('agri.xlsx',
                   skiprows=2, index_col=1)

print(df)

df = df[['조직형태별(1)', '작물재배업', '축산업']]

df.to_excel('agri_dropna.xlsx')
