import random
FILE_NAME = "list_name_symptoms.txt"

class symptoms:

    object_of_symptoms = []

    def __init__(self, name):
        self.name = name
        self.object_of_symptoms.append(self)

    @classmethod
    def init_group(cls, number):
        names = cls.get_all_posible_name()
        for i in range(number):
            cls(names.pop(random.randint(0, len(names) - 1)))

    def get_name(self):
        return self.name

    @classmethod
    def get_all_posible_name(cls):
        with open(FILE_NAME, "r") as all_posible_name_file:
            all_posible_name = all_posible_name_file.readlines()
            return "".join(all_posible_name).strip().split("\n")
