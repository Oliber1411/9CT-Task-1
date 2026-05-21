import os, time
import matplotlib.pyplot as plt
import pandas as pd
import data_module
from data_module import DSS_df, subj_choice, chice, clear_screen, plot




DSS_df = pd.read_csv("Data/DSS.csv")###I hope were not supposed to add comments cus uhh im not gonna 😎😎😎 they should gray out the emojis for comments XD


def menu():
    while True:
        print("--Data--Viewer--Interface--")
        print("|                          |")
        print("|    1. View datasheet     |")
        print("|                          |")
        print("|    2. Specify data       |")
        print("|                          |")
        print("|   3. View visualizations |")
        print("|                          |")
        print("|    4. Quit               |")
        print("----------------------------")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            print(DSS_df)
            back = input("Enter to go back: ")
        elif choice == '2':
            subj_choice()
            back = input("Enter to go back:")
        elif choice == '3':
            plot()
            back = input("Enter to go back:")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    menu()