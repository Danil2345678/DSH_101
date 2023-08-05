# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, separator=","):
    first_team_separator = group_1.split(separator)
    second_team_separator = group_2.split(separator)
    joint_people = list(set(first_team_separator).intersection(second_team_separator))
    joint_people.sort()
    return joint_people

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
