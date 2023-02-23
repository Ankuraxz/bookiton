import datetime
import uuid

# ['321', 1, UUID('4be4e495-d738-44f2-adac-59ab4e424cf4'), 5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
# uarr.update({usernamex: [usernamex, passwordx, bal, [1, x, y], b_owner, bidu, price,[],[]]})
#'john': ['321', 1, UUID('ce2e4207-a015-4b2e-a340-14a23e1d4a2a'), 5, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 5, 45,[],[]]

uarr=barr=admin={}
available_Business=[]
resell_business=[]
available_user=[]
transaction=[]
complaints=[]

class login:
    def __init__(self, username=None,password=None):
        self.username = username
        self.password = password

    def signin(self):
        print("ENTER TYPE OF USER")
        ux=int(input("Enter 0 for user, 1 for Buisness, 2 for Super Admin"))

        username = input("ENTER USERNAME: ").lower()
        password = input("ENTER PASSWORD: ")
        if ux==0:
            if username in uarr.keys() :
                if password== uarr[username][0]:
                    print("Login Success as User ")
                    return(username,password,ux)
                else:
                    print("Password is incorrect")
            else:
                print("Username is incorrect")
        elif ux==1:
            if username in barr.keys() :
                if password== barr[username][0]:
                    print("Login Success as Buisness ")
                    return(username,password,ux)
                else:
                    print("Password is incorrect")
            else:
                print("Username is incorrect")
        elif ux==2:
            if username in admin.keys() :
                if password== admin[username][0]:
                    print("Login Success as Admin ")
                    return(username,password,ux)
                else:
                    print("Password is incorrect")
            else:
                print("Username is incorrect")

class user(login):

    def __init__(self, username=None,password=None,message=[],notif=[],btypeu=None,sid=None,date=None,subscribe=None, bal=None):
        self.username = username
        self.password = password
        self.message = message
        self.notif = notif
        self.btype = btypeu
        self.sid = sid
        self.date = date
        self.subscribe = subscribe
        self.bal = bal
    def adder(self,uarr):
        uarr.update({self.username:[self.password]})
    def addvalue(self,uarr):
        uarr[self.username].append(self.btype)
        uarr[self.username].append(self.sid)
        uarr[self.username].append(self.date)
        uarr[self.username].append(self.subscribe)
        uarr[self.username].append(self.notif)
        uarr[self.username].append(self.message)




class buisness(login):
    def __init__(self, username=None,password=None,price=0,num_row=0,message=[],notif=[],btype=None,bid=0):
        self.username = username
        self.password = password
        self.price = price
        self.num_row = num_row
        self.message = message
        self.notif = notif
        self.btype =btype
    def adder(self,barr):
        barr.update({self.username:[self.password]})

    def addvalue(self,barr):
        barr[self.username].append(self.price)
        barr[self.username].append(self.num_row)
        barr[self.username].append(self.btype)
        barr[self.username].append(self.bid)
        barr[self.username].append(self.notif)
        barr[self.username].append(self.message)

    def buisness_select(self):

            print("Select Buisness")
            print("1. Restaurant")
            print("2. Cinema")
            print("3. Hotel")
            print("4. Train")
            print("5. Airplane")
            print("6. Exit")
            self.btype = int(input("Enter your choice: "))
            if buisness == 1:
                print("Restaurant")
                btypeu = 1
            elif buisness == 2:
                print("Cinema")
                btypeu = 2
            elif buisness == 3:
                print("Hotel")
                btypeu = 3
            elif buisness == 4:
                print("Train")
                btypeu = 4
            elif buisness == 5:
                print("Airplane")
                btypeu = 5
            elif buisness == 6:
                print("Exit")
                btypeu = None

    def create_seat_matrix(self):
        self.num_row = int(input(print("Enter Number of Rows , Atleast 4")))
        if num_row > 3:
            matrix = [[0] * num_row for _ in range(num_row)]

            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
            barr[self.username].append(num_row)
            barr[self.username].append(matrix)

    def price_select(self, matrix):
        if len(matrix) > 3:
            self.price = int(input(print("Enter the base price")))
            barr[self.username].append(self.num_row)
            barr[self.username].append(self.price)
            barr[self.username].append([])  # Notificaiton
            barr[self.username].append([])  # Message


class adminuser(login):

    def __init__(self, username=None,password=None,complaint=[],transaction=[]):
        self.username = username
        self.password = password
        self.complaint = complaint
        self.transaction = transaction

    def adder(self,admin):
        admin.update({self.username:[self.password]})

    def addvalue(self,admin):
        admin[self.username].append(self.complaint)
        admin[self.username].append(self.transaction)


def signin():
    print("ENTER TYPE OF USER")
    ux=int(input("Enter 0 for user, 1 for Buisness, 2 for Super Admin"))

    username = input("ENTER USERNAME: ").lower()
    password = input("ENTER PASSWORD: ")
    if ux==0:
        if username in uarr.keys() :
            if password== uarr[username][0]:
                print("Login Success as User ")
                return(username,password,ux)
            else:
                print("Password is incorrect")
        else:
            print("Username doesn't exist")

    elif ux==1:
        if username in barr.keys():
            if password == barr[username][0]:
                print("Login Success as Buisness")
                return (username, password, ux)
            else:
                print("Password is incorrect")
        else:
            print("Username doesn't exist")

    elif ux==2:
        if username in admin.keys():
            if password == admin[username][0]:
                print("Login Success as Admin")
                return (username, password, ux)
            else:
                print("Password is incorrect")


def buisness_select(usernamex):
    print("Select Buisness")
    print("1. Restaurant")
    print("2. Cinema")
    print("3. Hotel")
    print("4. Train")
    print("5. Airplane")
    print("6. Exit")
    buisness = int(input("Enter your choice: "))
    if buisness == 1:
        print("Restaurant")
        btype=1
    elif buisness == 2:
        print("Cinema")
        btype=2
    elif buisness == 3:
        print("Hotel")
        btype=3
    elif buisness == 4:
        print("Train")
        btype=4
    elif buisness == 5:
        print("Airplane")
        btype=5
    elif buisness == 6:
        print("Exit")
        btype=None
        return [btype, 0]
    else:
        print("Invalid Choice")
        btype=None
        return [btype,0]
    if btype!=None:
        # available_Business.append([usernamex,btype])
        bid = uuid.uuid4()
        barr[usernamex].append(btype)
        barr[usernamex].append(bid)


        return [btype,bid]

def create_seat_matrix(usernamex):
    num_row = int(input(print("Enter Number of Rows , Atleast 4")))
    if num_row>3:
        matrix = [[0]*num_row for _ in range(num_row)]

        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
        barr[usernamex].append(num_row)
        barr[usernamex].append(matrix)


        return [matrix,num_row]
    else:
        print("Add more rows")
        return [None,None]
        pass

def price_select(usernamex,matrix):
    if len(matrix)>3:
        price = int(input(print("Enter the base price")))
        barr[usernamex].append(num_row)
        barr[usernamex].append(price)
        barr[usernamex].append([]) #Notificaiton
        barr[usernamex].append([]) #Message
        return price


    else:
        print("Add more rows")
        return None
        pass

def buisness_selectu(usernamex):
    print("Select Buisness")
    print("1. Restaurant")
    print("2. Cinema")
    print("3. Hotel")
    print("4. Train")
    print("5. Airplane")
    print("6. Exit")
    buisness = int(input("Enter your choice: "))
    if buisness == 1:
        print("Restaurant")
        btypeu=1
    elif buisness == 2:
        print("Cinema")
        btypeu=2
    elif buisness == 3:
        print("Hotel")
        btypeu=3
    elif buisness == 4:
        print("Train")
        btypeu=4
    elif buisness == 5:
        print("Airplane")
        btypeu=5
    elif buisness == 6:
        print("Exit")
        btypeu=None
        return btypeu
    else:
        print("Invalid Choice")
        btypeu = None
        return [btypeu, 0]
    uarr[usernamex].append(btypeu)
    return btypeu

def buisness_id_selectu(usernamex,b_typeu):
    final_available_Business=[]
    print("Select Fresh seat (0) or Resell seat (1)")
    ss = int(input("Enter your choice: "))
    if ss == 0:
        for i in available_Business:
            if i[1] == b_typeu:
                final_available_Business.append(i)
        title ="Select Buisness \n Buisness owner Name, Buisness Type, Buisness ID, Number of Seats,  Base Price"
        if len(final_available_Business)>=1:
            #print("Choose a Business From the List below \n")
            print(final_available_Business, sep = '\n')
            #p = len(final_available_Business)
            p = int(input("Choose a Business From the List above \n"))
            print("SELECTED BUSINESS IS", final_available_Business[p])

            d = final_available_Business[p]
            d.append(ss)
            # new print("selected Business is", final_available_Business[p])

           #= b = enquiries.choose("Choose a Buisness",final_available_Business)
            # b = pick(final_available_Business, 'Select Buisness', indicator='=>', min_selection_count=1 )
           #= print(b)
            # Functionality of Conformation of selection
            return d
        else:
            print("No Buisness Available")
            return None
    elif ss == 1 and len(resell_business)>0:
        for i in resell_business:
            if i[1] == b_typeu:
                final_available_Business.append(i)
        title ="Select Buisness \n Buisness owner Name, Buisness Type, Buisness ID, Number of Seats,  Base Price"
        if len(final_available_Business)>=1:
            #print("Choose a Business From the List below \n")
            print(final_available_Business, sep = '\n')
            #p = len(final_available_Business)
            p = int(input("Choose a Business From the List above \n"))
            print("SELECTED BUSINESS IS", final_available_Business[p])

            d = final_available_Business[p]

            # new print("selected Business is", final_available_Business[p])

           #= b = enquiries.choose("Choose a Buisness",final_available_Business)
            # b = pick(final_available_Business, 'Select Buisness', indicator='=>', min_selection_count=1 )
           #= print(b)
            # Functionality of Conformation of selection
            d.append(ss)
            return d






def price_cal(usernamex,b_price,b_matrix,x,y):
    #X  - Row, Y - Column
    if x ==0 :
        return 2*b_price
    elif x==len(b_matrix)-1:
        return (3/4)*b_price
    elif y == len(b_matrix)//2 or y == len(b_matrix)//2+1:
        return (5/4)*b_price
    else:
        return b_price




if __name__ == "__main__":


    mudit = garv = ankur = kisha = muskan = user()
    mudit.username = "mudit"
    mudit.password = "123"
    mudit.adder(uarr)
    garv.username = "garv"
    garv.password = "123"
    garv.adder(uarr)
    kisha.username = "kisha"
    kisha.password = "123"
    kisha.adder(uarr)
    muskan.username = "muskan"
    muskan.password = "123"
    muskan.adder(uarr)
    ankur.username = "ankur"
    ankur.password = "123"
    ankur.adder(uarr)

    john = jack = julie = lily = mahesh = buisness()
    john.username = "john"
    john.password = "321"
    john.adder(barr)
    jack.username = "john"
    jack.password = "321"
    jack.adder(barr)
    julie.username = "julie"
    julie.password = "321"
    julie.adder(barr)
    lily.username = "lily"
    lily.password = "321"
    lily.adder(barr)
    mahesh.username = "mahesh"
    mahesh.password = "321"
    mahesh.adder(barr)

    xyz = adminuser()
    xyz.username = "admin"
    xyz.password = "admin"
    xyz.adder(admin)


## Code starts here
while True:
    details = list(signin())
    usernamex = details[0]
    passwordx = details[1]
    user_typex = details[2]
    # print(details)
    if user_typex == 1:
    ## Buisness Options
        print("Welcome "+ usernamex)
        choice=0
        while choice != 5:
            print("press 1 to Enter Business \n, 2 for Messages \n, 3 for Notifications \n, 4 for Price change \n, 5 for Exit \n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                b = buisness_select(usernamex)
                btype = b[0]
                if btype == None:
                    break
                else:
                    bid = b[1]
                    res = create_seat_matrix(usernamex)
                    matrix=res[0]
                    num_row=res[1]
                    price = price_select(usernamex,matrix)
                    available_Business.append([usernamex,btype,bid,(int(num_row)**2),price])


            elif choice==2:
                message = barr.get(usernamex)[8]
                if len(message)>0:
                    print("Messages are: ", message, sep = '\n')
                else:
                    print("No Messages")


            elif choice==3:
                notification = barr.get(usernamex)[7]
                if len(notification)>0:
                    print("Notifications are: ", notification, sep = '\n')
                else:
                    print("No Notifications")


            elif choice==4 and barr.get(usernamex)[3]!=None:
                matrix = barr.get(usernamex)[4]
                price = price_select(usernamex, matrix)
                barr[usernamex][6] = price




        # print(available_Business)

        # matrix[0][0]=1
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

    elif user_typex == 0:
        # For user
        uarr.update({usernamex: [usernamex, passwordx, 10000, [0, None, None], None, None, None,[],[]]})
        bal = uarr.get(usernamex)[2]

        print("Welcome " + usernamex)


        user_choice = 1
        while user_choice != 5:
            print("press 1 for seat reservation \n, 2 for Cancellation \n, 3 for Change \n, 4 for Resell \n, 5 for Exit \n, 6 for Notifications & Seat Status \n, 7 for Your Messages \n, 8 to send Message \n 9 to complaint")
            user_choice = int(input("Enter your choice \n"))
            if user_choice == 1:
                if uarr.get(usernamex)[3][0]==0: # If new user or no seat booked already
                    # Select available business
                    b_typeu = buisness_selectu(usernamex)
                    if b_typeu == None:
                        user_choice=5
                        break
                    else:
                        b= buisness_id_selectu(usernamex,b_typeu)
                        bidu=b[2]
                        status = b[-1]
                        b_type = b[1]
                        b_owner = b[0]

                        if status == 1:
                            #RESELL PROCESS
                            uarr[b_owner][3][0] = 0
                            b_price = b[4]

                            if bal>b_price:
                                uarr[b_owner][2]+=b_price
                                uarr[usernamex][2]-=b_price
                                x = uarr[b_owner][3][1]
                                y = uarr[b_owner][3][2]
                                uarr[b_owner][3][1]= None

                                uarr[b_owner][3][2]= None
                                print("Seat Booked Successfully")
                                print("Seat Number is",x,y)
                                transaction.append([usernamex, b_owner, b_price, [x, y], datetime.datetime.now()])
                                notif = uarr.get(usernamex)[7]

                                uarr.update({usernamex: [usernamex, passwordx, bal, [1, x, y], b_owner, bidu, b_price,[],[]]})
                                notif.append("Seat Booked Successfully" + str([x, y]))
                                uarr[usernamex][7] = notif
                                #MESSAGE TO BUSSINESS OWNER



                        elif status == 0:
                            b_num_seat = b[3]
                            b_price = b[4]
                            status = b[5]
                            b_matrix = barr.get(b_owner)[4]
                            b_rows = barr.get(b_owner)[5]
                            b_price = barr.get(b_owner)[6]
                            # print("Barr",barr)
                            print("Selection Made, Please enter seat number of the seat matrix as Column Num, Row Num \n")
                            print("Seats Available \n",b_num_seat)
                            print("Rows & Column Available \n",b_num_seat**(1/2))


                            # print(b_matrix)
                            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b_matrix]))
                            try:
                                s = list(map(int,input("Enter the Comma Seperated seat number: ").split(",")))
                                x = s[0]-1
                                y = s[1]-1

                            except ValueError:
                                print("Invalid Input")
                                break
                            if x>b_rows or y>b_rows or x<0 or y<0:
                                print("Invalid Input")
                                break

                            if b_matrix[x][y] == 0:
                                price = price_cal(usernamex,b_price,b_matrix,x,y)
                                if bal>price:
                                    print("Price is ",price)
                                    print("Effective Available Balance is ",bal-price)
                                    b_matrix[x][y] = 1
                                    barr[b_owner][4] = b_matrix
                                    print("Seat Booked")
                                    transaction.append([usernamex, b_owner, price, [x, y], datetime.datetime.now()])
                                    notif = uarr.get(usernamex)[7]
                                    notif.append("Seat Booked" + str([x, y]))

                                    uarr.update({usernamex: [usernamex, passwordx, bal, [1, x, y], b_owner, bidu, price,[],[]]})
                                    uarr[usernamex][7] = notif
                                    notifb = barr.get(b_owner)[7]
                                    notifb.append("Seat Booked" + str([x, y]))
                                    barr[b_owner][7] = notifb
                                    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b_matrix]))
                                else:
                                    print("Insufficient Balance")
                                    break
                            else:
                                print("Seat Already Booked")
                                break





                               # k = input(str(print('\n'"Do you want to Cancel the seat number YES / NO")))
                                #if k == "YES":
                                 #   b_matrix[x][y] = 1





            elif user_choice == 2 and uarr.get(usernamex)[3][0]==1: # Seat already booked
                print("Seat Cancelled, No money is returned, you can proceed for new booking")
                b_owner = uarr.get(usernamex)[4]
                b_matrix = barr.get(b_owner)[4]
                x = uarr.get(usernamex)[3][1]
                y = uarr.get(usernamex)[3][2]
                # b_owner = uarr.get(usernam
                bal = uarr.get(usernamex)[2]
                b_matrix = barr.get(b_owner)[4]
                # b_rows = barr.get(b_owner)[5]
                # b_price = barr.get(b_owner)[6]

                # x = uarr.get(usernamex)[3][1]
                # y = uarr.get(usernamex)[3][2]
                b_matrix[x][y] = 0
                barr[b_owner][4] = b_matrix
                uarr[usernamex][3][0] = 0
                notifb = barr.get(b_owner)[7]
                notifb.append("Seat Cancelled" + str([x, y]))
                barr[b_owner][7] = notifb
                notif = uarr.get(usernamex)[7]
                notif.append("Seat Cancelled" + str([x, y]))

                uarr.update({usernamex: [usernamex, passwordx, bal, [0, None, None], None, None, None, [], []]})
                uarr[usernamex][7] = notif


            elif user_choice == 3 and uarr.get(usernamex)[3][0]==1: # Seat already booked
                print("Seat Change")
                b_owner = uarr.get(usernamex)[4]
                bal = uarr.get(usernamex)[2]
                b_matrix = barr.get(b_owner)[4]
                b_rows = barr.get(b_owner)[5]
                b_price = barr.get(b_owner)[6]

                x = uarr.get(usernamex)[3][1]
                y = uarr.get(usernamex)[3][2]

                print("Current Seat is ",x+1,",",y+1)
                print("Enter new seat number")
                try:
                    s = list(map(int,input("Enter the Comma Seperated seat number: ").split(",")))
                    x1 = s[0]-1
                    y1 = s[1]-1


                except ValueError:
                    print("Invalid Input")
                    break
                if x1>b_rows or y1>b_rows or x1<0 or y1<0:
                    print("Invalid Input")
                    break

                if b_matrix[x1][y1] == 0:
                    price = price_cal(usernamex, b_price, b_matrix, x1, y1)
                    if bal > price:
                        print("Price is ", price)
                        print("Effective Available Balance is ", bal - price)
                        b_matrix[x1][y1] = 1
                        b_matrix[x][y] = 0 # Old seats Unbooked
                        notif = uarr.get(usernamex)[7]
                        notif.append("Seat Changed" + str([x, y]))

                        uarr.update({usernamex: [usernamex, passwordx, bal, [1, x1, y1], b_owner, bidu, price,[],[]]})
                        uarr[usernamex][7] = notif
                        transaction.append([usernamex, b_owner, price, [x1, y1], datetime.datetime.now()])

                        barr[b_owner][4] = b_matrix
                        print("Seat Booked")
                        notifb = barr.get(b_owner)[7]
                        notifb.append("Seat Changed" + str([x1, y1]))
                        barr[b_owner][7] = notifb
                        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in b_matrix]))



                    else:
                        print("Insufficient Balance")
                        break
                else:
                    print("Seat Already Booked")
                    break

                # uarr.update({usernamex: [usernamex, passwordx, bal, [1, x, y], b_owner, bidu, price,[],[]]})

            elif user_choice == 4 and uarr.get(usernamex)[3][0]==1: # Seat already booked
                print("Seat Resell")
                x=uarr.get(usernamex)[3][1]
                y=uarr.get(usernamex)[3][2]
                price = uarr.get(usernamex)[6]
                bal = uarr.get(usernamex)[2]
                b_owner = uarr.get(usernamex)[4]
                b_matrix = barr.get(b_owner)[4]
                btype= barr.get(b_owner)[1]
                print("Are you sure you want to resell the seat, press Y to confirm")
                k = input()
                if k == "Y":
                    b = buisness_select(usernamex)
                    btype = b[0]
                    if btype == None:
                        break
                    else:
                        bid = b[1]

                        price = int(input("Original Price is "+str(price)+" Enter the new price: "))
                        if price < 0:
                            print("Invalid Price")
                            break
                        else:
                            notif = uarr.get(usernamex)[7]
                            notif.append("Seat Resell request Accepted" + str([x, y]))
                            uarr[usernamex][7] = notif



                            resell_business.append([usernamex, btype, bid, [x,y], price])
                            print("Seat Resell Requested")

            elif user_choice==6 :
                ix = int(input("Enter 1 for Seat Status, 2 for all notifications"))
                if ix==2:
                    print("Your Notifications are: ")
                    notif = uarr.get(usernamex)[7]
                    if len(notif)==0:
                        print("No Notifications")
                    else:
                        print(notif,sep="\n")
                elif ix==1:
                    print("Your Seat Status is: ")
                    seat = uarr.get(usernamex)[3]

                    if seat[0]==0:
                        print("No Seat Booked")
                    else:
                        print("Seat Booked at "+ str(seat[1]+1,",",seat[2]+1))

            elif user_choice==7 :
                print("Your Messages are: ")
                message = barr.get(usernamex)[8]
                if len(message)==0:
                    print("No Messages")
                else:
                    print(message,sep="\n")

            elif user_choice==8 and uarr.get(usernamex)[3][0]==1:
                b_owner = uarr.get(usernamex)[4]
                msg = str(input("Enter your Message for the Business Owner"+str(b_owner)))
                barr[b_owner][8].append(msg)

            elif user_choice==9:
                complaint = str(input("Enter your Complaint"))
                complaints.append([usernamex,complaint,datetime.datetime.now()])


    elif user_typex ==2:
        print("Welcome Admin")
        user_choice=0
        while user_choice!=4:
            print("Welcome", usernamex)
            print("1. View Complaints")
            print("2. View Transactions")
            print("3. View All users and Remove")
            print("3. Exit")
            user_choice = int(input())
            if user_choice == 1:
                print("Complaints are: ")
                print(complaints,sep="\n")
            elif user_choice == 2:
                print(transaction,sep="\n")
            elif user_choice == 3:
                print("Print 1 for User, 2 for Business")
                ix = int(input())
                if ix==1:
                    for i,j in enumerate(uarr):
                        print(i,j)
                    print("Enter the index of the user to be removed")
                    ij = int(input())
                    uarr.pop(list(uarr.keys())[ij])

                elif ix==2:
                    for i,j in enumerate(barr):
                        print(i,j)
                    print("Enter the index of the user to be removed")
                    ij = int(input())
                    barr.pop(list(barr.keys())[ij])

            elif user_choice == 4:
                break
            else:
                print("Invalid Input")
                break

























