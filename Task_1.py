#Задача 1. Представлен список из значений "Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro",
#"Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro".
#Необходимо создать новый список, содержащий модели бренда Apple.

def creat_list_from_apple(target_list):
    list_apple = []
    for i in range(0, len(target_list)):
        elem_from_cur_list = target_list[i]
        string_from_elem = str(elem_from_cur_list).split()
        if string_from_elem.count('Apple') == 1:
            list_apple.append(target_list[i])
    return list_apple

#Второй способ получения списка


def creat_list_from_apple_2(target_list):
    list_apple_2 = []
    for i in range(0, len(target_list)):
        if target_list[i].__contains__('Apple'):
            list_apple_2.append(target_list[i])
    return list_apple_2


#Третий способ получения списка
def creat_list_from_apple_3(target_list):
    list_apple = list(filter(lambda x: x.__contains__('Apple'), target_list))
    return list_apple
