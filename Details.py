from enum import Enum


class TypeOfCollision(Enum):
    Frontal = 1
    From_the_rear = 2
    By_the_side = 3
    In_chain = 4
    Multiple_collisions = 5
    Other_collision = 6
    Without_collision = 7
    Unknown = 'NA'

    @staticmethod
    def make_directory():
        return {'1': TypeOfCollision.Frontal,
                '2': TypeOfCollision.From_the_rear,
                '3': TypeOfCollision.By_the_side,
                '4': TypeOfCollision.In_chain,
                '5': TypeOfCollision.Multiple_collisions,
                '6': TypeOfCollision.Other_collision,
                '7': TypeOfCollision.Without_collision,
                'NA': TypeOfCollision.Unknown
    }


class Details:
    def __init__(self, type_of_collision):
        self.type_of_collision = type_of_collision

    @property
    def type_of_collision(self):
        return self.__type_of_collision

    @type_of_collision.setter
    def type_of_collision(self, type_of_collision):
        self.__type_of_collision = type_of_collision

    def __str__(self):
        return "Details: " + str(self.type_of_collision.name)

    def __eq__(self, other):
        return self.type_of_collision == other.type_of_collision