
def fibonacci(n):

    first_num, second_num = 0, 1

    for _ in range(n):
        yield first_num
        first_num, second_num = second_num, first_num + second_num

def main():
    user_input = int(input("Введите количество чисел Фибоначчи: "))

    print(list(fibonacci(user_input)))


if __name__ == '__main__':
    main()
