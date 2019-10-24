rm(list = ls())
# extract data
MyDF <-read.csv("../data/EcolArchives-E089-51-D1.csv")

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
Results <- MyDF %>% group_by(Type.of.feeding.interaction,Predator.lifestage,Location) %>%
  summarise(regression_intercept = fc(Prey.mass,Predator.mass)[1],
            regression_slope = fc(Prey.mass,Predator.mass)[2],
            Rsquare = fc(Prey.mass,Predator.mass)[3],
            f_value = fc(Prey.mass,Predator.mass)[4],
            p_vlaue = fc(Prey.mass,Predator.mass)[5])

write.csv(Results,"../result/PP_Regress_Loc.csv",row.names = FALSE)