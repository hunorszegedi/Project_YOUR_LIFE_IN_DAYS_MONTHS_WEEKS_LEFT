the_age = (int)(input("When you wanna die? "))
your_age = (int)(input("What is your age? "))

year_90_days = 90 * 365
year_90_months = 90 * 12
year_90_weeks = 90 * 52

my_year_years_remaining = the_age - your_age
my_year_days_left = my_year_years_remaining * 365
my_year_months_left = my_year_years_remaining * 12
my_year_weeks_left = my_year_years_remaining * 52

message = f"My brother, if you lived until 90, you have:\n{my_year_days_left} days left\n{my_year_months_left} months left\n{my_year_weeks_left} weeks left\n"
print(message, "\n\t\tA man who dares to waste one hour of time has not discovered the value of life. ~ Charles Darwin")
