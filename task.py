import random   
import timeit

def generate_test_data():
    # Список відсортованих чисел
    sorted_list = list(range(1, 101))
    
    # Список у зворотному порядку
    reversed_list = sorted_list[::-1]
    
    # Список випадкових чисел
    random_list = random.sample(range(1, 101), 100)
    
    # Список з багатьма однаковими елементами
    duplicate_list = [random.choice(range(1, 11)) for _ in range(100)]
    
    # Список з майже відсортованими даними (з деякими перемішаними елементами)
    almost_sorted_list = sorted_list[:]
    random.shuffle(almost_sorted_list[:10])
    
    return sorted_list, reversed_list, random_list, duplicate_list, almost_sorted_list


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list



def python_sort(data):
    return sorted(data)


sorted_list, reversed_list, random_list, duplicate_list, almost_sorted_list = generate_test_data()
data_set = generate_test_data()


sorted_time = dict()
for sort_type in ["python_sort", "merge_sort", "insertion_sort"]:
    type_sorted_time = []
    for list in data_set:
        type_sorted_time.append(timeit.timeit(f'{sort_type}({list})', globals=globals(), number=1000))
    sorted_time[sort_type] = type_sorted_time  

print(sorted_time)

for type in sorted_time:
    print(f"Тип сортування {type}")
    print(f"Час сортування відсортованого списку: {sorted_time[type][0]:.6f} секунд")
    print(f"Час сортування списку у зворотному порядку: {sorted_time[type][1]:.6f} секунд")
    print(f"Час сортування випадкового списку: {sorted_time[type][2]:.6f} секунд")
    print(f"Час сортування списку з багатьма однаковими елементами: {sorted_time[type][3]:.6f} секунд")
    print(f"Час сортування майже відсортованого списку: {sorted_time[type][4]:.6f} секунд\n")