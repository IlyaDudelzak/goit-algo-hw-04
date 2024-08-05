contacts = []
debug = True

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args):
  try:
    contacts.append({"name":args[0].casefold(), "phone":args[1].casefold()})
  except Exception as e:
    print("Wrong args!")
    if(debug):
      print(e)

def change_contact(args):
  try:
    for i in range(len(contacts)):
      if(args[0].casefold() == contacts[i]["phone"]):
        contacts[i]["phone"] = args[1]

  except Exception as e:
    print("Wrong args!")
    if(debug):
      print(e)

def show_phone(args):
  try:
    for i in contacts:
      if(args[0].casefold() == i["name"]):
        print(i["phone"])

  except Exception as e:
    print("Wrong args!")
    if(debug):
      print(e)

def show_all(args):
  try:
    for i in contacts:
      print(i["name"] + ": " + i["phone"])

  except Exception as e:
    print("Wrong args!")
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
            add_contact(args)
        elif command == "change":
            change_contact(args)
        elif command == "phone":
            show_phone(args)
        elif command == "all":
            show_all(args)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
