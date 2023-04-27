import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('ENTER THE CITY (chicago, new york city, washington): ').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ("Sorry, I didn't catch that. Try again.\nENTER CITY: chicago, new york city OR washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('ENTER MONTH (all, january, february, ... , june): ').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Sorry, I didn't catch that. Try again.\nENTER MONTH all, january, february, ... , june : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('ENTER DAY (all, monday, tuesday, ... sunday): ').lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
        day = input("Sorry, I didn't catch that. Try again.\nENTER DAY all, monday, tuesday, ... sunday: ").lower()


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
    #Load Dataraw from file input 
    
    df = pd.read_csv(CITY_DATA[city])
    #Convert data type Start Time and End Time into date format yyyy-mm-dd
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Add new column months extract month from Start Time 
    df['month'] = df['Start Time'].dt.month
    # Add new column day_of_week extract day from Start Time
    df['day_of_week'] =pd.to_datetime(df['Start Time']).dt.day_name()
    # Add new column hour extract day from Start Time
    df['hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
       

    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df['day_of_week'])
    #print(df)
    # TO DO: display the most common month
    # print("The most common month is: ", df['month'].value_counts().idxmax())
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    #print(df['day_of_week'])
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print("The most common hour is: ", df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum() / 3600.0
    print("Total travel time in hours is: ", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean() / 3600.0
    print("Mean travel time in hours is: ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("Counts of user types")
    print(user_type)

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print("\nCounts of gender\n")
        print(user_gender)
    except:
        print("Data does not exist data column Gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].value_counts().idxmax())
        print("The earliest year of birth is:",earliest,
              ", most recent one is:",most_recent,
              "and the most common one is: ",most_common)
    except:
        print("Data does not exist data column Birth Year")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    begin_row = 0
    end_row = 5
    df_row= len(df.index)

    while begin_row < df_row:
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':
            print("\nDisplaying only 5 rows of data.\n")
            if end_row > df_row:
                end_row = df_row
            print(df.iloc[begin_row:end_row])
            begin_row += 5
            end_row += 5
        else:
            break
# This is the main method
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
