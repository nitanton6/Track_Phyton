def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            small_letter = letter.lower()
            if small_letter in letter_count:
                letter_count[small_letter] += 1
            else:
                letter_count[small_letter] = 1
    return letter_count
# TODO  Напишите функцию count_letters


def calculate_frequency(letter_dict):
    total = sum(letter_dict.values())
    frequency_dict = {}
    for letter, count in letter_dict.items():
            frequency_dict[letter] = round(count / total, 2)
    return frequency_dict
# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
letter_count = count_letters(main_str)
frequency_count = calculate_frequency(letter_count)

for letter, count in frequency_count.items():
    print(f"{letter}: {count:.2f}")
# TODO Распечатайте в столбик букву и её частоту в тексте
