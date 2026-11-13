import re #для поиска слов
import csv #для сохранения таблицы
import matplotlib.pyplot as plt #для графиков
from docx import Document #для чтения ворда

d = Document("lion.docx") #открываем вордовский файл
abz = [p.text for p in d.paragraphs] #берем текст из всех абзацев
txt = " ".join(abz).lower() #соединяем в одну строку и делаем мелкие буквы

alf = "а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я".split() #делим алфавит на список букв
kol_b = [txt.count(x) for x in alf] #считаем сколько раз каждая буква есть в тексте

slova = re.findall(r"[а-яё]+", txt) #вытаскиваем только русские слова
slovar = {} #пустой словарь для слов
for s in slova: #идем по всем словам
    slovar[s] = slovar.get(s, 0) + 1 #считаем сколько раз попалось слово

with open("itog.csv", "w", newline="", encoding="utf-8-sig") as f: #создаем файл таблицы
    wr = csv.writer(f, delimiter=";") #настраиваем запись через точку с запятой
    wr.writerow(["Слово", "Частота встречи, раз", "Частота встречи в %"]) #пишем названия колонок
    for k in slovar: #перебираем все уникальные слова
        wr.writerow([k, slovar[k], round((slovar[k] / len(slova)) * 100, 2)]) #записываем слово количество и процент

plt.bar(alf, kol_b, color="orange", edgecolor="black") #рисуем столбцы гистограммы
plt.show() #показываем график на экран

