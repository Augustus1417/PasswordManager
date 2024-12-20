import random, string, json

def line(): 
    for x in range(50): print("-",end="")
    print()

def encrypt(message): 
    cipher = ""
    for x in message: cipher += chr(ord(x) + 5 )
    return cipher

def decrypt(cipher):
    ciphered = ""
    for x in cipher: ciphered += chr(ord(x) - 5 )
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
    file = open("data.json")
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
            line()
            name = input("\nName of password: ")
            print("\n1. Create your own password"
                "\n2. Generate random password")
            choice = input("Enter choice [1,2]: ")
            line()
            if choice == "1":
                password = create_password()
                data[encrypt(name)] = encrypt(password)
                with open ("data.json",'w') as f: json.dump(data,f, indent=4)
            elif choice =="2":
                password = generate_password();
                data[encrypt(name)] = encrypt(password)
                with open ("data.json",'w') as f: json.dump(data,f, indent=4)
            else: print("Error input")   
        
        elif action == "2":
            print("\t\tDelete password")
            line()
            name = input("\nEnter password name: ")
            line()
            if encrypt(name) in data:
                del data[encrypt(name)]
                with open ("data.json",'w') as f: json.dump(data,f, indent=4)
                print("Password deleted successfully")
            else: print("Password not found")
        
        elif action == "3":
            print("\t\tView Passwords")
            line()
            for key,value in data.items(): print(f"{decrypt(key)}: {decrypt(value)}")
        
        elif action == "4":
            print("Program will now close...")
            break

if __name__ == "__main__": main()