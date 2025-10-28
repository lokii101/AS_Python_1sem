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
