from gtts import gTTS      #основной модуль для связи c api гугла для превращение текстого файла в звуковой
import pdfplumber          #для работы с пдф файлыми(плохо работает с текстом как фото)
from pathlib import Path   #для работы с файлами и проверки что он исуществуют
from art import tprint     #для визуализации командной строки
def pdf_to_mp3(file_path='test.pdf', language='en'):                    #принимает 2 параметра: путь до файла и язык для аудиодорожки
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':  #проверка что файл существует(класс Path из athlib и метод is file) и проверяем что суффикс оканчивается на .pdf
        print(f'[+] Original file: {Path(file_path).name}')             #берем название файла после получения пути до файла
        print('[+] In Process...')                                      #показываем что работа в процессе
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:    #читаем пдф файл в обычную строку(юзаем контекстныйц менеджер with и обращаемся к классу PDF модуляpdfplumber)
                                                                        # в параметрах которого открываем файл на чтение в двоичном режиме с помощью флага rb
            pages = [page.extract_text() for page in pdf.pages]         #нужно пройтись по всем страницам, используем конструкцию list comprehension (for page in pdf.pages)
                                                                        # и извлекаем текст из каждой (page.extract_text())
        text = ''.join(pages)                                           #метод join для склейки страниц между собой
        with open('text1.txt', 'w') as file:                            #сохраняем текст в файл до переноса символов--->>>
            file.write(text)                                            #----->>>
        text = text.replace('\n', '')                                   #методом replace заменяем все переносы строки на пустату(что озвучка не становилась на долгую паузу при переносах строки)
        with open('text2.txt', 'w') as file:                            #сохраняем текст в файл после переноса символов(ТЕКСТЫ ИСПОЛЬЗУЮТСЯ МОДУЛЕМ gTTS ДЛЯ ЧТО БЫ ПРЕВРАТИТЬ В ГОЛОС)--->>>
            file.write(text)                                            #----->>>
        my_audio = gTTS(text=text, lang=language, slow=False)           #обращаемся к классу gTTS в параметры передаем текст язык и скорость чтения машиной (fals = обычная скорость)
                                                                        # (значения которой мы будем получать из параметров функций)
        file_name = Path(file_path).stem                                #получаем ия файлв с помощь юсвойства stem
        my_audio.save(f'{file_name}.mp3')                               #сохраним аудиофайл обратившись к методу save в параметры которого передаем имя файла(строчка кода выше)

        return f'[+]{file_name}.mp3 saved successfully!\n'             #если файл существует и он пдф и код может его пропустить то выдаем следующее

    else:
        return 'File not Ok chek the file path'                        #иначе передаем что файл не ок
def main():                                                            #для читаемости запускаем код с main
    tprint('Amiram_Art -- PDF>>TO>>MP3')                               #шапка для красоты
    file_path = input("\n Enter a file path: ")                        #запрашиваем у пользователя путь до файла и зписываем в переменную file_path после чего будет передана как аргумент
    language = input("Choose the file language 'en' or 'ru': ")        #запрашшиваем выбора языка(ВСЕ ПЕРЕМЕННЫЕ ПЕРЕДАЕЮТСЯ В ПАРАМЕТРЫ ФУНКЦИИ "pdf_to_mp3"
    print(pdf_to_mp3(file_path=file_path, language=language))          #подставляем полученные аргументы в нашу функцию

if __name__ == '__main__':                                             #пока не до конца понял зачем такое делать но надо
    main()


#Минусы:
#Пока нет проверки если текст пдф файла идет как фотография а не как машинный текст.
#
#
#
#
#
#Links
#Файлы в python, ввод-вывод
#https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
#Руководство по использованию list comprehension
#https://pythonru.com/osnovy/python-list-comprehension#:~:text=List%20comprehension%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D1%83%D0%BF%D1%80%D0%BE%D1%89%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%BF%D0%BE%D0%B4%D1%85%D0%BE%D0%B4,%D0%B8%D1%82%D0%BE%D0%B3%D0%B5%20%D0%BE%D0%BA%D0%B0%D0%B6%D0%B5%D1%82%D1%81%D1%8F%20%D0%B2%20%D1%84%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%BC%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B5.
#
#
#
#
