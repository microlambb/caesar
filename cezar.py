alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"   #алфавит для шифрования
secret_key = 12   #секретный ключ
message = "ЕРМОЛИНА АНАСТАСИЯ КИРИЛЛОВНА"   #ФИО для щифровки
encrypted_message = ""   #будущее зашифрованное сообщение

for letter in message:    #проходим по каждой букве в сообщении
    if letter in alphabet:
        t = alphabet.find(letter)    #если символ входит в алфавит, методом find ищем позицию буквы и записываем в переменную t
        new_key = (t + secret_key) % len(alphabet)   #с учетом смещения на значение нашего ключа запишем в переменную new_key
        encrypted_message += alphabet[new_key]   #добавляем в encrypted_message букву с индексом new_key
    else:
        encrypted_message += letter  #если символ в алфавите не найден, просто добавляем его в зашифрованное сообщение
print(encrypted_message)
