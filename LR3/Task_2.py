def find_common_participants(participants_first_group, participants_second_group, separator = ","):
    list_first_group = participants_first_group.split(separator)
    list_second_group = participants_second_group.split(separator)
    common_set = (set(list_first_group)).intersection(list_second_group)
    common_list = sorted(list(common_set))
    return common_list
    # TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


find_common_participants(participants_first_group, participants_second_group, separator = "|")

# TODO Провеьте работу функции с разделителем отличным от запятой
