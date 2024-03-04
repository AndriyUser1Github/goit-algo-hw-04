"""
Бот-асистент
"""

def parse_input(user_input):
    """
    функція приймає рядок вводу і розбиває його 
    на слова, повертає перше слово як команду cmd
    та решту як список аргументів
    """

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    функція додає новий контакт до словника
    контактів, повертає рядок, що підтверджує
    успішне додавання контакту
    """

    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    """
    функція в контакті з вказаним іменем
    заміняє старий номер телефону на новий 
    номер телефону, якщо отримує команду про 
    підтвердження заміни, в противному випадку
    залишає старий номер телефону, повідомляє 
    про помилку, якщо ім'я не знайдено
    """
    
    name, phone = args
    if name in contacts:
        print("Replace the existing number with a new one?")
        a = input("Enter 'yes' or 'no': ")
        if a == 'yes':
            contacts[name] = phone
            return "Contact updated"
        else:
            return "No contact update"   
    return "No contact found with the name"

def show_phone(args, contacts):
    """
    функція виводить номер телефону, якщо 
    контакт з вказаним ім'ям існує в словнику
    контактів, або повідомлення про помилку,
    якщо контакту з вказаним ім'я не знайдено
    """

    name = args[0]
    if name in contacts:
        return contacts[name]
    return "No contact found with the name"

def show_all(contacts):
    """
    функція виводить усі збережені
    контакти з номерами телефонів
    """

    return contacts

def clear_all(contacts):
    """
    функція видаляє заданий контакт зі словника
    або всі контакти зі словника,
    очищає словник
    """

    
    print("Options for deleting 'contact'/'all'")
    a = input("Enter 'contact'/'all': ")
    if a == "contact":
        name = input("Contact name: ")
        del contacts[name]
        return "Contact has been deleted"
    else:
        contacts.clear()
        return "All contacts have been deleted"

def main():
    """
    функція управляє основним циклом обробки 
    команд
    """

    contacts = {}
    
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "delete":
            print(clear_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

