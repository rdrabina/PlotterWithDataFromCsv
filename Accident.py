class Accident:
    def __init__(self, area, date, details):
        self.area = area
        self.date = date
        self.details = details

    @property
    def area(self):
        return self.__area

    @property
    def date(self):
        return self.__date

    @property
    def details(self):
        return self.__details

    @area.setter
    def area(self,area):
        self.__area = area

    @date.setter
    def date(self,date):
        self.__date = date

    @details.setter
    def details(self,details):
        self.__details = details

    def __str__(self):
        return str(self.date) + "\n" + str(self.area)+ "\n" + str(self.details) + "\n "