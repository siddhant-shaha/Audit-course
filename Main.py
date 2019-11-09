import re
st=[]
br=[]
div=[]
tm=[]
eid=[]
rn=[]

def create_record():
    a=False
    while a==False:
        student=input("Enter your name:\n")
        pattern=re.compile(r'[A-Za-z][a-z]+')
        match=pattern.finditer(student)
        count=0
        for i in match:
        
            count+=1 
            st.append(student)
            a=True
        if count==0:
            print("Invalid Name\n")
            
        a=False
        while a==False:     
            try:
                roll=int(input("Enter the roll of student :"))
            except (ValueError):
                print("enter valid credentials\n")
            else:
                rn.append(roll)
                a=True  
   
    a=False
    while a==False:
        branch=input("Enter your branch:\n")
        pattern=re.compile(r'[A-Za-z]+')
        match=pattern.finditer(branch)
        count=0
        for i in match:
        
            count+=1 
            br.append(branch)
            a=True
        if count==0:
            print("Invalid Branch\n")
    
    a=False
    while a==False:
        division=input("Enter the Division:\n")
        pattern=re.compile(r'[A-Za-z]')
        match=pattern.finditer(division)
        count=0
        for i in match:
        
            count+=1 
            div.append(division)
            a=True
        if count==0:
            print("Invalid Division\n")
            
    a=False
    while a==False:
    
        try:
            marks=list(map(int,input("Enter the marks of 5 subjects: ").split()))
        except ValueError:
            print("enter valid credentials\n")
            
        else:
            tm.append(marks[0]+marks[1]+marks[2]+marks[3]+marks[4])
            a=True
            print("\n")

    a=False
    while a==False:
        
        email_id=input("Enter your university email id\n")
        pattern=re.compile(r'(\w+)@somaiya.edu')
        match=pattern.finditer(email_id)
        count=0
        for i in match:
            eid.append(email_id)
            a=True
            count+=1
        if count==0:
            print("invalid id\n")
    
def display_all():
      print("NAME\tROLL\tBRANCH\tDIVISION\tMARKS\tEMAIL")   
      for i in range(len(st)):
          print(f"{st[i]}\t{rn[i]}\t{br[i]}\t{div[i]}\t\t{tm[i]}\t{eid[i]}\n")

def display(range):
    print("NAME\tROLL\tBRANCH\tDIVISION\tMARKS\tEMAIL")  
    print(f"{st[range]}\t{rn[range]}\t{br[range]}\t{div[range]}\t\t{tm[range]}\t{eid[range]}\n")
    
def remove():
    print("\n1. Remove using roll no. \n2. Remove using name \n3. Exit")
    n1 = int(input("Enter your choice: "))
    while(n1!=3):
         if n1==1:
             remove_roll()
         elif n1==2:
             remove_name()
         else:
             print("Invalid Choice")
         print("\n1. Remove using roll no. \n2. Remove using name \n3. Exit")
         n1 = int(input("Enter your choice: "))
         
def remove_roll():
    index=-1
    roll= int(input("Enter roll number: "))
    for i in range(len(rn)):
        if rn[i]==roll:
            index=i
    rn.remove(rn[index])
    st.remove(st[index])
    tm.remove(tm[index])
    eid.remove(eid[index])

def remove_name():
    name = input("Enter name: ")
    index=-1
    for i in range(len(st)):
        if st[i]==name:
            index=i
    rn.remove(rn[index])
    st.remove(st[index])
    tm.remove(tm[index])
    eid.remove(eid[index])    
            
def search():
    print("\n1. Search using roll no. \n2. Search using name \n3. Exit")
    n1 = int(input("Enter your choice: "))
    while(n1!=3):
         
        if n1==1:
            search_roll()
        elif n1==2:
            search_name()
        else:
            print("Invalid Choice")
        print("\n1. Search using roll no. \n2. Search using name \n3. Exit")
        n1 = int(input("Enter your choice: "))
             
def search_roll():
    index = -1
    roll = int(input("Enter roll: "))
    for i in range(0,len(rn)):
        if rn[i]==roll:
            index=i
    if index==-1:
        print("Search not found")
    else:
        print("Search found")
        display(index)

def search_name():
    index = -1
    name = input("Enter name: ")
    for i in range(0,len(st)):
        if st[i]==name:
            index=i
    if index==-1:
        print("Search not found")
    else:
        print("Search found")
        display(index)        
 
def update():
    roll = int(input("Enter roll no. of Student to edit data: "))
    index = -1
    for i in range(len(rn)):
        if rn[i]==roll:
            i = index
    print("1. update name \n2. branch \n3. update div \n4. update marks \n5. update email id \n6. exit ")  
    m = int(input("enter your choice: "))
    while m!=6: 
        if m==1:
            nname = input("enter new name: ")
            st[index]=nname
        elif m==2:
            nbranch = input("enter new branch of student: ")
            br[index]=nbranch 
        elif m==3:
            ndiv = input("enter new div: ")
            div[index]=ndiv
        elif m==4:
            nmarks = input("enter new marks: ")
            tm[index]=nmarks
        elif m==5:
            neid = input("enter new email id: ")
            eid[index]=neid
        print("\n1. update name \n2. branch \n3. update div \n4. update marks \n5. update email id \n6. exit ")  
        m = int(input("enter your choice: "))
         
print("""*****Student Management System*****""")
print("-----------------------------------------")
print("\n1. Display the list \n2. Insert New Student \n3. Remove Student data \n4. Update Student data \n5. Search Student data \n6. Exit")
n = int(input("Enter your choice: "))  
while(n!=6):
    if n==1:
        display_all()
    elif n==2:        
        create_record()
    elif n==3:
        remove()
    elif n==4:
        update()
    elif n==5:
        search()
    else:
        print("Invalid choice")
    print("---------------------------------------------------------------------")
    print("1. Display the list \n2. Insert New Student \n3. Remove Student data \n4. Update Student data \n5. Search Student data \n6. Exit")
    n = int(input("Enter your choice: "))

