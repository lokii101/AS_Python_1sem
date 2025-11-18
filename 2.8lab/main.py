def find_min_year(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        years = []
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('-')
                last_part = parts[-1].strip()
                if '.' in last_part:
                    date_parts = last_part.split('.')
                    if len(date_parts) == 3:
                        year_str = date_parts[-1]
                        if year_str.isdigit():
                            year = int(year_str)
                            years.append(year)
                        else:
                            print({line})
                    else:
                        print({line})
                else:
                    if last_part.isdigit():
                        year = int(last_part)
                        years.append(year)
                    else:
                        print({line})
    return min(years) if years else None
min_year = find_min_year(r"C:\Users\253810\Desktop\111.txt")
print(min_year)
