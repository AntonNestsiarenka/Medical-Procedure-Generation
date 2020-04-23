import random
FILE_NAME = "list_name_illnesses.txt"

class illness:

    object_of_illnesses = []

    def __init__(self, name):
        self.name = name
        self.symptoms = list()
        self.medicines_for_treatment = list()
        self.object_of_illnesses.append(self)

    @classmethod
    def init_group(cls, number):
        names = cls.get_all_posible_name()
        for i in range(number):
            cls(names.pop(random.randint(0, len(names) - 1)))

    def get_name(self):
        return self.name

    def set_symptoms(self, symptoms):
        self.symptoms.extend(symptoms)

    def get_symptoms(self):
        return self.symptoms

    def set_medicines_for_treatment(self, medicines):
        self.medicines_for_treatment = list()
        self.add_medicines_for_treatment(medicines)

    def add_medicines_for_treatment(self, medicines):
        self.medicines_for_treatment.append(medicines)

    def get_medicines_for_treatment(self):
        return self.medicines_for_treatment

    @classmethod
    def get_all_posible_name(cls):
        with open(FILE_NAME, "r") as all_posible_name_file:
            all_posible_name = all_posible_name_file.readlines()
            return "".join(all_posible_name).strip().split("\n")

    def delete_nested_lists(self):
        temp = self.medicines_for_treatment.copy()
        for i in self.medicines_for_treatment:
            for j in self.medicines_for_treatment:
                if set(i) & set(j) == set(j) and set(i) != set(j):
                    self.medicines_for_treatment.remove(j)
        if temp != self.medicines_for_treatment:
            self.delete_nested_lists()

    @classmethod
    def output_info_class(cls):
        number = 1
        for object in cls.object_of_illnesses:
            print('{:3}. Название болезни: {}\n     Симптомы: {}\n     Лечение: {}'.format(number, object.name, [i.name for i in object.symptoms], [[j.name for j in i] for i in object.medicines_for_treatment]))
            print()
            number += 1