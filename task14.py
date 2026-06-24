def array_chunk(array: list[int], left: int, right: int) -> int:
    # {P: True} array_chunk(array, left, right) {Q: res = pivot_index and array[n1] <= array[res] and n1 >= 0 and n1 < res and array[n2] >= array[res] and n2 > res and n2 < len(array)}
    # На вход подаем любой массив и индексы для сортировки
    # На выходе получаем индекс опроного элемента и соритруем массив на месте так, что все элементы левее этого индекса меньше или равны данному элементу, а все элементы правее больше или равны.
    pivot_index: int = (right - left) // 2 + left
    pivot: int = array[pivot_index]
    i1: int = left
    i2: int = right
    while i1 <= i2:
        # {I: i1 <= i2 and pivot_index >= i1 and pivot_index <= i2}
        if array[i1] < pivot:
            i1 += 1
            continue
        if array[i2] > pivot:
            i2 -= 1
            continue
        if i1 == i2 - 1 and array[i1] > array[i2]:
            array[i1], array[i2] = array[i2], array[i1]
            i1 = left
            i2 = right
            pivot_index = (right - left) // 2 + left
            pivot = array[pivot_index]
            continue
        if i1 == i2 or (i1 == i2 - 1 and array[i1] < array[i2]):
            return pivot_index
        array[i1], array[i2] = array[i2], array[i1]
        if i1 == pivot_index:
            pivot_index = i2
            continue
        if i2 == pivot_index:
            pivot_index = i1
    return pivot_index


def quickSort(array: list[int], left: int, right: int) -> None:
    # {P: True} quickSort(array, left, right) {Q: array[n] <= array[n+1] and n >= left and n < right}
    # На вход подаем любой массив и индексы для сортировки
    # На выходе получаем отсритрованный массив, в котором в диапазоне индексов [left:right] элементы расположены в порядке возрастания для каждого рекурсивного вызова.
    if left >= right:
        return
    pivot_index = array_chunk(array, left, right)
    quickSort(array, left, pivot_index - 1)
    quickSort(array, pivot_index + 1, right)
