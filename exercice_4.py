contacts = {}
debug = False

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return -1
        except IndexError:
            return -1
        except KeyError:
            return -1

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args):
    name, phone = args
    if(name.casefold() in contacts):
      return 1
    contacts[name.casefold()] = phone
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args
    if(name not in contacts):
      return 1
    contacts[name.casefold()] = phone
    return "Contact changed."

@input_error
def get_phone(args):
  if args[0].casefold() in contacts.keys():
    return contacts[args[0].casefold()]
  else:
    return 1

@input_error
def get_all(args):
  contacts_ = []
  for i in contacts:
    contacts_.append(i + ": " + contacts[i])
  return contacts_

def main():
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
            r = add_contact(args)
            if(r==1):
              print("Contact of " + args[0] + " already exists.")
            elif(r==-1):
              print("Enter the argument for the command")
            else:
              print(r)

        elif command == "change":
            r = change_contact(args)
            if(r==1):
              print("Contact of " + args[0] + " doesn`t exist.")
            elif(r==-1):
              print("Enter the argument for the command")
            else:
              print(r)

        elif command == "phone":
            r = get_phone(args)
            if(r==1):
              print("Contact of " + args[0] + " doesn`t exist.")
            elif(r==-1):
              print("Enter the argument for the command")
            else:
              print(r)

        elif command == "all":
            r = get_all(args)
            if(len(r) == 0):
              print("There are no contacts registried.")
            else:
              for i in r:
                print(i)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
