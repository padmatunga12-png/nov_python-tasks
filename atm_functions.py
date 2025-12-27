balance = 0
def display_menu():
    print("\natm menu:")
    print("1.credit")
    print("2.debit")
    print("3.balance")
    print("4.exit")
def get_choice():
    return input("enter your choice(1-4):")
def credit():
    global balance
    try:
        amount = float(input("enter amount to credit:"))
        if amount <= 0:
            print("please enter a positive amount")
        else:
            balance += amount
            print(f"${amount} credited to your account")
    except:
        print(f"enter numerics positive numbers above 0")
def debit():
    global balance
    try:
        amount = float(input("enter amount to debit:"))
        if amount <= 0:
            print("please enter a positive amount")
        elif amount > balance:
            print("insufficient balance")
        else:
            balance -= amount
            print(f"${amount} debited from your account")
    except:
        print(f"please enter numerics")
def show_balance():
    print(f"your current balance is:${balance}")
def main():
    while True:
        display_menu()
        choice = get_choice()
    if choice == '1':
        credit()
    elif choice == '2':
        debit()
    elif choice == '3':
        show_balance()
    elif choice == '4':
        print("thank you for using the atm goodbye!")
        break
    else:
        print("invalid choice please try again")
main()
                                                