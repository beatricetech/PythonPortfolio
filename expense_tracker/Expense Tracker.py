import json
expenses = []

def save_data():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)
    print('Data saved.')

def load_data():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def add_expense(name, amount, category):
    expenses.append({'name': name, 'amount': amount, 'category': category})
    print(f'{name} has been added.')

def view_all_expenses():
    if len(expenses) == 0:
        print('No expenses yet.')
    else:
        for expense in expenses:
            print(f'Name: {expense['name']} | Amount: {expense['amount']} | Category: {expense['category']}')

def search_expense(name):
    for expense in expenses:
        if expense['name'] == name:
            print(f'Name: {expense['name']} | Amount: {expense['amount']} | Category: {expense['category']}')
            return
    print(f'{name} not found.')

def delete_expense(name):
    for expense in expenses:
        if expense['name'] == name:
            expenses.remove(expense)
            print(f'{name} has been deleted.')
            return
    print(f'{name} not found.')

def view_total():
    total = 0
    for expense in expenses:
        total = total + expense['amount']
    print(f'Total spent: {total}')

def menu():
    load_data()
    while True:
        print('\n Expense Tracker ')
        print('1. Add expense')
        print('2. View all expense')
        print('3. Search expense')
        print('4. Delete expense')
        print('5. View total')
        print('6. Quit')

        choice = input('Choose an option: ')

        if choice == '1':
            name = input('Enter expense name: ')
            amount = float(input('Enter expense amount: '))
            category = input('Enter expense category: ')
            add_expense(name, amount, category)

        elif choice == '2':
            view_all_expenses()

        elif choice == '3':
            name = input('Enter expense name to search: ')
            search_expense(name)

        elif choice == '4':
            name = input('Enter expense name to delete: ')
            delete_expense(name)

        elif choice == '5':
            view_total()

        elif choice == '6':
            save_data()
            print('Goodbye!')
            break

        else:
            print('Invalid option. Try again.')        

menu()