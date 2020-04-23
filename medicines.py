import random
FILE_NAME = "list_name_medicines.txt"

class medicines:

    object_of_medicines = []

    def __init__(self, name):
        self.name = name
        self.incompatibilities = list()
        self.object_of_medicines.append(self)

    @classmethod
    def init_group(cls, number):
        names = cls.get_all_posible_name()
        for i in range(number):
            cls(names.pop(random.randint(0, len(names) - 1)))

    def get_name(self):
        return self.name

    def set_incompatibilities(self, seted_incompatibilities):
        self.incompatibilities.clear()
        self.add_incompatibilities(self, seted_incompatibilities)

    def add_incompatibilities(self, added_incompatibilities):
        self.incompatibilities.append(added_incompatibilities)
        if not(isinstance(added_incompatibilities, list)):
            added_incompatibilities = [added_incompatibilities]
        for incompatibilitie in added_incompatibilities:
            incompatibilitie.incompatibilities.append(self)

    def get_incompatibilities(self):
        return self.incompatibilities

    def get_compatibilities(self):
        result = list()
        for medicine in self.object_of_medicines:
            if self.is_compatibilities_medicines(medicine) and self != medicine:
                result.append(medicine)
        return result

    @classmethod
    def is_compatibilities_medicines(cls, *args):
        for arg1 in args:
            for arg2 in args:
                if arg1 in arg2.get_incompatibilities():
                    return False
        return True

    def is_compatibilities_medicines(self, *args):
        for arg in args:
            if arg in self.get_incompatibilities():
                return False
        return True

    @classmethod
    def get_all_posible_name(cls):
        with open(FILE_NAME, "r") as all_posible_name_file:
            all_posible_name = all_posible_name_file.readlines()
            return "".join(all_posible_name).strip().split("\n")

    @classmethod
    def output_info_class(cls):
        number = 1
        for object in cls.object_of_medicines:
            print('{:3}. Название медикамента: {}\n     Название несовместимого медикамента: {}'.format(number, object.name, [subobject.name for subobject in object.incompatibilities]))
            print()
            number += 1