import illness
import medicines
import symptoms
import random
import itertools
SEED_MODULE = random.randint(1, 20000) + random.random()
random.seed(SEED_MODULE)

def get_all_combinations_symptoms():
    # Creating all possible non-recurring combinations of symptoms
    # Создание всех возможных неповторяющихся комбинаций симптомов
    combinations_symptoms = list()
    for len_combination in range(1, len(symptoms.symptoms.object_of_symptoms) + 1):
        for combination in itertools.combinations(symptoms.symptoms.object_of_symptoms, len_combination):
            combinations_symptoms.append(list(combination))
    return combinations_symptoms

def get_all_correct_medicines_combinations():
    # The function creates all the correct medication combinations without considering the combination with an incompatible medication
    # Функция создает все корректные комбинации медикаментов без учета комбинации с несовместимым медикаментом
    combinations_medicines = list()
    for len_combination in range(1, len(medicines.medicines.object_of_medicines) + 1):
        for combination in itertools.combinations(medicines.medicines.object_of_medicines, len_combination):
            combination = list(combination)
            if medicines.medicines.is_compatibilities_medicines(combination):
                combinations_medicines.append(combination)
    return combinations_medicines

def add_incompatible_medication(the_number_of_medicines_that_have_incompatibility):
    # Add incompatible medications to n-random medicines
    # Добавление n-случайным медикаментам несовместимых медикаментов
    # the_number_of_medicines_that_have_incompatibility - сколько хотим медикаментов с несовместимостями (how many medications with incompatibilities do we want)
    for i in range(the_number_of_medicines_that_have_incompatibility):
        # Random is selected from the list of medications instances
        # Из списка экземпляров медикаментов выбирается случайный
        object_of_influence = random.choice(medicines.medicines.object_of_medicines)
        # Search for a list of all compatible medications with the selected instance and randomly select from an incompatible list
        # Поиск списка всех совместимых медикаментов с выбранным экземпляром и случайный выбор из списка несовместимого
        added_medicine_in_incompatibilities = random.choice(object_of_influence.get_compatibilities())
        # Adding an incompatible medication to the medication instance and back
        # Добавление несовместимого медикамента к экземпляру медикамента и в обратную сторону
        object_of_influence.add_incompatibilities(added_medicine_in_incompatibilities)

def add_random_combinations_medicines_to_illness(n):
    # Adding n-random medication combinations to treat each disease
    # Добавление n-случайных комбинаций медикаментов для лечения каждой болезни
    for illness_obj in illness.illness.object_of_illnesses:
        combinations_medicines = get_all_correct_medicines_combinations()
        for x in range(n):
            illness_obj.add_medicines_for_treatment(combinations_medicines.pop(random.randint(0, len(combinations_medicines) - 1)))
        # Removal of incorrect treatment of diseases
        # Удаление некорректных лечений болезней
        illness_obj.delete_nested_lists()

def is_correct_count_combinations_to_add_all_illness(combinations):
    # General function for verifying the correct addition of symptoms or medication to all diseases
    # Общая функция для проверки корректного добавления симптомов или медикаментов всем болезням
    return len(combinations) >= len(illness.illness.object_of_illnesses)


# Instantiation of n-symptoms
# Создание экземпляров n-симптомов
symptoms.symptoms.init_group(6)

# Creating all possible symptom combinations from the created symptom instances
# Создание всех возможных комбинаций симптомов из созданных экземпляров симптомов
combinations_symptoms = get_all_combinations_symptoms()

# Creating Instances of n-Medicines
# Создание экземпляров n-медикаментов
medicines.medicines.init_group(4)

# Addition of incompatibilities to n-random medicines
# Добавление к n-случайным медикаментам несовместимостей
add_incompatible_medication(2)

# Creating all the right combinations of medicines
# Cоздание всех корректных комбинаций медикаментов
combinations_medicines = get_all_correct_medicines_combinations()

# Instantiation of n-diseases
# Создание экземпляров n-болезней
illness.illness.init_group(4)

if is_correct_count_combinations_to_add_all_illness(combinations_symptoms):
    # Adding a random combination of symptoms for each disease
    # Добавление случайной комбинации симптомов для каждой болезни
    for illness_obj in illness.illness.object_of_illnesses:
        illness_obj.set_symptoms(combinations_symptoms.pop(random.randint(0, len(combinations_symptoms) - 1)))
else:
    print("ALARM!!!")

if is_correct_count_combinations_to_add_all_illness(combinations_medicines):
    # Adding n-random medication combinations to treat each disease
    # Добавление n-случайных комбинаций медикаментов для лечения каждой болезни
    add_random_combinations_medicines_to_illness(4)
else:
    print("ALARM!!!")

# Display information about generated objects
# Вывод информации о сгенерированных объектах
medicines.medicines.output_info_class()
illness.illness.output_info_class()
