# load and examine and plot the data
load("../data/KeyWestAnnualMeanTemperature.RData")
plot(ats)

# calculate correlation between successive years
Temperatur_cor <- cor(ats$Temp[1:99],ats$Temp[2:100])

# calculate the random correlation
random_cor <- rep(NA,10000)
for (i in 1:10000) {
  random_tem <- sample(ats$Temp)
  random_cor[i] <- cor(random_tem[1:99],random_tem[2:100])
}

# calculate the p-value
p_value <- length(random_cor[random_cor>Temperatur_cor])/length(random_cor)
hist(random_cor,probability = TRUE,xlab = "random correlation coefficients",ylab = "density")
print(p_value)
