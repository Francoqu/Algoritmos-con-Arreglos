def selection_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arreglo[j] < arreglo[min_idx]:
                min_idx = j
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]
    return arreglo
