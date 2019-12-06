# load and examine and plot the data
load("../data/KeyWestAnnualMeanTemperature.RData")
plot(ats$Year,ats$Temp, xlab = "Year", ylab = "Annual mean Temperature")
lines(ats$Year,ats$Temp)

# calculate correlation between successive years
Temperatur_cor <- cor(ats$Temp[1:99],ats$Temp[2:100])

# plot the correlation graph
correlation_plot <- plot(ats$Temp[1:99],ats$Temp[2:100],ylab = "Next Year Temperature", xlab = "Current Year Temperature")

# calculate the random correlation between random two years
set.seed(1)#seet the seed to ensure the output same at every time
random_cor <- rep(NA,10000)
for (i in 1:10000) {
  random_tem <- sample(ats$Temp)
  random_cor[i] <- cor(random_tem[1:99],random_tem[2:100])
}

# calculate the p-value
p_value <- length(random_cor[random_cor>Temperatur_cor])/length(random_cor)
hist_cor <- hist(random_cor,probability = TRUE,xlab = "random correlation coefficients",ylab = "density")
print(p_value)

#store the patterns for report
pdf("../result/TAutoCorr_plot1.pdf")
correlation_plot <- plot(ats$Temp[1:99],ats$Temp[2:100],ylab = "Next Year Temperature", xlab = "Current Year Temperature")
dev.off()

pdf("../result/TAutoCorr_plot2.pdf")
hist_cor <- hist(random_cor,probability = TRUE,xlab = "random correlation coefficients",ylab = "density")
dev.off()
