
phone_book = {}

# помилки при введені даних
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "There is no such contact in the phone book"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter user name"
    return inner

@input_error
def add_contact(name, phone):
    phone_book[name] = phone
    return "Contact was added successfully"

@input_error
def change_phone(name, phone):
    phone_book[name] = phone
    return "Phone number was changed successfully"

@input_error
def get_phone(name):
    return phone_book[name]

def show_all():
    result = ""
    for name, number in phone_book.items():
        result += f"{name}: {number}\n"
    return result.strip()

def main():
    while True:
        command = input("Enter command: ")
        command = command.lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_contact(name, phone))
            except:
                print("Give me name and phone please")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change_phone(name, phone))
            except:
                print("Give me name and phone please")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except:
                print("Enter contact name")
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == ".":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
