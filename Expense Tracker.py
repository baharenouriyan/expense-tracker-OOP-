import json

FILE_NAME = "expenses.json"


# خواندن اطلاعات از فایل
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# ذخیره اطلاعات داخل فایل
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# اضافه کردن تراکنش
def add_transaction():
    data = load_data()

    t_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    transaction = {
        "type": t_type,
        "amount": amount,
        "category": category
    }

    data.append(transaction)
    save_data(data)

    print(":white_check_mark: Transaction added!\n")


# نمایش تراکنش‌ها
def view_transactions():
    data = load_data()

    if not data:
        print("No transactions found.\n")
        return

    print("\n------ Transactions ------")

    for t in data:
        print(f'{t["type"]} | {t["amount"]} | {t["category"]}')

    print()


# نمایش موجودی
def show_balance():
    data = load_data()

    balance = 0

    for t in data:
        if t["type"] == "income":
            balance += t["amount"]
        else:
            balance -= t["amount"]

    print(f"\n:moneybag: Your balance is: {balance}\n")


# منوی برنامه
def menu():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            show_balance()

        elif choice == "4":
            print("Goodbye :wave:")
            break

        else:
            print("Invalid choice!\n")


# اجرای برنامه
menu()
