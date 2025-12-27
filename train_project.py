class train():
    def __init__(self,train_num,source,destination,seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats
    def display_info(self):
        print(f"train number: {self.train_num}")
        print(f"source: {self.source}")
        print(f"destination: {self.destination}")
        print(f"available seats: {self.seats}")
        print()
    def book_tickets(self,num_tickets):
        if num_tickets > self.seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000,999999))
                self.seats -= num_tickets
                return pnr_list
class passenger:
    def __init__(self,name,age,gender,phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
    def display_info(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"phone number: {self.phone}")
class ticket:
    def __init__(self,train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
    def display_info(self):
        print(f"train number: {self.train.train_num}")
        print(f"source: {self.source}")
        print(f"destination: {self.destination}")
        print(f"pnr: {self.pnr}")
        for passengers in self.passengers:
            passenger.display_info()
            print()
class account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def check_password(self,password):
        return self.password == password
    accounts = [account("user1", "password1"), account("user2", "password2")]
    logged_in_account = None
    print("\n1. create an account\n2. login\n")
    choice = input("enter choice:")
    if choice == '1':
        username = input("enter username:")
        password = input("enter password:")
        accounts.append(account(username,password))
        print("Account created successfully!")
    elif choice == '2':
        username = input("enter username:")
        password = input("enter password:")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
            if logged_in_account is None:
                print("invalid username or password")
            else:
                print(f"\nlogged in as {logged_in_account.username}\n\n-----available train details-----\n")
                break
        else:
            print("invalid choice")
            if logged_in_account is not None:
                train = [train("23457", "kadapa", "raychoti", 40),
                         train("34567", "raychoti", "madanapalli", 50),
                         train("45678", "kadapa", "delhi", 1)]
                for train in trains:
                    train.display_info()
                    while True:
                        try:
                            train_num = input("enter train number:")
                            num_tickets = int(input("enter number of tickets:"))
                            if num_tickets <= 0:
                                raise ValueError("number of tickets should be greater than 0")
                            for train in trains:
                                if train.train_num == train_num:
                                    if num_tickets > train.seats:
                                        raise ValueError("selected more tickets than available seats")
                                    break
                                else:
                                    raise ValueError("invalid train number")
                                break
                        except ValueError as e:
                            print(f"invalid input: {e}")
                            train = None
                            for t in trains:
                                if t.train_num == train_num:
                                    train = t
                                    break
                                if train is None:
                                    print("invalid train number")
                                else:
                                    passengers = []
                                    for i in range(num_tickets):
                                        print(f"\nenter details for passenger {i+1}:")
                                        while True:
                                            try:
                                                name = input("name:")
                                                if not name:
                                                    raise ValueError("name cannot be empty")
                                                age = int(input("age:"))
                                                if age <=0 or age > 120:
                                                    raise ValueError("invalid age")
                                                gender = input("gender:")
                                                phone = input("phone number:")
                                                if not phone or len(phone) !=10 or not phone.isdigit():
                                                    raise ValueError("invalid phone number")
                                                passenger = passenger(name,age,gender,phone)
                                                passengers.append(passenger)
                                                break
                                            except ValueError as e:
                                                print(f"invalid input: {e}")
                                                pnr_list = train.book_tickets(num_tickets)
                                                if pnr_list is None:
                                                    print("tickets not available")
                                                else:
                                                    print("\n---------booking successful!-------\n\nyour ticket details: \n")
                                                    for i in range(num_tickets):
                                                        ticket = ticket(train,train.source,train.destination,[passengers[i]], pnr_list[i])
                                                        ticket.display_info()
                                                        print("\n-------thank you-------\n-----safe journey------")                            
                                            