import os
try:
    import cryptocode
except:
    os.system("pip install cryptocode")
    import cryptocode
import itertools
import time
while True:
    choice=int(input("""
    1. Bruteforce Attack
    2. Dictionary Attack
    3. Exit
    Enter your choice: """))

    if choice==1:
        def brute():
            global start,end
            path=input("Enter path of the encrypted file to Bruteforce: ")
            with open(path,"r") as file:
                data=file.read()
                x=1
                start=time.time()
                while x<=len("abcdefghijklmnopqrstuvwxyz"):
                    for i in itertools.product("abcdefghijklmnopqrstuvwxyz",repeat=x):
                        pwd="".join(i)
                        try:
                            print("Trying Password : ",pwd)
                            trydata=cryptocode.decrypt(data,pwd)
                            if trydata!=False:
                                print("Password Found, The pass is : ",pwd)
                                return
                        except:
                            pass
                    x+=1
                    end=time.time()
        brute()
        #min,sec=divmod(end-start,60)
        #input("Time Taken : "+str(int(min))+" min "+str(int(sec))+" sec")
        input("Time Taken : "+str(int(end-start))+" sec")

    elif choice==2:
        def dictionary():
            global s,e
            found=0
            path=input("Enter path of the encrypted file to Dictionary Attack: ")
            dpath=input("Enter path of the dictionary file: ")
            s=time.time()
            with open(path,"r") as file:
                data=file.read()
                with open(dpath,"r") as dict:
                    for i in dict:
                        i=i.strip()
                        try:
                            print("Trying Password : ",i)
                            trydata=cryptocode.decrypt(data,i)
                            if trydata!=False:
                                print("Password Found, The pass is :",i)
                                found=1
                                return
                        except:
                            pass
                if found==0:
                    print("Password Not Found in the Dictionary")
        dictionary()
        #min,sec=divmod(e-s,60)
        #input("Time Taken : "+str(int(min))+" min "+str(int(sec))+" sec")
        input("Time Taken : "+str(int(time.time()-s))+" sec")
    
    else:
        input("varata mame durrr!!")
        exit()
