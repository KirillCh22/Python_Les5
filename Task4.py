
def substrings(s):
    len_s = len(s)

    for start in range(len_s + 1):
        for end in range(start + 1, len_s + 1):
            yield s[start:end]



def main():
    user_string = input("Введите строку: ")

    print(list(substrings(user_string)))


if __name__ == '__main__':
    main()