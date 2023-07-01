def funct(file):
    f= open(file,"+a")
    rollnumber=input("enter your roll number :\n")
    name=input("enter your name :\n")
    class_=input("enter your class \n:")
    
    f.writelines([f"Roll No.: {rollnumber},",f" Name: {name},",f" Class: {class_}"])
    f.seek(0)
    print(f.readlines())

file=input("enter file name and add txt ")
funct(file)
