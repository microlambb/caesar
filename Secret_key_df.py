p = 22
g = 8
a_private_key = 5
b_private_key = 2

#вычисляем публичные ключи А и B
public_key_A = g**a_private_key % p
public_key_B = g**b_private_key % p

#Алиса и Боб вычисляют общий секретный ключ
Alice_s = public_key_B**a_private_key % p
Bob_s = public_key_A**b_private_key % p

#если ключи совпадают, ключ записывается в одну переменную secret_key
if Alice_s == Bob_s:
    secret_key = Alice_s or Bob_s

print(secret_key)
