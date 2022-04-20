import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_filters():
    cities = ["chicago", "new york city", "washington"]
    while True:
        city = input("which city what you want ??")
        if city in cities:
            break
        else:
            print("wrong city, please enter the correct city")
    months = ["january", "february", "march", "april", "may", "june", "all"]
    while True:

        month = input("which month ??")
        if month in months:
             break
        else:
            print("wrong month, enter the correct month")

    days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday","all"]
    while True:
        day_selected = input("which day ??")
        if day_selected in days:
            break
        else:
            print("wrong day selected")


    print('-'*40)
    return city, month, day_selected

def load_data(city, month, day_selected):
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # TO DO: get user input for month (all, january, february, ... , june)
    df["month"] = df["Start Time"].dt.month
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    df["start hour"] = df["Start Time"].dt.hour
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month)+1
        df = df[df["month"] == month]
    if day_selected != "all":
        days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
        df = df[df["day_of_week"] == day_selected.title()]
    return df
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print("the most common month is : {}".format(df["month"].mode()[0]))
    # TO DO: display the most common day of week
    print("the most common day is: {}".format(df["day_of_week"].mode()[0]))
    # TO DO: display the most common start hour
    print("the most common start hour is: {}".format(df["start hour"].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("the most commonly used start station is:")
    print(df["Start Station"].mode()[0])
    # TO DO: display most commonly used end station
    print("the most commonly used end station is:")
    print(df["End Station"].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + "," + df["End Station"]
    print("the most frequent combination of stations is: {}".format(df["combination"].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print("the total travel time is :", (df["Trip Duration"].sum()))
    # TO DO: display mean travel time
    print("the average travel time is:",(df["Trip Duration"].mean()).round())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df, city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print(df["User Type"].value_counts())
    if city != "washington":
    # TO DO: Display counts of gender
        print(df["Gender"].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print("the most common year of birth is:", int(df["Birth Year"].mode()[0]))
        print("the most recent year of birth is:", int(df["Birth Year"].max()))
        print("the earliest year of birth is:", int(df["Birth Year"].min()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
