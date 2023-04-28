import pandas as pd


df = pd.DataFrame([
    [1000, 2, 300],
    [4000, 5, 600],
    [7000, 8, 900]], columns=['가격', '인기도', '재료비'], index=['김밥', '순대', '돈까스'])

print('메뉴판 보기 =======')
print(df)

print('첫 번째 메뉴 =======')
print(df.iloc[0])

print('돈까스에 대한 정보 =======')
print(df.loc['돈까스'])

print('가격에 대한 정보 =======')
print(df['가격'])

df['가격'] = df['가격'] * 1.5
print('수정된 가격에 대한 정보 =======')
print(df['가격'])

df['인기도'] = df['인기도'].map(lambda x: x*2 if x<5 else x*0.8)
print('수정된 인기도에 대한 정보 =======')
print(df['인기도'])

for row in df.iterrows():
    print(row[1]['가격'])

print(df['가격'].unique())


df = pd.read_csv('finance.csv', index_col=1, encoding='euc-kr')

special = 0
market = 0
local = 0

for row in df.iterrows():
    if row[1]['구분'] == '특수은행':
        special += row[1]['합계_금액']
    elif row[1]['구분'] == '시중은행':
        market += row[1]['합계_금액']
    elif row[1]['구분'] == '지방은행':
        local += row[1]['합계_금액']

print(f'특수은행 평균: {special/len(special)}')

