# Import packages
library(psych)
library(survival)
library(survminer)
library(readr)
library(broom)
library(GPArotation)

# Load the factor_data.csv
factor_data <- read_csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/R%20Projects/factor_data.csv")

# Load the survival_data.csv
survival_data <- read_csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/R%20Projects/survival_data.csv")

# Check the top of the data sets
head(factor_data, 5)
head(survival_data, 5)

# Create corelation matrices for factor_data and SpeciesDiversity column
cor_factor_data <- cor(factor_data)
cor_species_diversity <- cor_factor_data["SpeciesDiversity", ]

# Remove corellation with itself
cor_species_diversity <- cor_species_diversity[names(cor_species_diversity) != "SpeciesDiversity"]
print(cor_species_diversity)

# Find the factor that influences wildilife populations the most
most_impactful_factor <- names(which.max(abs(cor_species_diversity)))
print(most_impactful_factor)

# Number of factors
num_factors <- length(cor_species_diversity)
print(num_factors)

# Scree Plot
scree(factor_data, factors = FALSE, main = "EFA plot")

# Parallel plot
fa.parallel(factor_data, fa = "fa", n.iter = 100, main = "Parallel Analysis")

# Actual analysis, nfactors based on the scree plot
num_factors <- 2
EFA_model <- fa(factor_data, nfactors = num_factors)

# The results
print(EFA_model$loadings)  # Factor loadings
print(EFA_model$communality)  # Communalities
print(EFA_model$Vaccounted)  # Variance explained

# Survival Analysis
survival_object <- Surv(survival_data$Survival_Time, survival_data$Censoring_Status)
print(survival_object)

# Fit the model
survival_fit <- survfit(survival_object ~ Habitat, data = survival_data)
survival_fit_df <- tidy(survival_fit)
summary(survival_fit)

# Which habitat drops to the lowest survival probability? Based on the survplot
surv_plot <- ggsurvplot(survival_fit, data = survival_data)
print(surv_plot)
low_surv_habitat <- "Savanna"