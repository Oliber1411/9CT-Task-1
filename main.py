import os, time
import matplotlib.pyplot as plt
import pandas as pd
import data_module
from data_module import DSS_df, subj_choice, chice, clear_screen, plot

DSS_df = pd.read_csv("Data/DSS.csv")


def menu():
    print("--Data--Viewer--Interface--")
    print("|                          |")
    print("|    1. View datasheet     |")
    print("|                          |")
    print("|    2. View Subject       |")
    print("|                          |")
    print("|  3. View average versus  |")
    print("|                          |")
    print("|    4. Quit               |")
    print("----------------------------")



if __name__ == "__main__":
    menu()
    chice()
