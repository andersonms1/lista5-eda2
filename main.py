import matplotlib.pyplot as plt
from ordena import quick_sort, bubble, insertion_sort, selection_sort
from sortTimer import SortTimer
import random


lista = []

print("Escolha uma opção de vetor")
print("1 - Aleatorio")
print("2 - Inverso Ordenado")
print("3 - Ordenado")
opc = input()

if(opc == '1'):
    lista = random.sample(range(100), 100)
elif(opc == '2'):
    lista = list(range(100, 0, -1))
elif(opc == '3'):
    lista = list(range(0, 100))


timer = SortTimer(lista)


data_quick = timer.get_time_taken(quick_sort, True)


plt.plot(data_quick["n_of_elements"], data_quick["time_taken"], label='quick')

plt.legend()
plt.show()