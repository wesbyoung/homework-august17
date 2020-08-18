list1 = ["good","great","fine","nice"]
list2=["yes", "no"]


name=input("hey whats your name: ")
first_answer=input(name + " , How are you? ")
if first_answer in list1:
    print("great, lets work")
    third_answer=input("Can I ask you math problem? ")
    if third_answer == "yes":
            print("I'm going to add how many years you've been alive with the number of people youve dated")
            print("okay")
            print("are you ready? ")
            x = int(input("how old are you? "))
            y = int(input("how many people have you dated "))
            if (x+y)> (x+2):
                print(x+y)
            if (x+y)==(x+2):
                print("Wholesome..I like it.. " + (x+y))
            if (x+y)< (x+2):
                print("That's sad")

else:
        print("well...")
        print("go outside and relax")
        third_answer=input("Can I ask you math problem? ")
        if third_answer == "yes":
            print("I'm going to add how many years you've been alive with the number of people youve dated")
            print("okay")
            print("are you ready? ")
            x = int(input("how old are you? "))
            y = int(input("how many people have you date "))
            if (x+y)> (x+2):
                print(x+y)
            if (x+y)==(x+2):
                print("Wholesome..I like it.. " + (x+y))
            else:
                print("That's sad")

                
                
                
            
