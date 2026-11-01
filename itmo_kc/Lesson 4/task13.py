import numpy as np

def one_hot_encode(categories: np.ndarray) -> tuple[np.ndarray, list[str]]:
    unique = np.unique(categories)
    array = np.zeros([categories.shape[0], unique.shape[0]], dtype=int)
    for i in range(categories.shape[0]):
        city = categories[i]
        for j in range(unique.shape[0]):
            if unique[j] == city:
                array[i, j] = 1
        

    return array, unique.tolist()


# У нас есть список городов, в которых живут пользователи.
# Нужно превратить текстовые названия в числовую матрицу.

cities = np.array(["Москва", "СПб", "Казань", "Москва", "Екатеринбург"])

print("Исходные данные:")
print(cities)

encoded, unique_cities = one_hot_encode(cities)

print("\nУникальные категории:")
print(unique_cities)

print("\nРезультат one-hot кодирования:")
print(encoded)

### Output:
# Исходные данные:
# ['Москва' 'СПб' 'Казань' 'Москва' 'Екатеринбург']

# Уникальные категории:
# [np.str_('Екатеринбург'), np.str_('Казань'), np.str_('Москва'), np.str_('СПб')]

# Результат one-hot кодирования:
# [[0 0 1 0]
#  [0 0 0 1]
#  [0 1 0 0]
#  [0 0 1 0]
#  [1 0 0 0]]