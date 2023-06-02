import Task_1
import Task_2_1


current_list = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]

if __name__ == '__main__':
    # Задача 1.
    print(Task_1.creat_list_from_apple(current_list))
    print(Task_1.creat_list_from_apple_2(current_list))

    # Задача 2.
    cow = Task_2_1.Animal('Zorka', 'brown', 'My MY')
    cat = Task_2_1.Animal('Vasia', 'white', 'Miay Miay')
    dog = Task_2_1.Animal('Reks', 'black', 'Gav Gav')

    Task_2_1.animal_description(cow)
    Task_2_1.animal_description(cat)
    Task_2_1.animal_description(dog)


