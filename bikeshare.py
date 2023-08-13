import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
weekdays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    city_list = ['chicago','new york city','washington']
    while city not in city_list :
        city = input('Enter City from (chicago, new york city, washington) : ').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    months_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months_list :
        month = input('Enter month from (all, january, february, ... , june) : ').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    weekday_list = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
    while day not in weekday_list :
        day = input('Enter weekday from (all, sunday, monday, ... , saturday) : ').lower()
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']== month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most frequent month = ',months[df['month'].mode()[0]-1].title())

    # TO DO: display the most common day of week
    print('Most frequent day of week = ', df['day_of_week'].mode()[0].title())

    # TO DO: display the most common start hour
    print('Most frequent start hour = ',df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station = ',df['Start Station'].mode()[0].title())
    # TO DO: display most commonly used end station
    print('Most commonly used end station = ',df['End Station'].mode()[0].title())
    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip = ',df[['Start Station', 'End Station']].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time in hours :", df['Trip Duration'].sum()/3600)

    # TO DO: display mean travel time
    print("Mean travel time in hours :", df['Trip Duration'].mean()/3600)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of user types :",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Count of gender :",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest year of birth :",df['Birth Year'].min())
        print("Most recent year of birth :",df['Birth Year'].max())
        print("Most common year of birth :",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    response = ['yes', 'no'] 
    view_data = input('\n Would you like to view 5 rows of individual trip data ? Enter yes or no\n').lower()
    start_loc = 0
    loc = start_loc + 5
    row_length = df.shape[0]
    while (view_data == 'yes' and loc < row_length) :
        print(df.iloc[start_loc : loc])
        view_data = input('\n Do you wish to continue and see next 5 rows ? Enter yes or no\n').lower()
        if view_data == 'yes':
            start_loc = start_loc + 5
            loc = loc + 5
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()