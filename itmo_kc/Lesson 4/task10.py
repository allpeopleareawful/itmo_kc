import numpy as np

def detect_outliers(x: np.ndarray) -> np.ndarray:

    # вычисляем квартили
    Q1 = np.percentile(x, 25)
    Q3 = np.percentile(x, 75)

    # вычисляем межквартильный размах
    IQR = Q3 - Q1

    # вычисляем границы
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # возвращаем массив-маску
    return ((x < lower) | (x > upper))


# Представим, что это оценки по тесту в классе.
# Большинство учеников получили баллы от 60 до 85,
# но есть пара подозрительно низких и высоких значений.

scores = np.array([70, 75, 80, 65, 83, 78, 74, 72, 68, 69, 150, 20])

outliers_mask = detect_outliers(scores)

print("Оценки:", scores)
print("Маска выбросов:", outliers_mask)

# Для удобства выведем сами выбросы
print("\nНайденные выбросы:")
print(scores[outliers_mask])

### Output:

# Оценки: [ 70  75  80  65  83  78  74  72  68  69 150  20]
# Маска выбросов: [False False False False False False False False False False  True  True]

# Найденные выбросы:
# [150  20]
