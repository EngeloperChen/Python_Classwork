number_1 = input("Enter number1: ")
number_2 = input("Enter number2: ")
number_3 = input("Enter number3: ")
number_4 = input("Enter number4: ")
number_5 = input("Enter number5: ")


def get_max_and_min(number1, number2, number3, number4, number5):
    number_list = [number1, number2, number3, number4, number5]
    number_list.sort()
    max_number = number_list[4]
    min_number = number_list[0]
    return "最大值为" + max_number + "。最小值为" + min_number + "。"


print(get_max_and_min(number_1, number_2, number_3, number_4, number_5))
