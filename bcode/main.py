import pandas as pd

df = pd.read_csv('법정동코드 전체자료.txt', sep ='\t', encoding='ms949')
print(df.head())
print(df.iloc[0])
print(df.iloc[0]['폐지여부'])

delRows = []

for index, row in df.iterrows():
    if df.iloc[index]['폐지여부'] == '폐지':
        delRows.append(index)


print(len(delRows))


df = df.drop(delRows, axis=0)
df = df.drop(['폐지여부'], axis=1)
df.to_csv('법정동코드.csv', index=False, encoding='ms949')

print("저장 완료")