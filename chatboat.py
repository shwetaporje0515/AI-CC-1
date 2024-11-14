class BankChatbot:
    def __init__(self):
        self.accounts = {'savings': 1000, 'checking': 500} # Initial account balances

    def display_menu(self):
        print("\nWelcome to Virtual Bank Chatbot")
        print("1. View Account Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def view_balance(self):
        print("\nAccount Balances:")
        for account, balance in self.accounts.items():
            print(f"{account.capitalize()}: ${balance}")

    def deposit_money(self, account, amount):
        self.accounts[account] += amount
        print(f"\n${amount} deposited into {account.capitalize()} account")

    def withdraw_money(self, account, amount):
        if self.accounts[account] >= amount:
            self.accounts[account] -= amount
            print(f"\n${amount} withdrawn from {account.capitalize()} account")
        else:
            print("Insufficient funds")

    def process_menu_selection(self, choice):
        if choice == '1':
            self.view_balance()
        elif choice == '2':
            account = input("Enter account type (savings/checking): ").lower()
            amount = float(input("Enter deposit amount: "))
            self.deposit_money(account, amount)
        elif choice == '3':
            account = input("Enter account type (savings/checking): ").lower()
            amount = float(input("Enter withdrawal amount: "))
            self.withdraw_money(account, amount)
        elif choice == '4':
            print("Thank you for banking with us!")
            return False
        else:
            print("Invalid choice. Please try again.")
        return True

if __name__ == "__main__":
    bank_bot = BankChatbot()
    while True:
        bank_bot.display_menu()
        user_choice = input("Enter your choice (1-4): ")
        if not bank_bot.process_menu_selection(user_choice):
            break


        