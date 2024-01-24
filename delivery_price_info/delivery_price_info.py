import random
import pandas as pd

df = pd.read_csv('../delivery_place/delivery_place_v2.csv', sep=',', encoding='utf8')
# df = pd.read_csv('delivery_place_sample.csv', sep=',', encoding='utf8')
print(df.head())

total = len(df)

with open('delivery_price_info.csv', 'w', encoding='utf8') as file:
    delivery_price_info_id = 0
    file.write('delivery_price_info_id,delivery_price,order_price,delivery_place_id\n')

    for index, row in df.iterrows():
        max_delivery_price = 0
        min_delivery_price = 999999999999
        min_order_price = 999999999999


        if index % 1000 == 0:
            print(f'{index/total:.2%}')

        for _ in range(3):
            delivery_price_info_id += 1
            delivery_price = random.randint(0, 10) * 500
            order_price = 10000 + random.randint(0, 40) * 1000

            if max_delivery_price < delivery_price:
                max_delivery_price = delivery_price
            if min_delivery_price > delivery_price:
                min_delivery_price = delivery_price
            if min_order_price > order_price:
                min_order_price = order_price

            file.write(f'{delivery_price_info_id},'
                       f'{delivery_price},'
                       f'{order_price},'
                       f'{row["delivery_place_id"]}\n')

        df.loc[index, 'max_delivery_price'] = max_delivery_price
        df.loc[index, 'min_delivery_price'] = min_delivery_price
        df.loc[index, 'min_order_price'] = min_order_price

df.to_csv('delivery_place_240122.csv', index=False, encoding='utf8')

print('저장 완료')
