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

    def filter_customers(self, min_age):
        return [c for c in self.customers_data if (c.get("age") or 0) >= min_age]

    def add_customer(self, name, age):
        self.customers_data.append({'name': name, 'age': age})
        self.last_update = datetime.now()

    def update_data(self, new_data):
        self.customers_data = new_data
        self.last_update = datetime.now()

    def __contains__(self, customer_name): 
        return any(c.get('name') == customer_name for c in self.customers_data)

    def __repr__(self):
        return f'CustomerDataset({len(self)} customers from \'{self.source}\')'

    def __len__(self):
        return len(self.customers_data)

def process_customers(dataset: CustomerDataset):
    print('Обработка покупателей...')
    dataset.display_info()
    print('Готово.')

ds = CustomerDataset([], "data.csv")

process_customers(ds)

class PremiumCustomerDataset(CustomerDataset):
    def __init__(self, customers_data, source, membership_level):
        super().__init__(customers_data, source)
        self.membership_level = membership_level

    def filter_by_membership(self, level):
        return [c for c in self.customers_data if c.get("membership") == level]

    def display_info(self):
        super().display_info()
        print(f'Уровень членства: {self.membership_level}')