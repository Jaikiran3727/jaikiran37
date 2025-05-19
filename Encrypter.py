import os
try:
    import cryptocode
except:
    os.system("pip install cryptocode")
    import cryptocode
while True:
    choice=int(input("""
1. Encrypt
2. Decrypt
3. Exit
Enter your choice: """))
    if choice==1:
        path=input("Enter path of the text file to encrypt: ")
        pwd=input("Enter the password to encrypt(3 or 4 small letters only): ")
        try:
            with open(path,"r") as file:
                data=file.read()
                data=cryptocode.encrypt(data,pwd)
            with open(path,"w") as file:
                file.write(data)
            input("File encrypted sucessfully!")
        except Exception as e:
            input(e)

    elif choice==2:
        path=input("Enter path of the text file to decrypt: ")
        pwd=input("Enter the password to decrypt: ")
        try:
            with open(path,"r") as file:
                data=file.read()
                trydata=cryptocode.decrypt(data,pwd)
                if trydata != False:
                    with open(path,"w") as file:
                        file.write(trydata)
                    input("File decrypted sucessfully!")
                else:
                    input("Wrong password! Or Empty file!")
        except Exception as e:
            input(e)

    else:
        print("Bye!")
        exit()
