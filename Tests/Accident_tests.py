import Accident
import Area
import Date
import Details


object = Accident.Accident(Area.Area(Area.Localisation.In_built_up_areas, Area.Intersection.Out_of_intersection), Date.
                           Date(12, 30, 5, 11, 2018), Details.Details(Details.TypeOfCollision.Multiple_collisions))

#properties test
assert object.area.localisation == Area.Localisation.In_built_up_areas
assert object.area.intersection == Area.Intersection.Out_of_intersection
assert object.date == Date.Date(12, 30, 5, 11, 2017)
assert object.details == Details.Details(Details.TypeOfCollision.Multiple_collisions)

#setters test
object.area = Area.Area(Area.Localisation.Out_of_agglomeration, Area.Intersection.Out_of_intersection)
object.date = Date.Date(11, 50, 28, 2, 2017)
object.details = Details.Details(Details.TypeOfCollision.By_the_side)
assert object.area.localisation == Area.Localisation.Out_of_agglomeration
assert object.date == Date.Date(11, 50, 28, 2, 2017)
assert object.details == Details.Details(Details.TypeOfCollision.By_the_side)
