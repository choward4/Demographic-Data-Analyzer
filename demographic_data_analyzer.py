import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file and set commonly used variables
    df = pd.read_csv('adult.data.csv')
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df['age'].values.mean()

    # What is the percentage of people who have a Bachelor's degree?
    edu = df['education']
    total = edu.count()
    bachelors = edu[edu == 'Bachelors'].count()

    percentage_bachelors = (bachelors / total) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    advanced_arr = (edu == 'Bachelors') | (edu == 'Masters') | (edu == 'Doctorate')

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = edu[advanced_arr].count()
    lower_education = edu[~advanced_arr].count()
    # Earning over 50K
    over_50K = df['salary'] == '>50K'

    # percentage with salary >50K
    higher_education_rich = edu[advanced_arr & over_50K].count() / higher_education * 100
    lower_education_rich = edu[~advanced_arr & over_50K].count() / lower_education * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hours = df['hours-per-week']

    minimum = hours.min()
    num_min_workers = hours.value_counts()[minimum]

    rich_percentage = ((hours == minimum) & over_50K).sum() / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = 0

    for country in df['native-country'].value_counts().index:
        country_arr = df['native-country'] == country
        total_pop = country_arr.sum()
        percentage = (country_arr & over_50K).sum() / total_pop * 100
        
        # Update with the highest percentage if the current percentage is higher
        if percentage > highest_earning_country_percentage:
            highest_earning_country_percentage = percentage
            highest_earning_country = country

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = (df['native-country'] == 'India') & over_50K
    
    top_IN_occupation = df['occupation'][india_rich].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
