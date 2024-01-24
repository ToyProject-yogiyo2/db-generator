import random
import pandas as pd

df = pd.read_csv('../bcode/법정동코드.csv', sep=',', encoding='ms949')
print(df.head())

with open('delivery_place.csv', 'w', encoding='utf8') as file:
    delivery_place_id = 0
    file.write('delivery_place_id,code,delivery_time,max_delivery_price,min_delivery_price,min_order_price,name,shop_id\n')

    for shopId in range(1, 1062562):  # 1062562
        if shopId % 1000 == 0:
            print(f'{shopId}/1062561')

        df_bcode = df.sample(n=10)
        for index, row in df_bcode.iterrows():
            delivery_place_id += 1
            file.write(f'{delivery_place_id},{row["법정동코드"]},{random.randint(30, 60)},{random.randint(4000, 5000)},{random.randint(0, 3000)},{random.randint(10000, 15000)},{row["법정동명"]},{shopId}\n')

print('저장 완료')
