#Добавьте ing в конце заданной строки (длина должна быть не менее трех). Если данная строка уже заканчивается на ing, добавьте вместо этого ly. Если длина заданной строки меньше трех, оставьте ее без изменений.
def add_suffix(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

print(add_suffix("go"))
print(add_suffix("run"))
print(add_suffix("playing"))
