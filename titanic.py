import pandas as pd #подключаем pandas для работы с таблицами
import matplotlib.pyplot as plt #подключаем библиотеку для графиков

df = pd.read_parquet("titanic.parquet") #читаем исходный файл parquet
df.to_csv("titanic.csv", index=False) #переводим данные в формат csv и сохраняем

tab = pd.read_csv("titanic.csv") #открываем сохраненный csv файл для проверки
svod = pd.crosstab(tab["Pclass"], tab["Survived"], normalize="index") * 100 #считаем процент выживших по каждому классу
svod = svod[[1, 0]] #меняем столбцы местами чтобы выжившие были снизу
svod.columns = ["Выжил", "Не выжил"] #меняем 1 и 0 на понятные подписи
svod.index = ["первый класс", "второй класс", "третий класс"] #подписываем номера классов словами

svod.plot(kind="bar", stacked=True, color=["royalblue", "darkorange"], width=0.35) #строим столбцы друг на друге
plt.title("Выживаемость пассажиров Титаника", pad=30) #добавляем заголовок и немного поднимаем его
plt.xlabel("") #убираем стандартную подпись оси снизу
plt.yticks([0, 50, 100], ["0%", "50%", "100%"]) #делаем деления слева в процентах
plt.xticks(rotation=0) #ставим подписи классов горизонтально
plt.legend(loc="lower center", bbox_to_anchor=(0.5, 1.01), ncol=2, frameon=False) #выносим обозначение цветов над графиком
plt.grid(axis="y", color="gray", alpha=0.5) #добавляем горизонтальные линии сетки
plt.show() #выводим готовый график на экран



