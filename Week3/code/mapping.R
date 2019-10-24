### create a world map and superimposes the location points ###
require(maps)
require(ggplot2)
load("../data/GPDDFiltered.RData")
attach(gpdd)
# map the world with points
mp <- NULL
mapWorld <- borders("world",colour = "gray50",fill = "gray50")
mp <- ggplot() + mapWorld

# layer the species on the world
mp <- mp + geom_point(aes(x=gpdd$long,y=gpdd$lat),colour="yellow",size=3)
mp


# most of the species are located at latitude 50 degrees north of the world.
# I think the biase of this database is the distribution of the species is limited.
# For instance, When analysing the migration of global species, this data may not be generalizable 