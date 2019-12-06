# create three lattice plots and calculate the mean and median of each data
rm(list = ls())
# extract data and check the size and content of it
MyDF <-read.csv("../data/EcolArchives-E089-51-D1.csv")
str(MyDF)
dim(MyDF)

require(lattice)
# create and save lattice plots
pdf("../result/Pred_Lattice.pdf",11.7,8.3)
print(densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data = MyDF))
dev.off()

pdf("../result/Prey_Lattice.pdf",11.7,8.3)
print(densityplot(~log(Prey.mass) | Type.of.feeding.interaction,data = MyDF))
dev.off()

pdf("../result/SizeRatio_Lattice.pdf",11.7,8.3)
print(densityplot(~log(Prey.mass/Predator.mass) | Type.of.feeding.interaction, data = MyDF))
dev.off()

# calculate and output the mean and median 
require(dplyr)
table <- MyDF %>% select(Predator.mass,Prey.mass,Type.of.feeding.interaction) %>%
  mutate(Ratio=Prey.mass/Predator.mass) %>%
  group_by(Type.of.feeding.interaction) %>%
  summarise(mean_Pred.mass=mean(log(Predator.mass)),mean_Prey.mass=mean(log(Predator.mass)),mean_Ratio=mean(log(Ratio)),
            median_Pred.mass=median(log(Predator.mass)),medain_Prey.mass=median(log(Prey.mass)),median_Ratio=median(log(Ratio))) %>%
  ungroup()

# output as .csv file
write.table(table,"../result/PP_Results.csv",row.names = FALSE)
