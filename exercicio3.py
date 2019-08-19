from statistics import mean

num_pri = float(input('Digite o primeira numero: '))
num_sec = float(input('Digite o segundo numero: '))

lista_notas = [num_pri, num_sec]
media = mean(lista_notas)
print(media)
