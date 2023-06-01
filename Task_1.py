#Задача 1. Представлен список из значений "Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro",
#"Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro".
#Необходимо создать новый список, содержащий модели бренда Apple.


current_list = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]
list_apple = []


def creat_list_from_apple():

    for i in range(0, len(current_list)):
        elem_from_cur_list = current_list[i]
        string_from_elem = str(elem_from_cur_list).split()
        if string_from_elem.count('Apple') == 1:
            list_apple.append(current_list[i])
    if list_apple:
        return print(list_apple)
    else:
        return print('Моделей бренда Apple в текущем списке нет')


#Второй способ получения списка

list_apple_2 = []


def creat_list_from_apple_2():

    for i in range(0, len(current_list)):
        if current_list[i].__contains__('Apple'):
            list_apple_2.append(current_list[i])
    return print(list_apple_2)
