from time import time

def sqrt(N:int):
    for i in range(N):
        # Находим квадрат
        sq = i * i

        # Если он равен числу, то выводим его
        if sq == N:
            return i
        
        # Если он больше числа, то уже поздно и выводим None
        if sq > N:
            return None


def binary_sqrt(N:int):
    # Выделяем интервал
    start_num = 0
    end_num = N//2 + 1      # +1, что б 4 правильно находилось
    
    # Пока интервал не сблизился
    while end_num-start_num != 1:
        # Находим серидину интервала
        new_num = (end_num - start_num) // 2 + start_num
        
        # Если квадрат числа больше N
        # Из-за строгого сравнения, конец интервала не будет равен квадрату
        if new_num**2 > N:  
            end_num = new_num       # Теперь это конец интервала
        else:
            start_num = new_num     # Или теперь это начало
    
    # Проверяем, корень ли мы нашли и выводим ответ
    if start_num**2 == N:
        return start_num
    else:
        return None 


# На небольших числах обычный быстрее
N = 10000000000

start = time()
print(binary_sqrt(N))
print(time() - start, "Бинарный")

start = time()
print(sqrt(N))
print(time() - start, "Обычный")