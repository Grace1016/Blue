###Expected allele frequency under Wright-Fisher model###
## Over one generation
N <- 50
fA <- 0.25
rbinom(1, 2*N, fA) / (2*N)
mean( rbinom(20, 2*N, fA) / (2*N) )
mean( rbinom(1e5, 2*N, fA) / (2*N) )

## Over many generations
N <- 50
# 100 generations
fA <- rep(NA, 100)
# at t=0
fA[1] <- 0.5
for (t in 1:99) {
  fA[t+1] <- rbinom(1, 2*N, fA[t]) / (2*N)
}
plot(x=1:100, y=fA, type="l", ylim=c(0,1))

N <- 50
for (j in 1:20) {
  fA <- rep(NA, 100)
  fA[1] <- 0.5
  for (t in 1:99)
    fA[t+1] <- rbinom(1, 2*N, fA[t]) / (2*N)
    if (j==1)
      plot(x=1:100, y=fA, xlab="generations", type="l", ylim=c(0,1), col=rainbow(20)[j]) else lines(x=1:100, y=fA, col=rainbow(20)[j])
}

## Effect of population size¶
# small population (blue)
N <- 10
for (j in 1:10) {
  fA <- rep(NA, 100); fA[1] <- 0.5
  for (t in 1:99) fA[t+1] <- rbinom(1, 2*N, fA[t]) / (2*N)
  if (j==1) plot(x=1:100, y=fA, type="l", ylim=c(0,1), col="blue") else lines(x=1:100, y=fA, col="blue")
}

# large population (red)
N <- 1000
for (j in 1:10) {
  fA <- rep(NA, 100); fA[1] <- 0.5
  for (t in 1:99) fA[t+1] <- rbinom(1, 2*N, fA[t]) / (2*N)
  lines(x=1:100, y=fA, col="red")
}