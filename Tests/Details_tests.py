import Details


details = Details.Details(Details.TypeOfCollision.In_chain)

#properties test
assert details.type_of_collision == Details.TypeOfCollision.In_chain

#setters test
details.type_of_collision = Details.TypeOfCollision.Frontal
assert details.type_of_collision == Details.TypeOfCollision.Frontal


