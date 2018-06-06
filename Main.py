import Date
import Area
import Details
import Accident
import Plotter
import csv


accidents = []


def read_hour(time):
    if 2 < len(time) < 5:
        return int(int(time) / 100)
    else:
        return 0


def read_minute(time):
    if 2 < len(time) < 5:
        return int(int(time) % 100)
    else:
        return 0


def parser():
    date = input("Choose data (hh:mm dd.mm.yyyy): ")
    hour = date[:2]

    if hour[0] == '0':
        hour = hour[1]
    minute = date[3:5]
    if minute[0] == '0':
        minute = minute[1]
    day = date[6:8]
    if day[0] == '0':
        day = day[1]
    month = date[9:11]
    if month[0] == '0':
        month = month[1]
    year = date[12:16]

    try:
        if not date[2] == ':':
            print("':' must occur as 3 char of input")
            exit()
        if not date [5] == ' ':
            print("' ' must occur as 6 char of input")
            exit()
        if not date[8] == '.':
            print("'.' must occur as 9 char of input")
            exit()
        if not date[11] == '.':
            print("'.' must occur as 12 char of input")
            exit()
        if not len(year) == 4:
            print("Invalid year")
    except IndexError:
        print("Index out of range")
        exit()

    if not all(hour.isdigit() for i in hour):
        print("Invalid hour")
        exit()
    if not all(minute.isdigit() for i in minute):
        print("Invalid minute")
        exit()
    if not all(day.isdigit() for i in day):
        print("Invalid day")
        exit()
    if not all(month.isdigit() for i in month):
        print("Invalid month")
        exit()

    try:
        date_object = Date.Date(int(hour), int(minute), int(day), int(month), int(year))
    except ValueError:
        print("Invalid entered date. Try again")
        exit()
    return date_object


def read_accidents_from_file(date_object):
    localisations = Area.Localisation.make_dictionary()
    intersections = Area.Intersection.make_directory()
    type_of_collisions = Details.TypeOfCollision.make_directory()

    try:
        with open('Accidents.csv', 'r', encoding="ISO-8859-1") as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                date = Date.Date(read_hour(row[4]), read_minute(row[4]), int(row[3]), int(row[2]), 2000+int(row[1]))
                if date_object == date:
                    area = Area.Area(localisations[row[6]], intersections[row[7]])
                    details = Details.Details(type_of_collisions[row[9]])
                    accident = Accident.Accident(area,date,details)
                    accidents.append(accident)
    except FileNotFoundError:
        print("Cannot open a file")


def print_opportunities():
    print("Opportunities to print bar chart group by:")
    opportunities = ["Localisation", "Intersection", "Type of collision", "Chart by hours"]

    n = 1
    for i in opportunities:
        print(str(n) + ". " + str(i))
        n += 1

    choice = input()
    try:
        if not 0 < int(choice) < 5:
            print("Invalid choice")
    except ValueError:
        print("Invalid choice. You have to enter a number")
        exit()
    return int(choice)


def print_accidents():
    for i in accidents:
        print(i)

if __name__ == '__main__':
    chosen_number = print_opportunities()
    date_object = parser()

    if not 2004 < date_object.year < 2017:
        print("There is no data from chosen year.")
        exit()

    print("\n\nLoading data. This could take a while\n\n")
    read_accidents_from_file(date_object)

    if chosen_number == 1:
        print_accidents()
        Plotter.Plotter.make_chart_localisation(accidents)
    if chosen_number == 2:
        print_accidents()
        Plotter.Plotter.make_chart_intersection(accidents)
    if chosen_number == 3:
        print_accidents()
        Plotter.Plotter.make_chart_type_of_collision(accidents)
    if chosen_number == 4:
        print_accidents()
        Plotter.Plotter.make_chart_by_hours(accidents, date_object)
