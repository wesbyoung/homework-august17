list1 = ["good","great","fine","nice"]
list2=["yes", "no"]


def takeaway_month(x,y):
    name=input("hey whats your name: ")
    first_answer=input(name + " , How are you? ")
    if first_answer in list1:
        print("great, lets work")
        third_answer=input("Can I ask you math problem? ")
    else:
            print("well...")
            print("go outside and relax")
            third_answer=input("Can I ask you math problem? ")
            if third_answer == "yes" or "okay":
                print("I'm going to add how many years you've been alive with the number of people youve dated")
                z= x + y
    print (z)


takeaway_month(3,4)




