import csv
from datetime import date

FILE_NAME = "data.csv"

def read_sales_data(file_path: str) -> list[dict]:
    """
    Функция принимает путь к файлу и возвращает список (list) продаж.
    Продажи в свою очередь являются словарем (dict) с ключами:
    
    product_name (название) -> str
    quantity (количество) -> int
    price (цена) -> float
    date (дата) -> date
    """
    # Открытие файла CSV в режиме чтения
    with open(FILE_NAME, 'r', newline='') as file:
        # Список продаж
        data_list_sales = []
        reader = csv.reader(file)

        # Получение заголовков столбцов
        headers = next(reader)

        # Создание словаря для каждой строки
        for row in reader:
            row_dict = {}
            for i, value in enumerate(row):
                row_dict[headers[i]] = value
            data_list_sales.append(row_dict)

    return data_list_sales

def total_sales_per_product(sales_data: list) -> dict:
    """
    Функция принимает список продаж и возвращает словарь,
    где ключ - название продукта,
    а значение - общая сумма продаж этого продукта.
    """

if __name__ == "__main__":

    sales_data = read_sales_data(FILE_NAME)



