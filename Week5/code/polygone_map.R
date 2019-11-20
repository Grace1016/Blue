### create a population density map for the British Isles ###
pop_dens <- data.frame(n_km2 = c(260, 67,151, 4500, 133), 
                       country = c('England','Scotland', 'Wales', 'London', 'Northern Ireland'))
print(pop_dens)

# Create coordinates  for each country 
# -  this is a list of sets of coordinates forming the edge of the polygon. 
# - note that they have to _close_ (have the same coordinate at either end)
scotland <- rbind(c(-5, 58.6), c(-3, 58.6), c(-4, 57.6), 
                  c(-1.5, 57.6), c(-2, 55.8), c(-3, 55), 
                  c(-5, 55), c(-6, 56), c(-5, 58.6))
england <- rbind(c(-2,55.8),c(0.5, 52.8), c(1.6, 52.8), 
                 c(0.7, 50.7), c(-5.7,50), c(-2.7, 51.5), 
                 c(-3, 53.4),c(-3, 55), c(-2,55.8))
wales <- rbind(c(-2.5, 51.3), c(-5.3,51.8), c(-4.5, 53.4),
               c(-2.8, 53.4),  c(-2.5, 51.3))
ireland <- rbind(c(-10,51.5), c(-10, 54.2), c(-7.5, 55.3),
                 c(-5.9, 55.3), c(-5.9, 52.2), c(-10,51.5))

# Convert these coordinates into feature geometries
# - these are simple coordinate sets with no projection information
scotland <- st_polygon(list(scotland))
england <- st_polygon(list(england))
wales <- st_polygon(list(wales))
ireland <- st_polygon(list(ireland))

# Combine geometries into a simple feature column
uk_eire <- st_sfc(wales, england, scotland, ireland, crs=4326)
plot(uk_eire, asp=1)
uk_eire_capitals <- data.frame(long= c(-0.1, -3.2, -3.2, -6.0, -6.25),
                               lat=c(51.5, 51.5, 55.8, 54.6, 53.30),
                               name=c('London', 'Cardiff', 'Edinburgh', 'Belfast', 'Dublin'))

uk_eire_capitals <- st_as_sf(uk_eire_capitals, coords=c('long','lat'), crs=4326)

#use the buffer operation to create a polygon for London
#which we define as anywhere within a quarter degree of St. Pauls Cathedral
st_pauls <- st_point(x=c(-0.098056, 51.513611))
london <- st_buffer(st_pauls, 0.25)
#remove London from the England polygon
england_no_london <- st_difference(england, london)
# Count the points and show the number of rings within the polygon features
lengths(scotland)
length(england_no_london)
#tidy up wales#
wales <- st_difference(wales, england)

# A rough polygon that includes Northern Ireland and surrounding sea.
# - not the alternative way of providing the coordinates
ni_area <- st_polygon(list(cbind(x=c(-8.1, -6, -5, -6, -8.1), y=c(54.4, 56, 55, 54, 54.4))))

northern_ireland <- st_intersection(ireland, ni_area)
eire <- st_difference(ireland, ni_area)

# Combine the final geometries
uk_eire <- st_sfc(wales, england_no_london, scotland, london, northern_ireland, eire, crs=4326)
plot(uk_eire,asp=1)
#make the UK into a single feature
uk_country <- st_union(uk_eire[-6])
# compare six Polygon features with one Multipolygon feature
print(uk_eire)
print(uk_country)
par(mfrow=c(1, 2), mar=c(3,3,1,1))
#plot them
plot(uk_eire, asp=1, col=rainbow(6))
plot(st_geometry(uk_eire_capitals), add=TRUE)
plot(uk_country, asp=1, col='lightblue')

uk_eire <- st_sf(name=c('Wales', 'England','Scotland', 'London', 
                        'Northern Ireland', 'Eire'),
                 geometry=uk_eire)

plot(uk_eire, asp=1)
uk_eire$capital <- c('Cardiff','London','Edinburgh', NA, 'Belfast','Dublin')
uk_eire <- merge(uk_eire, pop_dens, by.x='name', by.y='country', all.x=TRUE)
print(uk_eire)
#spatial attributes
uk_eire_centroids <- st_centroid(uk_eire)
st_coordinates(uk_eire_centroids)
uk_eire$area <- st_area(uk_eire)
# The length of a polygon is the perimeter length 
#- note that this includes the length of internal holes.
uk_eire$length <- st_length(uk_eire)
# Look at the result
print(uk_eire)
# You can change units in a neat way
uk_eire$area <- set_units(uk_eire$area, 'km^2')
uk_eire$length <- set_units(uk_eire$length, 'km')
uk_eire$length <- as.numeric(uk_eire$length)
print(uk_eire)

#show our map of population density
plot(uk_eire['n_km2'], asp=1)

# British National Grid (EPSG:27700)
uk_eire_BNG <- st_transform(uk_eire, 27700)
# The bounding box of the data shows the change in units
st_bbox(uk_eire)
##  xmin  ymin  xmax  ymax 
## -10.0  50.0   1.6  58.6

st_bbox(uk_eire_BNG)
##       xmin       ymin       xmax       ymax 
## -154811.97   17655.72  642773.71  971900.65

# UTM50N (EPSG:32650)
uk_eire_UTM50N <- st_transform(uk_eire, 32650)
# Plot the results
par(mfrow=c(1, 3), mar=c(3,3,1,1))
plot(st_geometry(uk_eire), asp=1, axes=TRUE, main='WGS 84')
plot(st_geometry(uk_eire_BNG), axes=TRUE, main='OSGB 1936 / BNG')
plot(st_geometry(uk_eire_UTM50N), axes=TRUE, main='UTM 50N')

# Set up some points separated by 1 degree latitude and longitude from St. Pauls
st_pauls <- st_sfc(st_pauls, crs=4326)
one_deg_west_pt <- st_sfc(st_pauls - c(1, 0), crs=4326) # near Goring
one_deg_north_pt <-  st_sfc(st_pauls + c(0, 1), crs=4326) # near Peterborough
# Calculate the distance between St Pauls and each point
st_distance(st_pauls, one_deg_west_pt)
st_distance(st_pauls, one_deg_north_pt)
st_distance(st_transform(st_pauls, 27700), st_transform(one_deg_west_pt, 27700))
