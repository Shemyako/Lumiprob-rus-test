
def main(a:str):
    # Проверка на пустую строку
    if len(a) == 0:
        return ('', 0)

    # Всё к нижнему регистру
    a = a.lower()
    # Ищем самую чатсую букву
    answer = (max(a, key=lambda ch: a.count(ch)))
    # Возвращаем котреж (буква, сколько их)
    return (answer, a.count(answer))

if __name__ == "__main__":
    # Принимаем строку
    a = input()
    # Выводим ответ
    print(main(a))