
def dict_by_names_bonus(list_names, list_salary, list_bonus):
    new_list_bonus = []
    # new_list_bonus = [new_list_bonus[i].append(list_bonus[i].strip('%')) for i in range(len(list_bonus + 1))]
    for i in range(len(list_bonus)):
        new_list_bonus.append(list_bonus[i].strip('%'))

    result = {list_names[i]: round(list_salary[i] * float(new_list_bonus[i]) // 100, 3) for i in range(len(list_names))}

    return result





def main():
    user_names = input("Введите имена работников через ',' : ").split(",")
    user_salary = list(map(int,  input("Введите ставку работника через ',' : ").split(",")))
    user_bonus = input("Введите строку с указанием премии для работника через  ',': ").split(",")

    result = dict_by_names_bonus(user_names, user_salary, user_bonus)
    print("Премии работников - ", result)


if __name__ == '__main__':
    main()