"""
"id","created_at","updated_at","email","nickname","password","provider_type"
1,2023-11-10 21:12:07.000,2023-11-10 21:12:07.000,owner1@test.com,점주 1,$2a$10$6Oz7gxrrPvpEritioYkjNer.LtvXkAIx31ZcYow8ZwKSwukZ3BVta,DEFAULT
"""

import bcrypt

password = bcrypt.hashpw('12345678'.encode('utf-8'), bcrypt.gensalt(10)).decode('utf-8')

with open('owner.csv', 'w', encoding='utf-8') as owner:
    owner.write('id,created_at,updated_at,email,nickname,password,provider_type\n')
    for owner_id in range(1, 102701):
        if owner_id % 1000 == 0:
            print(f'{owner_id/102700:.2%}')

        owner.write(f'{owner_id},2023-11-10 21:12:07.000,2023-11-10 21:12:07.000,owner{owner_id}@test.com,점주 {owner_id},{password},DEFAULT\n')


print('저장 완료')