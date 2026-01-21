# TODO решите задачу
import json
def task(input_) -> float:

    try:
        with open(input_, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("JSON файл должен содержать список словарей.")
        total_sum = 0.0
        for item in data:
            if "score" not in item or "weight" not in item:
                raise KeyError(f"В словаре отсутствуют необходимые ключи: {item}")
            total_sum += item["score"] * item["weight"]
        rounded_sum = round(total_sum, 3)
        return rounded_sum

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_}' не найден.")
        raise

    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{input_}' содержит некорректный JSON.")
        raise

    except (ValueError, KeyError) as e:
        print(f"Ошибка: {e}")
        raise

print(task("input_.json"))
