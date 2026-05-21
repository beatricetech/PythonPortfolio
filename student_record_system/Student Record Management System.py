import json

students = {}

def save_data():
    with open('students.json', 'w') as file:
        json.dump(students, file)
    print('Data saved.')

def load_data():
    global students
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = {}

def add_student(name, scores):
    students[name] = scores
    print(f"{name} has been added.")

def view_all_students():
    if len(students) == 0:
        print('No students yet.')
    else: 
        for name, scores in students.items():
            average = sum(scores)/len(scores)
            print(f'{name} | Scores: {scores} | Average: {average:.1f}')

def search_student(name):
    if name in students:
        scores = students[name]
        average = sum(scores)/len(scores)
        print(f'{name} | Scores: {scores} | Average: {average:.1f}')
    else:
        print(f'{name} not found.')

def delete_student(name):
    if name in students:
        del students[name]
        print(f'{name} has been deleted.')
    else:
        print(f'{name} not found.')

def menu():
    load_data()
    while True:
        print('/n--- Student Records ---')
        print('1. Add Student')
        print('2. View All Students')
        print('3. Search Student')
        print('4. Delete Student')
        print('5. Quit')

        choice = input('choose an option:')

        if choice == '1':
            name = input('Enter student name: ')
            scores_input = input('Enter scores separated by commas: ')
            scores = [int(x) for x in scores_input.split(',')]
            add_student(name, scores)

        elif choice == '2':
            view_all_students()

        elif choice == '3':
            name = input('Enter student name to search: ')
            search_student(name)

        elif choice == '4':
            name = input('Enter student name to delete: ')
            delete_student(name)

        elif choice == '5':
            save_data()
            print('Goodbye!')
            break
        
        else:
            print('invalid option. Try again.')

menu()