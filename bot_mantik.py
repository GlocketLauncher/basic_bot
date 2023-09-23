# bot_logic in original

import random


def sifre_olusturucu(sifre_uzunlugu):
    

    
    characters = "@+-!'^$%&/(=?*1234567890qwertyuopasdfghjklşizxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    length = int(input("Şifre ne kadar uzun olsun?"))




    password = ""
    for i in range(length):
        password += random.choice(characters)

    if not any(password[i] == password[i+1] for i in range(len(password)-1)):
        return password


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 2)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
