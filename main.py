def sum_negatives_between_min_max(arr):
    """
    задание 3
    """
    if not arr:
        return 0  # Если массив пустой
    
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    
    start = min(max_index, min_index)
    end = max(max_index, min_index)
    
    total_sum = 0
    for i in range(start + 1, end):  
        if arr[i] < 0:
            total_sum += arr[i]
            
    return total_sum

# Пример использования:
if __name__ == "__main__":
    A = [3, -5, 2, -1, 8, -4, 0, -2, 7, -3]
    N = len(A)
    
    result = sum_negatives_between_min_max(A)
    print(f"Массив: {A}")
    print(f"Сумма отрицательных элементов между максимумом и минимумом: {result}")
