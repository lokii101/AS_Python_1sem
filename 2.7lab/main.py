def remove_line_from_file(filename, k):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if 1 <= k <= len(lines):
            lines.pop(k - 1)
            with open(filename, 'w', encoding='utf-8') as file:
                file.writelines(lines)
    except FileNotFoundError:
        print({filename})
    except PermissionError:
        print({filename})
    except Exception as e:
        print({e})
