#!usr/bin/env Rscript

# script: Plot.R
# Author: Hongye Wang (hw2419@imperial.ac.uk)

library(tidyr)
library(reshape)

#doesn't print warnings when workflow is hongye on terminal
options(warn=-1)

# clear current workspace
rm(list=ls())

# read in data
DF <- read.csv("../data/start_val_data.csv")
classicalDF <- read.csv("../results/classical_model.csv")
gompertzDF <- read.csv("../results/gompertz_model.csv")
baranyiDF <- read.csv("../results/baranyi_model.csv")
buchananDF <- read.csv("../results/buchanan_model.csv")
cubicDF <- read.csv("../results/cubic_model.csv")

modelselectDF <- data.frame("ID" = cubicDF$ID,
                            "cub_AIC" = cubicDF$aic,
                            "cla_AIC" = classicalDF$aic,
                            "gom_AIC" = gompertzDF$aic,
                            "bar_AIC" = baranyiDF$aic,
                            "bucha_AIC"=buchananDF$aic)

# add delta AIC colomns
for (i in 1:dim(modelselectDF)[1]) {
  modelselectDF$cla_deltaAIC[i] <- modelselectDF$cla_AIC[i] - min(modelselectDF[i,2:5],na.rm=TRUE)
  modelselectDF$gom_deltaAIC[i] <- modelselectDF$gom_AIC[i] - min(modelselectDF[i,2:5],na.rm=TRUE)
  modelselectDF$bar_deltaAIC[i] <- modelselectDF$bar_AIC[i] - min(modelselectDF[i,2:5],na.rm=TRUE)
  modelselectDF$bucha_deltaAIC[i] <- modelselectDF$bucha_AIC[i] - min(modelselectDF[i,2:5],na.rm=TRUE)
  modelselectDF$cub_deltaAIC[i] <- modelselectDF$cub_AIC[i] - min(modelselectDF[i,2:5],na.rm=TRUE)
}

# get the sample size of each curve and add to dataframe 
SampleSize <- as.numeric(unlist(aggregate(cbind(count = ID) ~ ID, data = DF, FUN = function(x){NROW(x)})['count']))
modelselectDF$SampleSize <- SampleSize

# calculate the AICc cause the Sample size of each curve is very small, so AICc might be better than AIC
modelselectDF$cla_AICc <- modelselectDF$cla_AIC + 2*3*(3+1)/(modelselectDF$SampleSize-3-1)
modelselectDF$gom_AICc <- modelselectDF$gom_AIC + 2*3*(3+1)/(modelselectDF$SampleSize-3-1)
modelselectDF$bar_AICc <- modelselectDF$bar_AIC + 2*4*(4+1)/(modelselectDF$SampleSize-4-1)
modelselectDF$bucha_AICc <- modelselectDF$bucha_AIC + 2*5*(5+1)/(modelselectDF$SampleSize-5-1)
modelselectDF$cub_AICc <- modelselectDF$cub_AIC + 2*4*(4+1)/(modelselectDF$SampleSize-4-1)

# if sample size < 8, then 2p(p+1)/(n-p-1) <= 0, the AICc lose its meaning 
modelselectDF$cla_AICc[modelselectDF$SampleSize < 8] <- NA
modelselectDF$gom_AICc[modelselectDF$SampleSize < 8] <- NA
modelselectDF$bar_AICc[modelselectDF$SampleSize < 8] <- NA
modelselectDF$bucha_AICc[modelselectDF$SampleSize < 8] <- NA
modelselectDF$cub_AICc[modelselectDF$SampleSize < 8] <- NA

#add delta AICc columns
for (i in 1:dim(modelselectDF)[1]) {
  modelselectDF$cla_deltaAICc[i] <- modelselectDF$cla_AICc[i] - min(modelselectDF[i,11:14],na.rm=TRUE)
  modelselectDF$gom_deltaAICc[i] <- modelselectDF$gom_AICc[i] - min(modelselectDF[i,11:14],na.rm=TRUE)
  modelselectDF$bar_deltaAICc[i] <- modelselectDF$bar_AICc[i] - min(modelselectDF[i,11:14],na.rm=TRUE)
  modelselectDF$bucha_deltaAICc[i] <- modelselectDF$bucha_AICc[i] - min(modelselectDF[i,11:14],na.rm=TRUE)
  modelselectDF$cub_deltaAICc[i] <- modelselectDF$cub_AICc[i] - min(modelselectDF[i,11:14],na.rm=TRUE)
}

# Calcualate the Akaike Weight(AIC) for each model
modelselectDF$cla_AIC_Wt <- exp((-0.5)*modelselectDF$cla_deltaAIC)/(exp((-0.5)*modelselectDF$cla_deltaAIC)+exp((-0.5)*modelselectDF$gom_deltaAIC)+exp((-0.5)*modelselectDF$bar_deltaAIC)+exp((-0.5)*modelselectDF$bucha_deltaAIC)+exp((-0.5)*modelselectDF$cub_deltaAIC))
modelselectDF$gom_AIC_Wt <- exp((-0.5)*modelselectDF$gom_deltaAIC)/(exp((-0.5)*modelselectDF$cla_deltaAIC)+exp((-0.5)*modelselectDF$gom_deltaAIC)+exp((-0.5)*modelselectDF$bar_deltaAIC)+exp((-0.5)*modelselectDF$bucha_deltaAIC)+exp((-0.5)*modelselectDF$cub_deltaAIC))
modelselectDF$bar_AIC_Wt <- exp((-0.5)*modelselectDF$bar_deltaAIC)/(exp((-0.5)*modelselectDF$cla_deltaAIC)+exp((-0.5)*modelselectDF$gom_deltaAIC)+exp((-0.5)*modelselectDF$bar_deltaAIC)+exp((-0.5)*modelselectDF$bucha_deltaAIC)+exp((-0.5)*modelselectDF$cub_deltaAIC))
modelselectDF$bucha_AIC_Wt <- exp((-0.5)*modelselectDF$bucha_deltaAIC)/(exp((-0.5)*modelselectDF$cla_deltaAIC)+exp((-0.5)*modelselectDF$gom_deltaAIC)+exp((-0.5)*modelselectDF$bar_deltaAIC)+exp((-0.5)*modelselectDF$bucha_deltaAIC)+exp((-0.5)*modelselectDF$cub_deltaAIC))
modelselectDF$cub_AIC_Wt <- exp((-0.5)*modelselectDF$cub_deltaAIC)/(exp((-0.5)*modelselectDF$cla_deltaAIC)+exp((-0.5)*modelselectDF$gom_deltaAIC)+exp((-0.5)*modelselectDF$bar_deltaAIC)+exp((-0.5)*modelselectDF$bucha_deltaAIC)+exp((-0.5)*modelselectDF$cub_deltaAIC))

#Calculate the Akaike Weight(AICc) for each model
modelselectDF$cla_AICc_Wt <- exp((-0.5)*modelselectDF$cla_deltaAICc)/(exp((-0.5)*modelselectDF$cla_deltaAICc)+exp((-0.5)*modelselectDF$gom_deltaAICc)+exp((-0.5)*modelselectDF$bar_deltaAICc)+exp((-0.5)*modelselectDF$bucha_deltaAICc)+exp((-0.5)*modelselectDF$cub_deltaAICc))
modelselectDF$gom_AICc_Wt <- exp((-0.5)*modelselectDF$gom_deltaAICc)/(exp((-0.5)*modelselectDF$cla_deltaAICc)+exp((-0.5)*modelselectDF$gom_deltaAICc)+exp((-0.5)*modelselectDF$bar_deltaAICc)+exp((-0.5)*modelselectDF$bucha_deltaAICc)+exp((-0.5)*modelselectDF$cub_deltaAICc))
modelselectDF$bar_AICc_Wt <- exp((-0.5)*modelselectDF$bar_deltaAICc)/(exp((-0.5)*modelselectDF$cla_deltaAICc)+exp((-0.5)*modelselectDF$gom_deltaAICc)+exp((-0.5)*modelselectDF$bar_deltaAICc)+exp((-0.5)*modelselectDF$bucha_deltaAICc)+exp((-0.5)*modelselectDF$cub_deltaAICc))
modelselectDF$bucha_AICc_Wt <- exp((-0.5)*modelselectDF$bucha_deltaAICc)/(exp((-0.5)*modelselectDF$cla_deltaAICc)+exp((-0.5)*modelselectDF$gom_deltaAICc)+exp((-0.5)*modelselectDF$bar_deltaAICc)+exp((-0.5)*modelselectDF$bucha_deltaAICc)+exp((-0.5)*modelselectDF$cub_deltaAICc))
modelselectDF$cub_AICc_Wt <- exp((-0.5)*modelselectDF$cub_deltaAICc)/(exp((-0.5)*modelselectDF$cla_deltaAICc)+exp((-0.5)*modelselectDF$gom_deltaAICc)+exp((-0.5)*modelselectDF$bar_deltaAICc)+exp((-0.5)*modelselectDF$bucha_deltaAICc)+exp((-0.5)*modelselectDF$cub_deltaAICc))

##create a table to see which is the best model based on delta AIC and delta AICc
cla_col <- c(sum(modelselectDF$cla_deltaAIC <= 2, na.rm = TRUE),
               sum(modelselectDF$cla_deltaAICc <= 2, na.rm = TRUE))
gom_col <-  c(sum(modelselectDF$gom_deltaAIC <= 2, na.rm = TRUE),
               sum(modelselectDF$gom_deltaAICc <= 2, na.rm = TRUE))
bar_col <- c(sum(modelselectDF$bar_deltaAIC <= 2,na.rm = TRUE),
             sum(modelselectDF$bar_deltaAICc <= 2, na.rm = TRUE))
bucha_col <- c(sum(modelselectDF$bucha_deltaAIC <= 2, na.rm = TRUE),
             sum(modelselectDF$bucha_deltaAICc <= 2, na.rm = TRUE))
cub_col <- c(sum(modelselectDF$cub_deltaAIC <= 2, na.rm = TRUE),
             sum(modelselectDF$cub_deltaAICc <= 2, na.rm = TRUE))

table1 <- rbind(cla_col,gom_col,bar_col,bucha_col,cub_col)
rownames(table1) <- c("Classical", "Gompertz", "Baranyi",
                      "Buchanan","Cubic")
colnames(table1) <- c('deltaAIC <= 2','delta_AICc <= 2')
print(table1)

#create a table to see each model's mean statistic values
cla_col2 <- c(mean(classicalDF$Rsqrd, na.rm = TRUE),
                mean(modelselectDF$cla_AIC, na.rm = TRUE),
                mean(modelselectDF$cla_AICc, na.rm = TRUE),
                mean(modelselectDF$cla_AIC_Wt, na.rm = TRUE),
                mean(modelselectDF$cla_AICc_Wt, na.rm = TRUE))
gom_col2 <- c(mean(gompertzDF$Rsqrd, na.rm = TRUE),
               mean(modelselectDF$gom_AIC, na.rm = TRUE),
               mean(modelselectDF$gom_AICc, na.rm = TRUE),
               mean(modelselectDF$gom_AIC_Wt, na.rm = TRUE),
               mean(modelselectDF$gom_AICc_Wt, na.rm = TRUE))
bar_col2 <- c(mean(baranyiDF$Rsqrd, na.rm = TRUE),
              mean(modelselectDF$bar_AIC, na.rm = TRUE),
              mean(modelselectDF$bar_AICc, na.rm = TRUE),
              mean(modelselectDF$bar_AIC_Wt, na.rm = TRUE),
              mean(modelselectDF$bar_AICc_Wt, na.rm = TRUE))
bucha_col2 <- c(mean(buchananDF$Rsqrd, na.rm = TRUE),
              mean(modelselectDF$bucha_AIC, na.rm = TRUE),
              mean(modelselectDF$bucha_AICc, na.rm = TRUE),
              mean(modelselectDF$bucha_AIC_Wt, na.rm = TRUE),
              mean(modelselectDF$bucha_AICc_Wt, na.rm = TRUE))
cub_col2 <- c(mean(cubicDF$Rsqrd, na.rm = TRUE),
                mean(modelselectDF$cub_AIC, na.rm = TRUE),
                mean(modelselectDF$cub_AICc, na.rm = TRUE),
                mean(modelselectDF$cub_AIC_Wt, na.rm = TRUE),
                mean(modelselectDF$cub_AICc_Wt, na.rm = TRUE))


table2 <- cbind(cla_col2,gom_col2,bar_col2,bucha_col2,cub_col2)
colnames(table2) <- c("Classical", "Gompertz", "Baranyi",
                      "Buchanan", "Cubic")
rownames(table2) <- c('Mean Rsquared','Mean AIC','Mean AICc','Mean Akaike Weight(AIC)','Mean Akaike Weight(AICc)')
print(table2)

#plot the box imagine to compare AICc value in each model
boxdata1 <- gather(modelselectDF, Model, AICc, cla_AICc:gom_AICc:bar_AICc:bucha_AICc:cub_AICc)
boxdata2 <- gather(modelselectDF, Model, Weight_AICc, cla_AICc_Wt:gom_AICc_Wt: bar_AICc_Wt:bucha_AICc_Wt:cub_AICc_Wt)
p2 <- ggplot(boxdata1,aes(x = Model, y = AICc )) + geom_boxplot(fill = "#4271AE", colour = "#1F3552", alpha = 0.7) + ggtitle("Boxplot of AICc by model") + 
  scale_y_continuous(name = "AICc value in all fitted subset", breaks = seq(-280,120,50),limits = c(-280,120))
p3 <- ggplot(boxdata2,aes(x = Model, y = Weight_AICc )) + geom_boxplot(fill = "red", colour = "#1F3552", alpha = 0.7) + ggtitle("Boxplot of Weight(AICc) by model") + 
  scale_y_continuous(name = "Weight(AICc) value in all fitted subset", breaks = seq(0,1.8,0.1),limits = c(0,1.8))

write.csv(modelselectDF, file="../results/analysis_dt.csv", sep = ",", col.names = TRUE, row.names = FALSE)

