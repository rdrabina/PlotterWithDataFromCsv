class Date:
    def __init__(self, hour, minute, day, month, year):
        self.hour = hour
        self.minute = minute
        self.year = year
        self.month = month
        self.day = day

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if not 0 <= hour < 24:
            raise ValueError
        else:
            self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year


    @minute.setter
    def minute(self,minute):
        if not 0 <= minute < 60:
            raise ValueError
        else:
            self.__minute = minute

    @day.setter
    def day(self,day):
        month = self.month
        year = self.year
        global days
        if month in [1, 3, 5, 7, 8, 10, 12]:
            days = 31
        elif month in [4, 6, 9, 11]:
            days = 30
        else:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        days = 29
                    else:
                        days = 28
                else:
                    days = 29
            else:
                days = 28
        if not 0 < day <= days:
            raise ValueError
        else:
            self.__day = day

    @month.setter
    def month(self,month):
        if not 0 < month < 13:
            raise ValueError
        else:
            self.__month = month

    @year.setter
    def year(self,year):
        self.__year = year

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __str__(self):
        if self.hour < 10:
            hour_string = "0"+str(self.hour)
        else:
            hour_string = str(self.hour)
        if self.minute < 10:
            minute_string = "0"+str(self.minute)
        else:
            minute_string = str(self.minute)
        if self.day < 10:
            day_string = "0" + str(self.day)
        else:
            day_string = str(self.day)
        if self.month < 10:
            month_string = "0" + str(self.month)
        else:
            month_string = str(self.month)
        return "Date: "+ hour_string +":"+minute_string+" "+day_string+"."+month_string+"."+str(self.year)