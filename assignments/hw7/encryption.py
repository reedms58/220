def encode(message, special_key):
    ordinals = []
    key = eval(special_key)
    for character in message:
        num = ord(character)
        shift = num + key
        new_num = chr(shift)
        ordinals.append(new_num)
    output = "".join(ordinals)
    print(output)


def encode_better(message, key):
    key_len = len(key)
    length = len(message)
    encoded_mess = ''
    for i in range(length):
        shift = ord(key[i % key_len]) - 65
        num = ord(message[i]) - 65
        new_num = (num + shift) % 58
        characters = chr(new_num + 65)
        encoded_mess = encoded_mess + characters
    print(encoded_mess)
