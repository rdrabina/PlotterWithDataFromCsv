import Area


area = Area.Area(Area.Localisation.Out_of_agglomeration,Area.Intersection.Intersection_in_X)


#properties test
assert area.localisation == Area.Localisation.Out_of_agglomeration
assert area.intersection == Area.Intersection.Intersection_in_X

#setters test
area.localisation = Area.Localisation.In_built_up_areas
area.intersection = Area.Intersection.Out_of_intersection

assert area.localisation == Area.Localisation.In_built_up_areas
assert area.intersection == Area.Intersection.Out_of_intersection
