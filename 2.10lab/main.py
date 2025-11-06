# а) Необходимо открыть файл с заданным именем. Если файл не существует, вывести сообщение «Файл не найден». Если файл не является текстовым, выбрасывается исключение «Файл не является текстовым». В остальных случаях вывести сообщение «Файл успешно открыт». Используйте исключения FileNotFoundError и TypeError.б) Необходимо проверить, является ли введенная пользователем строка числом. Если строка не является числом, выбрасывается исключение «Строка не является числом». В остальных случаях выводится сообщение «Строка является числом».в) Необходимо открыть файл с заданным именем. Если файл не существует, используя инструкцию assert, проверить условие и вывести сообщение «Файл не найден». Если файл не является текстовым, выбрасывается исключение «Файл не является текстовым». В остальных случаях вывести сообщение «Файл успешно открыт».
А) def open_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Файл успешно открыт")
    except FileNotFoundError:
        print("Файл не найден")
    except TypeError:
        print("Файл не является текстовым")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
open_text_file("example.txt")

Б) def check_if_number(user_input):
    try:
        float(user_input)
        print("Строка является числом")
    except ValueError:
        raise TypeError("Строка не является числом")
    except Exception:
        raise TypeError("Строка не является числом")
try:
    user_input = input()
    check_if_number(user_input)
except TypeError as e:
    print(e)

В) def open_text_file_with_assert(filename):
    assert os.path.exists(filename), "Файл не найден"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Файл успешно открыт")
    except TypeError:
        print("Файл не является текстовым")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
import os
try:
    open_text_file_with_assert("example.txt")
except AssertionError as e:
    print(e)
