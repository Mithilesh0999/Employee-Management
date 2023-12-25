import json

def load_data(file_path='D:/PYyyyyyy/employee_data.txt'):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

def save_data(data, file_path='D:/PYyyyyyy/employee_data.txt'):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def register_employee(employee_id, name, position, salary):
    data = load_data()
    if employee_id not in data:
        data[employee_id] = {'name': name, 'position': position, 'salary': salary}
        save_data(data)
        print(f"Employee {name} (ID: {employee_id}) registered successfully.")
    else:
        print(f"Employee with ID {employee_id} already exists.")

def update_employee(employee_id, new_salary, new_position):
    data = load_data()
    if employee_id in data:
        data[employee_id]['salary'] = new_salary
        data[employee_id]['position'] = new_position
        save_data(data)
        print(f"Employee {data[employee_id]['name']} (ID: {employee_id}) updated successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")

def view_employee(employee_id):
    data = load_data()
    if employee_id in data:
        print("\nEmployee Details:")
        print(f"ID: {employee_id}")
        print(f"Name: {data[employee_id]['name']}")
        print(f"Position: {data[employee_id]['position']}")
        print(f"Salary: {data[employee_id]['salary']}")
    else:
        print(f"Employee with ID {employee_id} not found.")
def delete_employee(employee_id):
    data = load_data()
    if employee_id in data:
        deleted_name = data[employee_id]['name']
        del data[employee_id]
        save_data(data)
        print(f"Employee {deleted_name} (ID: {employee_id}) deleted successfully.")
    else:
        print(f"Employee with ID {employee_id} not found.")


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Register Employee")
        print("2. Update Employee Details")
        print("3. View Employee Details")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = input("Enter Employee Salary: ")
            register_employee(employee_id, name, position, salary)
        elif choice == '2':
            employee_id = input("Enter Employee ID to update: ")
            new_salary = input("Enter new Salary: ")
            new_position = input("Enter new Position: ")
            update_employee(employee_id, new_salary, new_position)
        elif choice == '3':
            employee_id = input("Enter Employee ID to view details: ")
            view_employee(employee_id)
        elif choice == '4':
            employee_id = input("Enter Employee ID to delete: ")
            delete_employee(employee_id)
        elif choice == '5':
            print("Exiting the Employee Management System.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
