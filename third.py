def main(a:str):
    # Счётчик. 
    # '(' -> +1
    # ')' -> -1
    counter = 0
    for i in a:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        else:
            # Проверка на прочие символы в строке
            assert i == ")", "String shouldn't have anithing except ( and )"
        
        # Если закрыли лишнюю скобку (counter<0)
        if counter < 0:
            return False
            
    # Проверяем счётчик. Должен быть == 0
    if counter == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(main("())("))