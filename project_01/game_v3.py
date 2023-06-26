import numpy as np

def random_predict(number:int=1) -> int:
    """игра угадай число. 
    компьютер загадывает и угадывает число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    predict_number = np.random.randint(1,101) # предполагаемое число
    while predict_number != number:
       
        if predict_number < number:
            while True:
                count += 1
                predict_number += 10
                if predict_number >= number:
                    break
                
            if number == predict_number:
                break
            
            while predict_number != number:
                count += 1
                predict_number -= 1
        
        if predict_number > number:
            while True:
                count += 1
                predict_number -= 10
                if predict_number <= number:
                    break
                
            if number == predict_number:
                break
            
            while predict_number != number:
                count += 1
                predict_number += 1
    
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)
