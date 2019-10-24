#CREATE A GRAPHICS AS EXAMPLE FIGURE AND WRITE REGRESSION RESULTS
rm(list = ls())
# extract data
MyDF <-read.csv("../data/EcolArchives-E089-51-D1.csv")

library(ggplot2)
library(dplyr)

# create the figure
p <- ggplot(MyDF,aes(x=Prey.mass,y=Predator.mass,colour=Predator.lifestage))+geom_point(shape=3)
p <- p+facet_grid(Type.of.feeding.interaction~.)+geom_smooth(method = lm,fullrange=TRUE)
p <- p+scale_x_continuous(trans = "log10","Prey Mass in grams")+scale_y_continuous(trans = "log10","Predator Mass in grams")
p <- p+theme_bw()+theme(legend.position = "bottom")+coord_fixed(ratio = 0.3)+guides(color=guide_legend(nrow = 1))

# saving the graphic
pdf("../result/PP_Regress.pdf")
print(p)
dev.off()

# define a function to calculate slope,intercept,Rsquare,F-statistic value and p-value
fc <- function(x,y) {
  a <- lm(log(y)~log(x))
  intercept = summary(a)$coefficients[1]
  slope = summary(a)$coefficients[2]
  Rsquare = summary(a)$r.squared[1]
  f_statistic = summary(a)$fstatistic[1]
  p_value = summary(a)$coefficients[8]
  DF <- c(intercept,slope,Rsquare,f_statistic,p_value)
  return(DF)
}

# create a table
Results <- MyDF %>% group_by(Type.of.feeding.interaction,Predator.lifestage) %>%
  summarise(regression_intercept = fc(Prey.mass,Predator.mass)[1],
            regression_slope = fc(Prey.mass,Predator.mass)[2],
            Rsquare = fc(Prey.mass,Predator.mass)[3],
            f_value = fc(Prey.mass,Predator.mass)[4],
            p_vlaue = fc(Prey.mass,Predator.mass)[5])

write.csv(Results,"../result/PP_Regress.csv",row.names = FALSE)
