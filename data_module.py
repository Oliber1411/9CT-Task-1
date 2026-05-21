import os, time
import matplotlib.pyplot as plt
import pandas as pd
DSS_df = pd.read_csv("Data/DSS.csv")

def subj_choice():
            print("--Data--Viewer--Interface--")
            print("|                          |")
            print("|    1. View grades        |")
            print("|                          |")
            print("|    2. View homework      |")
            print("|                          |")
            print("|    3. View subject       |")
            print("|                          |")
            print("|    4. Go back            |")
            print("----------------------------")
            query = input("uhh choose one").strip()
            if query == "3":
                subject = input("Enter subject (maths/science/geography/english): ")
                if subject.strip().lower() == "maths":
                    print(DSS_df[["Math test grades", "Homework rate: maths"]])
                elif subject.strip().lower() == "science":
                    print(DSS_df[["Science test grades", "Homework rate: science"]])
                elif subject.strip().lower() == "geography":
                    print(DSS_df[["Geography test grades", "Homework rate: geography"]])
                elif subject.strip().lower() == "english":
                    print(DSS_df[["English test grades", "Homework rate: english"]])
                else:
                    print("Invalid subject, try again")
                    subj_choice()

def chice():
    choice = input("Enter choice (1-4) ")
    if choice == "1":
        clear_screen()
        print(DSS_df)
        choice()
    elif choice == "2":
        clear_screen()
        subj_choice()
    elif choice == "3":
        clear_screen()
        plot()
    elif choice == "4":
        print("Goodbye!")
        time.sleep(1)
        exit()
    else:
        print("Invalid choice, try again")
        chice()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def plot():
    DSS_df.plot(
        kind="bar",
         x= "Homework rate: maths",
         y="Math test grades",
         color="blue", 
        title="Maths Homework vs Test Grades"
    )
    plt.show()    


