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
            elif query == "1":
                print(DSS_df[["Math test grades", "Science test grades", "Geography test grades", "English test grades"]])
            elif query == "2":
                print(DSS_df[["Homework rate: maths", "Homework rate: science", "Homework rate: geography", "Homework rate: english"]])
            else:
                print("Invalid choice, try again")
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
    subbywubby = input("Enter subject (maths/science/geography/english): ")
    if subbywubby.strip().lower() == "maths":
        test_grades_col = "Math test grades"
        homework_col = "Homework rate: maths"
        gradeles = ["A", "B", "C", "E"]
        avg_homework_by_grade = []
        
        for grade in gradeles:
            mask = DSS_df[test_grades_col].str.startswith(grade)
            avg_homework = DSS_df.loc[mask, homework_col].astype(int).mean()
            avg_homework_by_grade.append(avg_homework)

        plt.bar(gradeles, avg_homework_by_grade)
        plt.xlabel("Math Test Grades")
        plt.ylabel("Average Homework Rate (maths)")
        plt.title("Average Homework Rate by Math Test Grade")
        plt.show()
    elif subbywubby.strip().lower() == "science":
        test_grades_col = "Science test grades"
        homework_col = "Homework rate: science"
        gradeles = ["A", "B", "C", "E"]
        avg_homework_by_grade = []
        
        for grade in gradeles:
            mask = DSS_df[test_grades_col].str.startswith(grade)
            avg_homework = DSS_df.loc[mask, homework_col].astype(int).mean()
            avg_homework_by_grade.append(avg_homework)
        plt.bar(gradeles, avg_homework_by_grade)
        plt.xlabel("Science Test Grades")
        plt.ylabel("Average Homework Rate (science)")
        plt.title("Average Homework Rate by Science Test Grade")
        plt.show()
    elif subbywubby.strip().lower() == "geography":
        test_grades_col = "Geography test grades"
        homework_col = "Homework rate: geography"
        gradeles = ["A", "B", "C", "E"]
        avg_homework_by_grade = []
        
        for grade in gradeles:
            mask = DSS_df[test_grades_col].str.startswith(grade)
            avg_homework = DSS_df.loc[mask, homework_col].astype(int).mean()
            avg_homework_by_grade.append(avg_homework)
        

        plt.bar(gradeles, avg_homework_by_grade)
        plt.xlabel("Geography Test Grades")
        plt.ylabel("Average Homework Rate (geography)")
        plt.title("Average Homework Rate by Geography Test Grade")
        plt.show()
    elif subbywubby.strip().lower() == "english":
        test_grades_col = "English test grades"
        homework_col = "Homework rate: english"
        gradeles = ["A", "B", "C", "E"]
        avg_homework_by_grade = []
        
        for grade in gradeles:
            mask = DSS_df[test_grades_col].str.startswith(grade)
            avg_homework = DSS_df.loc[mask, homework_col].astype(int).mean()
            avg_homework_by_grade.append(avg_homework)
        
        plt.bar(gradeles, avg_homework_by_grade)
        plt.xlabel("English Test Grades")
        plt.ylabel("Average Homework Rate (english)")
        plt.title("Average Homework Rate by English Test Grade")
        plt.show()
    else:
        print("Invalid subject. Please enter maths, science, geography, or english.")


    