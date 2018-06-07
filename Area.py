from enum import Enum


class Localisation(Enum):
    Out_of_agglomeration = 1
    In_built_up_areas = 2

    @staticmethod
    def make_dictionary():
        return {'1': Localisation.Out_of_agglomeration,
                '2': Localisation.In_built_up_areas
        }


class Intersection(Enum):
    Out_of_intersection = 1
    Intersection_in_X = 2
    Intersection_in_T = 3
    Intersection_in_Y = 4
    More_than_4_branches = 5
    Giratory = 6
    Place = 7
    Level_crossing = 8
    Other = 9
    Unknown = 0

    @staticmethod
    def make_dictionary():
        return {'0': Intersection.Unknown,
                '1': Intersection.Out_of_intersection,
                '2': Intersection.Intersection_in_X,
                '3': Intersection.Intersection_in_T,
                '4': Intersection.Intersection_in_Y,
                '5': Intersection.More_than_4_branches,
                '6': Intersection.Giratory,
                '7': Intersection.Place,
                '8': Intersection.Level_crossing,
                '9': Intersection.Other
        }


class Area:
    def __init__(self,localisation, intersection):
        self.localisation = localisation
        self.intersection = intersection

    @property
    def localisation(self):
        return self.__localisation

    @property
    def intersection(self):
        return self.__intersection

    @localisation.setter
    def localisation(self, localisation):
        self.__localisation = localisation

    @intersection.setter
    def intersection(self, intersection):
        self.__intersection = intersection

    def __str__(self):
        return "Place: " + str(self.localisation.name) + ', ' + str(self.intersection.name)
