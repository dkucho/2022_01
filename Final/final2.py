import pandas as pd
g_data = [[80, 90, 100],[75, 78, 90],[100, 80, 95]]
df = pd.DataFrame(g_data, columns=['국어', '수학', '영어'],index=['철수','영희','동수'])
print(df)


df['총점']=df.sum(axis=1)
print(df)

df.to_excel('result.xlsx',index=False)
