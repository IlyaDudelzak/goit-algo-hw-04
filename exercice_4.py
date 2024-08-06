contacts = {}
debug = False

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args):
  try:
    if args[0].casefold() in contacts.keys():
      return 1
    else:
      contacts[args[0].casefold()] = args[1].casefold()
      return 0
  except Exception as e:
    return -1
    if(debug):
      print(e)

def change_contact(args):
  try:
    if args[0].casefold() in contacts.keys():
      contacts[args[0].casefold()] = args[1].casefold()
      return 0
    else:
      return 1
  except Exception as e:
    return -1
    if(debug):
      print(e)

def get_phone(args):
  try:
    if args[0].casefold() in contacts.keys():
      return contacts[args[0].casefold()]
    else:
      return 1
  except Exception as e:
    return -1
    if(debug):
      print(e)

def get_all(args):
  try:
    contacts_ = []
    for i in contacts:
      contacts_.append(i + ": " + contacts[i])
    return contacts_
  except Exception as e:
    
    if(debug):
      print(e)

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
            if(r==0):
              print("Success!")
            elif(r==1):
              print("Contact of " + args[0] + " already exists.")
            elif(r==-1):
              print("Wrong args!")

        elif command == "change":
            r = change_contact(args)
            if(r==0):
              print("Success!")
            elif(r==1):
              print("Contact of " + args[0] + " doesn`t exist.")
            elif(r==-1):
              print("Wrong args!")

        elif command == "phone":
            r = get_phone(args)
            if(r==1):
              print("Contact of " + args[0] + " doesn`t exist.")
            elif(r==-1):
              print("Wrong args!")
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
