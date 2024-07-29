import csv
from datetime import date

def read_sales_data(file_path: str) -> list[dict]:
    """
    Функция принимает путь к файлу и возвращает список (list) продаж.
    Продажи в свою очередь являются словарем (dict) с ключами:
    
    Args:
        file_path: Имя файла CSV.

    Returns:
        Список словарей, 
        где каждый словарь представляет строку из файла CSV.
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
                row_dict[headers[i].strip()] = value
            data_list_sales.append(row_dict)

    return data_list_sales

def total_sales_per_product(sales_data: list) -> dict:
    """
    Нахождение общей суммы продаж по продуктам
    
    Args:
        sales_data: список продаж.

    Returns:
        возвращает словарь,
        где ключ - название продукта,
        а значение - общая сумма продаж этого продукта.
    """

    total_sales = {}

    for product in sales_data:
        product_name = product['product_name']
        # Преобразуем строку в число
        quantity = int(product['quantity'].strip())
        # Преобразуем строку в число
        price = float(product['price'].strip()) 

        # Если продукт уже есть в словаре, прибавляем к существующей сумме
        if product_name in total_sales:
            total_sales[product_name] += quantity * price
        else:
            # Иначе создаем новую запись в словаре
            total_sales[product_name] = quantity * price
    return total_sales

if __name__ == "__main__":

    # Константа имя файла
    FILE_NAME = "data.csv"

    # получаем продажи
    sales_data = read_sales_data(FILE_NAME)
    # Сумма продаж по продуктам
    total_sales = total_sales_per_product(sales_data)
    print(total_sales)



