"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

def main(sales_list):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sales_sum = 0
    for sale in sales_list:
        sales_sum += sale
    return sales_sum

if __name__ == "__main__":
    for position in sales:
        product_sales = main(position['items_sold'])
        print(f'Суммарное количество продаж {position["product"]} - {product_sales}')

    for position in sales:
        product_sales = main(position['items_sold'])
        product_sales_avr = product_sales / len(position['items_sold'])
        print(f'Среднее количество продаж {position["product"]} - {product_sales_avr}')

    all_sales = 0

    for position in sales:
        all_sales += main(position['items_sold'])
    print(f'Суммарное количество продаж всех товаров - {all_sales}')
    print(f'Среднее количество продаж всех товаров - {all_sales / len(sales)}')
