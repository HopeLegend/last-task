import random

def xod_compuctera(N):
    if N > 5 and N <= 8:
        return N-5
    elif N > 8:
        return random.randint(1, 3)
    elif N <= 4:
        return N-1

    elif N == 5:
        return random.randint(1, 3)


def get_count_test(temp,count):
    temp = int(input())
    while temp < 1 or temp > 3:
        try:
            print('Число не удовлетворяет условию задачи. Попробуйте еще раз:')
            temp = int(input())
        except:
            print('Число не удовлетворяет условию задачи. Попробуйте еще раз:')
            temp = int(input())
    return temp

N = random.randint(3, 40)
temp = 0
print('В кучке находится', N, 'камня(-ей)')
while N > 1:
    count = xod_compuctera(N)
    N -= count
    print('ход компьютера')
    print('Компьютер берет из кучки', count, 'камней. В куче осталось',N,'камней')
    if N == 1:
        print('Компьютер побеждает')
        exit()
    print('Ход игрока')
    print('Введите, сколько камней вы хотите взять(от 1 до 3): ')
    count = get_count_test(temp,count)
    N -= count
    print('Вы берете из кучки', count, 'камней. В куче осталось', N, 'камней')
    if N == 1:
        print('Игрок побеждает')
        exit()



