#Railway Ticket

while True:
    ticket = int(input("Enter the ticket price"))
    def railway():
        global price
        price=0
        dis = 0
        gender = input("Select one option male/female").lower()
        age = int(input("Enter the age"))
        if gender == "Male":
            if age>=60:
                dis = ticket * (30/100)
            else:
                dis = 0
        else:
            if age>=60:
                dis = ticket * (50/100)
            else:
                dis = ticket * (30/100)

        
        price = ticket - dis

    railway()
    print("Ticket price is",price)
            
