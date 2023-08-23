# TODO решите задачу
import json

INPUT = 'input.json'

with open(INPUT) as file:
    load_json_file = json.load(file)


def task(load_file) -> float:
    new_list = []
    for value in load_file:
        new_list.append(value["score"] * value["weight"])
        sum_new_list = sum(new_list)
    return (f"{sum_new_list:.3f}")


print(task(load_json_file))
