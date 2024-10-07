input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
data = input_data.read() # чтение файла ввода
N = int(data)
A = 0
if N>0:
    for i in range (1, N+1):
     A = A + i
elif N<0:
    for i in range (N, 2):
     A = A + i
elif N == 0:
    A = 1
      

output_data = open('output.txt', 'w') # создание и открытие файла для вывода ответа
output_data.write(str(A)) # преобразование числа в строку при выводе и сам вывод
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода


