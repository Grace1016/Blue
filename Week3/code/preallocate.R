### two examples to show the advantage of pre-allocation ###
### without pre-allocation ###
time <- as.numeric(proc.time())[1]
a <- NA
for (i in 1:10) {
  a <- c(a, i)
  print(a)
  print(object.size(a))
}
time2 <- as.numeric(proc.time())[1]
using_time <- time2-time
print(paste("Without Pre-allocation, it takes:",using_time))

### Using pre-allocation ###
a <- rep(NA, 10)
pre_allocation <- function(a){
for (i in 1:10) {
  a[i] <- i
  print(a)
  print(object.size(a))
 }
}
print("Using pre-allocation,it takes")
print(system.time(pre_allocation(a)))
