

def func_generator(end_num):

    for i in range(1, end_num + 1):
        yield pow(i, 2)




def main():
    user_end_num = int(input("Введите число, до которого хотите получить последовательность из квадратов чисел: "))

    print("\nВывод чисел с помощью генератора функций")
    print(list(func_generator(user_end_num)))


    print("\nВывод чисел с помощью генераторного выражения")
    gen_expression = [pow(i, 2) for i in range(1, user_end_num + 1)]
    print(gen_expression)

    # ЕЩЕ ГЕНЕРАТОРНОЕ ВЫРАЖЕНИЕ, ЭТО КЛАССИЧЕСКИЙ ЦИКЛ FOR 

if __name__ == '__main__':
    main()