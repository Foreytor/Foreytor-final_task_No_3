import csv
import matplotlib.pyplot as plt

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
                row_dict[headers[i].strip()] = value.strip()
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

def sales_over_time(sales_data: list) -> dict:
    """
    Нахождение общей суммы продаж за дату
    
    Args:
        sales_data: список продаж.

    Returns:
        возвращает словарь,
        где ключ - дата,
        а значение общая сумма продаж за эту дату
    """

    sales_by_date = {}

    for item in sales_data:
        date = item['date']
        quantity = int(item['quantity'].strip())
        price = int(item['price'].strip())
        total_price = quantity * price

        if date in sales_by_date:
            sales_by_date[date] += total_price
        else:
            sales_by_date[date] = total_price

    return sales_by_date

def sales_analytics_max_value(total_sales: dict) -> str:
    """
    Нахождение продукта с максимальной выручкой.
    
    Args:
        total_sales: Словарь с суммами по продажам.

    Returns:
        ключ словоря с максимальным значением
    """
    max_key_name = max(total_sales, key=total_sales.get)

    return max_key_name

def build_graph(total_sales: list, out_file_name: str = "file.png"):
    """
    Строит график общей суммы продаж по каждому продукту
    и сохраняет файл в текущей директории.
    Args:
        total_sales: Словарь с суммами по продажам,
        out_file_name: Выходной файл в формате png.
    """
    # сбрасываем состояние plt
    plt.clf()
    # Построение графика
    plt.bar(total_sales.keys(), total_sales.values())
    plt.xlabel('Название продукта')
    plt.ylabel('Общая сумма продаж')
    plt.title('Сумма продаж по продуктам')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(out_file_name)
    plt.show()

if __name__ == "__main__":

    # Константа имя файла
    FILE_NAME = "data.csv"

    # получаем продажи
    sales_data = read_sales_data(FILE_NAME)
    # Сумма продаж по продуктам
    total_sales = total_sales_per_product(sales_data)
    # Количество продаж по датам
    sales_by_date = sales_over_time(sales_data)
    print(sales_by_date)

    # Нахождение продукта с максимальной выручкой
    max_revenue_product = sales_analytics_max_value(total_sales)
    print(f"Продукт с максимальной выручкой: {max_revenue_product}")

    # Нахождение дня с максимальной выручкой
    max_sales_date = sales_analytics_max_value(sales_by_date)
    print(f"День с максимальной выручкой: {max_sales_date}")

    # Построение графика продаж по продуктам
    build_graph(total_sales, "sales_chart_on_name.png")

    # Построение графика продаж по дням
    build_graph(sales_by_date, "sales_chart_on_date.png")

