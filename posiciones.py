

def bubble_sort_reverse(vector):
    n = len(vector)
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

vector = [1,31,23,47,19,54,6,27,85]
bubble_sort_reverse(vector)
print(vector)
                

def insertion_sort_reverse(vector2):
    for i in range(len(vector2),1):
        key = vector2[i]
        j = i-1
        while j >=0 and key < vector2[j] :
            vector2[j+1] = vector2[j]
            j -= 1
        vector2[j+1] = key

vector2 = [1,31,23,47,19,54,6,27,85]
insertion_sort_reverse(vector2)
print(vector2)


def selection_sort_reverse(vector3):
    for i in range(len(vector3)):
        min_idx = i
        for j in range(i+1, len(vector3)):
            if vector3[min_idx] > vector3[j]:
                min_idx = j
        vector3[i], vector3[min_idx] = vector3[min_idx], vector3[i]

vector3 = [1,31,23,47,19,54,6,27,85]
selection_sort_reverse(vector3)
print(vector3)

