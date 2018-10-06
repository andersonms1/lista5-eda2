def partition(lista, start, end):

    pivot = lista[end]
    bottom = start - 1
    top = end

    done = 0

    while not done:
        while not done:
            bottom = bottom + 1
            if bottom == top:
                done = 1
                break

            if lista[bottom] > pivot:
                lista[top] = lista[bottom]
                break

        while not done:
            top = top - 1
            if top == bottom:
                done = 1
                break

            if lista[top] < pivot:
                lista[bottom] = lista[top]
                break

    lista[top] = pivot
    return top


def quick_sort(lista, start, end):
    if start < end:
        split = partition(lista, start, end)
        quick_sort(lista, start, split - 1)
        quick_sort(lista, split+1, end)
    else:
        return