import math


def pearson_correlation(array_1, array_2):
    if len(array_1) != len(array_2):
        raise ValueError("массивы должны быть одного размера")

    n = len(array_1)

    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1])
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2])

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1, array_2)])
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [2, 4, 6, 8]
array_2 = [2, 4, 10, 12]


print(pearson_correlation(array_1, array_2))
