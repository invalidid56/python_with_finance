import pandas as pd

incheon = pd.read_csv(
    'incheon.csv',
    encoding='euc-kr',
    index_col=0
)

incheon['예산액변화율'] = incheon['예산액'] / incheon['전년도예산액']

print(incheon['예산액변화율'])

incheon.to_csv('incheon_modified.csv', index=True)

