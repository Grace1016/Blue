library("ggplot2")
library("minpack.lm")
library("zoo")
library("dplyr")
library("nls.multstart")

data <- read.csv("../data/start_val_data.csv")
cla_params <- read.csv("../results/classical_model.csv")
gom_params <- read.csv("../results/gompertz_model.csv")
bar_params <- read.csv("../results/baranyi_model.csv")
bucha_params <- read.csv("../results/buchanan_model.csv")
cubic_params <- read.csv('../results/cubic_model.csv')

data_subset <- subset(data,ID %in% 1)
data_subset <- data_subset[order(data_subset$Time),]

e <- exp(1)

#create the rolling regression function to plot the slope
roll_regress <- function(x){
  temp <- data.frame(x)
  mod <- lm(temp)
  temp <- data.frame(slope = coef(mod)[[2]],
                     slope_lwr = confint(mod)[2, ][[1]],
                     slope_upr = confint(mod)[2, ][[2]],
                     intercept = coef(mod)[[1]],
                     rsq = summary(mod)$r.squared, stringsAsFactors = FALSE)
  return(temp)
}
num_points <- 4

# run rolling regression on logN ~ t
models <- data_subset %>%
  do(cbind(model = select(.,Log_PopBio, Time) %>% 
             zoo::rollapplyr(width = num_points, roll_regress, by.column = FALSE, fill = NA, align = 'center'),
           time = select(., Time),
           ln_od = select(., Log_PopBio))) %>%
  rename_all(., gsub, pattern = 'model.', replacement = '')

# create predictions
preds <- models %>%
  filter(., !is.na(slope)) %>%
  group_by(Time) %>%
  do(data.frame(time2 = c(.$Time - 60, .$Time + 100))) %>%
  left_join(., models) %>%
  mutate(pred = (slope*time2) + intercept)

growth_rate <- filter(models, slope == max(slope, na.rm = TRUE))

# plot rolling 
p <- ggplot(data_subset, aes(Time, Log_PopBio)) +
  geom_point(size = 1) +
  geom_line(aes(time2, pred, group = Time), col = 'red', preds, alpha = 0.3, size = 0.4) +
  theme_bw(base_size = 16) +
  labs(x = "Time", y = "Log_PopBio")

# plot the line with maximum slope and show Rmax
p1 <- ggplot(data_subset, aes(Time, Log_PopBio)) + geom_point(size = 1) +
  geom_abline(data= growth_rate, color = 'blue', slope = growth_rate$slope, intercept=growth_rate$intercept)+
  annotate(geom = 'text', x=400, y=0.04, label = paste('Rmax = ', growth_rate$slope,2), hjust=0)

# create a funtion to get the calculated data for ggplot
classical_model <- function(id,dataframe){
  if(!is.na(subset(cla_params, ID == id)$aic)){
    x <- subset(dataframe, ID == id)$Time
    x <- seq(min(x), max(x), length.out = 100) # create sequence of length 100 from min to max temperature
    
    # get parameters value
    N0 <- subset(cla_params, ID == id)$N0
    Nmax <- subset(cla_params, ID == id)$Nmax
    Rmax <- subset(cla_params, ID == id)$Rmax
    
    # put sequence through model to get predicted trait values
    y <- (N0*Nmax*(e**(Rmax*x)))/((Nmax+N0*(e**(Rmax*x)-1)))
    data.frame(x, y, model = "Classical model")  # return as dataframe
  }
}

# similar as above
gompertz_model <- function(id,dataframe){
  if(!is.na(subset(gom_params, ID == id)$aic)){
    x <- subset(dataframe, ID == id)$Time
    x <- seq(min(x), max(x), length.out = 100) # create sequence of length 100 from min to max temperature
    
    # get parameters value
    A <- subset(gom_params, ID == id)$A 
    Tlag <- subset(gom_params, ID == id)$Tlag
    Rmax <- subset(gom_params, ID == id)$Rmax
    
    # put sequence through model to get predicted trait values
    y <- A*(e**(-e**((Rmax*e*(Tlag-x))/A)+1))
    data.frame(x, y, model = "Gompertz model")  # return as dataframe
  }
}

baranyi_model <- function(id,dataframe){
  if(!is.na(subset(bar_params, ID == id)$aic)){
    x <- subset(dataframe, ID == id)$Time
    x <- seq(min(x), max(x), length.out = 100) # create sequence of length 100 from min to max temperature
    
    # get parameters value
    N0 <- subset(bar_params, ID == id)$N0
    Nmax <- subset(bar_params, ID == id)$Nmax
    Rmax <- subset(bar_params, ID == id)$Rmax
    H0 <- subset(bar_params, ID == id)$H0
    
    
    # put sequence through model to get predicted trait values
    At = x+(1+Rmax)*(log((e**(-Rmax*x)+H0)/(1+H0)))
    y <- N0+Rmax*At-(log(1+((e**(Rmax*At)+1)/e**(Nmax-N0))))
    data.frame(x, y, model = "Baranyi model")  # return as dataframe
  }
}

buchanan_model <- function(id,dataframe){
  if(!is.na(subset(bucha_params, ID == id)$aic)){
    x <- subset(dataframe, ID == id)$Time
    x <- seq(min(x), max(x), length.out = 100) # create sequence of length 100 from min to max temperature
    
    # get parameters value
    N0 <- subset(bucha_params, ID == id)$N0
    Nmax <- subset(bucha_params, ID == id)$Nmax
    u <- subset(bucha_params, ID == id)$u
    Tlag <- subset(bucha_params, ID == id)$Tlag
    
   # put sequence through model to get predicted trait values  
    y <- (N0 +(x >= Tlag)*(x <= (Tlag +  (Nmax - N0) * log(10)/u)) *u* (x-Tlag)/log(10) +
               (x >= Tlag) * (x > (Tlag + (Nmax - N0) * log(10)/u)) * (Nmax - N0))
    data.frame(x, y, model = "Buchanan model")  # return as dataframe
  }
}

# similar as above
cubic_model <- function(id,dataframe){
  if(!is.na(subset(gom_params, ID == id)$aic)){
    x <- subset(dataframe, ID == id)$Time
    x <- seq(min(x), max(x), length.out = 100) # create sequence of length 100 from min to max temperature
    
    # get parameters value
    a <- subset(cubic_params, ID == id)$a
    b <- subset(cubic_params, ID == id)$b
    c <- subset(cubic_params, ID == id)$c
    d <- subset(cubic_params, ID == id)$d
    
    # put sequence through model to get predicted trait values
    y <- a + b*x + c*x^2 + d*x^3
    data.frame(x, y, model = "Cubic model")  # return as dataframe
  }
}

#model plotting function
models_plot <- function(id,dataframe){
  # data points for curve x = temperature (K), y = logged trait value
  points <- subset(dataframe, ID == id, select = c(Time, Log_PopBio))
  colnames(points) <- c("Time", "Log_PopBio")
  
  # rbind the dataframes which are output from the model functions (100 x and
  # y values) suppressWarnings used as NAs are produced when the curves do
  # not converge
  suppressWarnings(models <- rbind(classical_model(id, dataframe),
                                   gompertz_model(id, dataframe),
                                   baranyi_model(id, dataframe),
                                   buchanan_model(id, dataframe),
                                   cubic_model(id,dataframe)))
  models <- na.omit(models)  # remove NAs (models which did not converge)
  rownames(models) <- NULL   # get rid of row names (which mess with ggplot)
  colnames(models) <- c("Time", "Log_PopBio", "model")
  models$Time  <- as.numeric(models$Time)
  models$Log_PopBio <- as.numeric(models$Log_PopBio)
  
  plt <- ggplot(models, aes(Time, Log_PopBio))
  plt <- plt + geom_line(aes(color = model, linetype = model))
  plt <- plt + geom_point(data = points)  # add the data points from the points df
  plt <- plt + theme_classic()
  plt <- plt + theme(legend.position = "bottom")
  plt <- plt + xlab("Time")
  plt <- plt + ylab("Log_PopBio")
  return(plt)
  
}







