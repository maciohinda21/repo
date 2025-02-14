library(dplyr)
library(tidyr)
library(ggplot2)
library(ggthemes)

life_expectancy <- read.csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/R%20Projects/UNdata.csv") # nolint: line_length_linter.

# Is anything missing from Value column?
sum(is.na(life_expectancy$Value))
# Answer to the question
missing <- FALSE

# Calculate the average of life expectancy grouped by gender
avg_values_by_subgroup <- life_expectancy %>%
  group_by(Subgroup) %>%
  summarise(avg_value = mean(Value, na.rm = TRUE))
avg_values_by_subgroup
# Group with higher life expectance
subgroup <- "Female"

# Largest disparities between genders

df_disparities <- life_expectancy %>%
  group_by(Country.or.Area, Subgroup) %>%
  filter(Year == "2000-2005") %>%
  summarize(mean_life_expectancy = mean(Value, na.rm = TRUE)) %>%
  spread(Subgroup, mean_life_expectancy) %>%
  mutate(disparity = abs(Female - Male)) %>%
  arrange(desc(disparity)) %>%
  top_n(3, disparity)
df_disparities

# Top 3 countries with largest male-female disparities
disparities <- df_disparities %>%
  arrange(desc(disparity)) %>%
  head(3) %>%
  select(Country.or.Area) %>%
  .[[1]]
print(disparities)

# Create the plot
p <- ggplot(life_expectancy, aes(x = Value, y = Subgroup, color = Year)) +
  geom_point(size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE, linetype = "dashed") +
  scale_color_brewer(palette = "Set1") +
  theme_minimal() +
  theme(
    plot.title = element_text(hjust = 0.5, size = 24, face = "bold"),
    plot.subtitle = element_text(hjust = 0.5, size = 18),
    axis.title = element_text(size = 16),
    axis.text = element_text(size = 14),
    legend.position = "bottom"
  ) +
  labs(
       title = "Life expectancy by gender scatterplot",
       x = "Years",
       y = "Gender",
       color = "Category")
print(p)