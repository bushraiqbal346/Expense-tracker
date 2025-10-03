import csv
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

def add_expense(date, category, amount):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\nYour Expenses:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found yet.")

def plot_expenses():
    categories = {}
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    category = row[1]
                    amount = float(row[2])
                    categories[category] = categories.get(category, 0) + amount
        plt.bar(categories.keys(), categories.values())
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
    except FileNotFoundError:
        print("No expenses to plot yet.")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Plot Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Travel, etc.): ")
            amount = input("Enter amount: ")
            add_expense(date, category, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            plot_expenses()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
