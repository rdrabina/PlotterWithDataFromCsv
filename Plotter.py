import matplotlib.pyplot as plot


class Plotter:
    @staticmethod
    def make_chart_localisation(found_accidents):
        plot.figure(figsize=(10,10))
        localisations = {}

        for found_accident in found_accidents:
            if found_accident.area.localisation.name in localisations:
                localisations[found_accident.area.localisation.name] += 1
            else:
                localisations[found_accident.area.localisation.name] = 1

        localisations_list = localisations.keys()
        localisations_value = localisations.values()

        xticks = []
        yticks = []

        for i in range(len(localisations_list)):
            xticks.append(i)
        for i in range(0, max(localisations_value)+5, 5):
            yticks.append(i)

        plot.title("Accidents grouped by localisation")
        plot.xlabel("Localisation")
        plot.ylabel("How many occured?")
        plot.xticks(xticks, localisations_list, )
        plot.yticks(yticks)
        plot.bar(xticks, localisations_value, 0.7)
        plot.show()

    @staticmethod
    def make_chart_intersection(found_accidents):
        plot.figure(figsize=(10, 10))
        intersections = {}

        for found_accident in found_accidents:
            if found_accident.area.intersection.name in intersections:
                intersections[found_accident.area.intersection.name] += 1
            else:
                intersections[found_accident.area.intersection.name] = 1

        intersections_list = intersections.keys()
        intersections_value = intersections.values()

        xticks = []
        yticks = []

        for i in range(len(intersections_list)):
            xticks.append(i)
        for i in range(0, max(intersections_value) + 5, 5):
            yticks.append(i)

        plot.title("Accidents grouped by intersection")
        plot.xlabel("Intersection")
        plot.ylabel("How many occured?")
        plot.xticks(xticks, intersections_list, rotation=15)
        plot.yticks(yticks)
        plot.bar(xticks, intersections_value, 0.7)
        plot.show()

    @staticmethod
    def make_chart_type_of_collision(found_accidents):
        plot.figure(figsize=(10, 10))
        type_of_collisions = {}

        for found_accident in found_accidents:
            if found_accident.details.type_of_collision.name in type_of_collisions:
                type_of_collisions[found_accident.details.type_of_collision.name] += 1
            else:
                type_of_collisions[found_accident.details.type_of_collision.name] = 1

        type_of_collision_list = type_of_collisions.keys()
        type_of_collision_value = type_of_collisions.values()

        xticks = []
        yticks = []

        for i in range(len(type_of_collision_list)):
            xticks.append(i)
        for i in range(0, max(type_of_collision_value) + 5, 5):
            yticks.append(i)

        plot.title("Accidents grouped by type of collision")
        plot.xlabel("Type of collision")
        plot.ylabel("How many occured?")
        plot.xticks(xticks, type_of_collision_list, rotation=15)
        plot.yticks(yticks)
        plot.bar(xticks, type_of_collision_value, 0.7)
        plot.show()

    @staticmethod
    def make_chart_by_hours(found_accidents, date):
        plot.figure(figsize=(7, 6))
        parts = 24 * [0]
        hours = []
        for i in range(24):
            hours.append(str(i))

        for found_accident in found_accidents:
            parts[found_accident.date.hour-1] += 1

        plot.title("Accidents grouped by hours from " + str(date.day) + '.' + str(date.month)
                   + '.' + str(date.year)+"\n Chosen hour: "+ str(date.hour))
        plot.pie(parts, labels=hours, autopct='%1.2f%%', pctdistance=0.8)
        plot.legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=6)
        plot.show()
