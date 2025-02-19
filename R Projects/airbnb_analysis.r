suppressMessages(library(dplyr)) # This line is required to check your answer correctly
options(readr.show_types = FALSE) # This line is required to check your answer correctly
library(readr)
library(readxl)
library(stringr)

# Preparing the files with review_dates
airbnb_prices <- read.csv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/R%20Projects/airbnb_price.csv")
airbnb_rooms <- read_excel("https://github.com/maciohinda21/repo/raw/refs/heads/main/R%20Projects/airbnb_room_type.xlsx")
airbnb_reviews <- read_tsv("https://raw.githubusercontent.com/maciohinda21/repo/refs/heads/main/R%20Projects/airbnb_last_review.tsv", show_col_types = FALSE)

# View contents
head(airbnb_reviews, 5)
head(airbnb_prices, 5)
head(airbnb_rooms, 5)

# Join airbnb_prices and airbnb_rooms
joined_data <- inner_join(airbnb_prices, airbnb_rooms, by = "listing_id")

# Join the tables
final_data <- inner_join(joined_data, airbnb_reviews, by = "listing_id")

# First and last reviewed room
# Convert the last_review column to Date format with the specified format
final_data$last_review <- as.Date(final_data$last_review, format = "%b %d %Y")


# Find the row with the earliest and latest review date
first_reviewed <- final_data[which.min(final_data$last_review), ]
first_reviewed_date <- format(first_reviewed$last_review, "%Y-%m-%d")
last_reviewed <- final_data[which.max(final_data$last_review), ]
last_reviewed_date <- format(last_reviewed$last_review, "%Y-%m-%d")

# Number of private rooms available
final_data$room_type <- tolower(final_data$room_type) # Convert room_type to lowercase
nb_private_rooms <- sum(final_data$room_type == "private room")
print(unique(final_data$room_type))

# Average price. Remove dollars word from the column
avg_price <- mean(as.numeric(gsub(" dollars", "", final_data$price)))

review_dates <- tibble(
  first_reviewed = first_reviewed_date,
  last_reviewed = last_reviewed_date,
  nb_private_rooms = nb_private_rooms,
  avg_price = avg_price
)
print(review_dates)