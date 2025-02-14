# Load the necessary packages (install first if needed)
library(readr)
library(dplyr)
library(ggplot2)
library(broom)

# Load the data
data <- read.csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/R%20Projects/kidney_stone_data.csv")

# Inspect the first five rows
head(data, 5)

# Create the model
logistic_model <- glm(success ~ treatment + stone_size, data = data, family = binomial)

# Model summary
summary(logistic_model)

print(logistic_model)

# Describe the results
Results <-"Adding all the values gives us the success rate of treatment B on small sized stones, which is 1.9366. This value is higher than Intercept (general rate of success),
meaning that Treatment B has by far higher chance of success than the baseline of treatment A on large stones"

print(Results)
