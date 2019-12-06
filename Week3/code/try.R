### showing the example of how 'try' doing ###

doit <- function(x){
  temp_x <- sample(x, replace = TRUE)
  if(length(unique(temp_x)) > 30) {#only take mean if sample was sufficient
    print(paste("Mean of this sample was:", as.character(mean(temp_x))))
  } 
  else {
    stop("Couldn't calculate mean: too few unique values!")
  }
}

popn <- rnorm(50) #Generate your population

#use lapply
lapply(1:15, function(i) doit(popn))

result <- lapply(1:15, function(i) try(doit(popn), FALSE))
class(result)
result

# or using for loop
result <- vector("list", 15) #Preallocate/Initialize
for(i in 1:15) {
  result[[i]] <- try(doit(popn), FALSE)
}
