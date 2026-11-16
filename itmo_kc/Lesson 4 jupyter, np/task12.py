import numpy as np

def fill_na_with_median(X: np.ndarray) -> np.ndarray:
    X_filled = X.copy()
    sum = 0
    for i in range (X_filled.shape[1]):
      median = np.nanmedian(X_filled[:, i])
      for j in range(X_filled.shape[0]):
        if np.isnan(X_filled[j, i]):
           X_filled[j, i] = median

    return X_filled

# У нас таблица измерений роста и веса трёх человек.
# В одном месте данные потерялись (nan).

X = np.array(
    [
        [170, 65],
        [160, np.nan],
        [180, 80],
    ]
)

print("Исходная таблица:")
print(X)

# Заполняем пропуски медианой каждого столбца
X_filled = fill_na_with_median(X)

print("\nТаблица после заполнения пропусков медианой:")
print(X_filled)

### Output:
# Исходная таблица:
# [[170.  65.]
#  [160.  nan]
#  [180.  80.]]

# Таблица после заполнения пропусков медианой:
# [[170.   65. ]
#  [160.   72.5]
#  [180.   80. ]]