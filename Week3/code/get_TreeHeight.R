# This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 
#
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

TreeHeight <- function(degrees, distance){
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  
  return (height)
}

# import data and takes the file name from command line 
args <- commandArgs()
print(args)
mydata <- read.csv(args[6],header = TRUE)

#set arguments and calculate the height of trees
degrees <- mydata[,3]
distance <- mydata[,2]
Tree.Height.m <-TreeHeight(degrees,distance)

Result <- data.frame(mydata,Tree.Height.m) # combine treeheight with other datas of trees
output <- head(Result,2) # cat first 2 datas in result

# output as request
FileName <- tools::file_path_sans_ext(basename(args[6]))
write.csv(output, paste("../result/",FileName,"_treeheight.csv"), row.names = FALSE)



