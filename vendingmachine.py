        
choice_1={
    "1" : 40,
    "2" : 20,
    "3" : 30,
    "4" : 15,
}
choice_2={
    "1" : "coke",
    "2" : "chips",
    "3" : "choclate",
    "4" : "Water",
}
def check_money(user_input,user_amount):
    correct_price = choice_1[user_input]
    correct_product = choice_2[user_input]
    if  user_amount < correct_price:
        print("Entered wrong amount")
    else:
        print("picking your snack ....")
        balance=user_amount-correct_price
        print(f"here is your change ${balance}")
        print(f"Enjoy your {correct_product} ")
def main():
    is_running=True
    while is_running:
        print("-------------------------------------------------------------")
        print(" 1. Coke      ₹40 \n",
              "2. Chips     ₹20\n",
              "3. Chocolate ₹30\n",
              "4. Water     ₹15\n",
              "5.Exit" )
        print("-------------------------------------------------------------")

        user_input=input("Select your choice :").strip()
        if not user_input == "5":
                    
            if  user_input not in choice_1:
                print("invalid choice")
            
            try:
                user_amount=int(input("Enter your amount:").strip())
            except ValueError:
                print("Please enter a valid number for the amount.")
                continue
            check_money(user_input,user_amount)

        else:
            print("OK exitting the vending machine ")
            is_running=False


if __name__ == "__main__":
    main()
