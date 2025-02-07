tasklist=[]
while True:
    try:
        print("-----MENU-----")
        print("1-ADD TASK")
        print("2-VIEW TASKS")
        print("3-DELETE A TASK")
        print("4-EXİT")
        secim=int(input("Please specify the action you will take:"))
        if secim<1 or secim>4:
             print("Please enter a valid value!")
        
        if secim==1:
            gorev=input("Please specify the task you will add:")
            tasklist.append(gorev)
        if secim==2:
            j=1
            if tasklist==False:
                print("LIST İS EMPTY..")
            else:
                for gorev in tasklist:
                    
                    print(f"{j}.{gorev}")
                    j+=1
        if secim==3:
            j=1
            for gorev in tasklist:
                    
                    print(f"{j}.{gorev}")
                    j+=1
            silme=int(input("Please specify the number of the task you want to delete."))
            if silme<1 or silme>j-1:
                print("Please specify the task you will add:")
            
            tasklist.pop(silme-1)
        if secim==4:
             print("exiting the program...")
    except ValueError:
         print("Please enter a valid value!")
                    
                    