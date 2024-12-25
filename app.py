import pandas as pd
from enum import Enum
import platform
import os

file_name= "dmnd.csv"

df = pd.read_csv(file_name)

class Actions(Enum):
    MOST_EXPENSIVE=1
    AVERAGE_PRICE = 2
    COUNT_IDEAL=3
    COLOR_COUNT = 4
    MEDIAN_PREMIUM = 5
    AVERAGE_PER_CUT = 6
    PRICE_PER_COLOR = 7
    EXIT = 8

def menu():
    for act in Actions: print(f"{act.value} - {act.name}")
    while True:
            try:
                user_selection = int(input("Choose an option from the menu: "))
                return int(user_selection)
            except ValueError:
                print("wrong input, enter number from the menu.")


def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else: 
        os.system('clear')

def most_expensive():
    most_expensive_row = df['price'].max()
    print("the most expensive diamond is: ")
    print(most_expensive_row)

def average_diamond_price():
    average_price= df['price'].to_list()
    average= 0
    for price in average_price:
        average += price
    average = average / len(average_price)
    print(f"the average price is: {average}")

def count_ideal_diamonds():
    count_ideal = df['cut'].to_list()
    counter =0
    for cut in count_ideal:
        if cut == 'Ideal':
            counter += 1
    print(f"ther are {counter} Ideal diamonds.")

def count_color():
    unique_colors = df['color'].unique()
    color_count = df['color'].nunique()
    print(f"There are {color_count} unique colors.")
    print("The unique colors are:", unique_colors)

def median_premium():
    premium_diamonds = df[df['cut']== 'Premium']
    median_carat = premium_diamonds ['carat'].median()
    print(f"the median carat for 'Premium' diamonds is: {median_carat}")

def average_carat_per_cut():
    average_carat = df.groupby('cut')['carat'].mean()
    print("average carat per cut: ")
    for cut, avg_carat in average_carat.items():
        print(f"{cut}: {avg_carat}")

def average_per_color():
    avg_color = df.groupby('color')['price'].mean()
    print(f"the average price per color is: ")
    for color, avg_price in avg_color.items():
        print(f"{color}: {avg_price}")

if __name__=="__main__":
    while True:
        user_selection= menu()
        clear_terminal()
        if user_selection == Actions.EXIT.value : 
            exit()
        if user_selection == Actions.MOST_EXPENSIVE.value : 
            most_expensive()
        if user_selection == Actions.AVERAGE_PRICE.value : 
            average_diamond_price()
        if user_selection == Actions.COUNT_IDEAL.value : 
            count_ideal_diamonds()
        if user_selection == Actions.COLOR_COUNT.value :
            count_color()
        if user_selection == Actions.MEDIAN_PREMIUM.value :
            median_premium()
        if user_selection == Actions.AVERAGE_PER_CUT.value :
            average_carat_per_cut()
        if user_selection == Actions.PRICE_PER_COLOR.value :
            average_per_color()
        