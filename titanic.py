from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def process_and_visualize_titanic():
    # Определяем исходную папку (директорию, в которой находится сам скрипт)
    base_dir = Path(__file__).resolve().parent
    parquet_path = base_dir / 'titanic.parquet'
    csv_path = base_dir / 'titanic.csv'

    # 1. Читаем файл titanic.parquet
    if not parquet_path.exists():
        print(f'Ошибка: файл {parquet_path} не найден в исходной папке.')
        return

    df_parquet = pd.read_parquet(parquet_path)

    # 2. Переводим в формат CSV и сохраняем в исходную папку
    df_parquet.to_csv(csv_path, index=False, encoding='utf-8')
    print(f'Файл успешно конвертирован и сохранен по пути: {csv_path}')

    # 3. Открываем сохраненный CSV-файл для проверки корректности
    df_csv = pd.read_csv(csv_path)
    print(
        f'Проверка успешна: загружено {df_csv.shape[0]} строк и'
        f' {df_csv.shape[1]} столбцов.'
    )

    # 4. Подготавливаем данные и отображаем гистограмму выживаемости по классам
    survival_by_class = pd.crosstab(df_csv['Pclass'], df_csv['Survived'])
    survival_by_class.columns = ['Погибли (0)', 'Выжили (1)']

    ax = survival_by_class.plot(
        kind='bar',
        figsize=(9, 6),
        color=['#d9534f', '#5cb85c'],
        edgecolor='black',
    )

    plt.title(
        'Выживаемость пассажиров Титаника в зависимости от класса билета',
        fontsize=14,
        pad=15,
    )
    plt.xlabel('Класс билета (Pclass)', fontsize=12)
    plt.ylabel('Количество пассажиров', fontsize=12)
    plt.xticks(
        ticks=[0, 1, 2],
        labels=['1-й класс', '2-й класс', '3-й класс'],
        rotation=0,
    )
    plt.legend(title='Статус')
    plt.grid(axis='y', linestyle='--', alpha=0.6)

    # Добавляем числовые значения над каждым столбцом
    for container in ax.containers:
        ax.bar_label(container, padding=3, fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    process_and_visualize_titanic()
#Создайте файл «titanic.py».
#В файле реализуйте программный код, который прочитает файл titanic.parquet, переведет его наполнение в формат csv и сохранит в исходную папку. Для проверки корректности сохранения файла в формате csv откройте его и отобразите гистограмму выживаемости пассажиров в зависимости от класса билета. 
