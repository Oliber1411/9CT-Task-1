import os, time
import matplotlib.pyplot as plt
import pandas as pd
import data_module
from data_module import DSS_df, subj_choice, chice, clear_screen, plot
# Source - https://stackoverflow.com/q/62534037
# Posted by Morgpan
# Retrieved 2026-05-21, License - CC BY-SA 4.0



DSS_df = pd.read_csv("Data/DSS.csv")


def menu():
    while True:
        print("--Data--Viewer--Interface--")
        print("|                          |")
        print("|    1. View datasheet     |")
        print("|                          |")
        print("|    2. Search data        |")
        print("|                          |")
        print("|   3. View visualizations |")
        print("|                          |")
        print("|    6. Quit               |")
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
            update_data_entry()
        elif choice == '5':
            save_changes()
            print("Changes saved.")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    menu()