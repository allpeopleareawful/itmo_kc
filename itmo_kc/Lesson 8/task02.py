from datetime import datetime

class CustomerDataset:
    def __init__(self, customers_data, source):
        self.customers_data = customers_data
        self.source = source
        self.last_update = datetime.now()

    def display_info(self):
        print(f"Источник: {self.source}")
        print(f"Последнее обновление: {self.last_update}")
        print(f"Количество покупателей: {len(self.customers_data)}")


def process_customers(dataset: CustomerDataset):
    print('Обработка покупателей...')
    dataset.display_info()
    print('Готово.')

ds = CustomerDataset([], "data.csv")

process_customers(ds)