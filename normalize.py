import re
import os

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "i", "ji", "g")


TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    file_name, ext = os.path.splitext(name) #splitext ігнорує всі . у назві, бере лише останню. Розділяємо окремо назву файлу і його розширення
    file_name = file_name.translate(TRANS)
    file_name = re.sub(r'[\W]+', '_', file_name)
    # print(file_name)
    # print(ext)    
    return str(file_name + ext)

# print(normalize('Якийсь-файл.bmp'))

