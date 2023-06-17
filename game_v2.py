'''Игра "Угадай число" '''

import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла, если угадали
    return (count) # 


def score_game(randon_predict) -> int:
    """За какое кол-во попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        randon_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загаали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))  
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return (score)
    
# print(f'Количество попыток: {random_predict(10)}')

if __name__ == '__main__':
    score_game(random_predict)