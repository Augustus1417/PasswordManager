import random, string, json

def line(): 
    for x in range(50): print("-",end="")
    print()

def encrypt(message): # Uses caesar cipher to encrypt strings
    cipher = ""
    for x in message:
        newOrd = ord(x) + 5 
        cipher += chr(newOrd)
    return cipher

def decrypt(cipher):
    ciphered = ""
    for x in cipher:
        newOrd = ord(x) - 5 
        ciphered += chr(newOrd)
    return ciphered

def generate_password():
    print("Password generated")
    return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(15)])

def create_password():
    password = input("Enter password: ")
    passwordAgain = input("Enter password again: ")
    if password != passwordAgain: 
        print("Passwords do not match, try again.")
        line()
        create_password()
    else: 
        print("Password created")
        return password

def main():
    file = open("PasswordManager\\data.json")
    data = json.load(file)

    line()
    print("\t\tPassword Manager")
    while True:
        line()
        print("1. Create new password"
            "\n2. Delete password"
            "\n3. View passwords"
            "\n4. Exit")
        action = input("Enter choice [1,2,3,4]: ")

        line()
        if action == "1":
            print("\t\tCreate new password")

            name = input("\nName of password: ")
            print("\n1. Create your own password"
                "\n2. Generate random password")
            choice = input("Enter choice [1,2]: ")
            line()
            if choice == "1":
                password = create_password()
            elif choice =="2":
                password = generate_password();
            data[encrypt(name)] = encrypt(password)
            with open ("PasswordManager\data.json",'w') as f: json.dump(data,f, indent=4)
        
        elif action == "2":
            print("\t\tDelete password")

            name = input("\nEnter password name: ")
            line()
            if encrypt(name) in data:
                del data[encrypt(name)]
                with open ("PasswordManager\data.json",'w') as f: json.dump(data,f, indent=4)
                print("Password deleted successfully")
            else: print("Password not found")
        
        elif action == "3":
            print("\t\tView Passwords")

            for key,value in data.items(): print(f"{decrypt(key)}: {decrypt(value)}")
        
        elif action == "4":
            print("Program will now close...")
            break

if __name__ == "__main__": main()