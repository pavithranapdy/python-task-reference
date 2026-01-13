# # class Person:
# #     def _init_(self, name, age):
# #         self.name = name          # public variable -Can be accessed from outside the class
# #         self.__age = age          # private variable - Python protects it using name mangling

# #     def show_age(self):            # Public method to access Private Data
# #         return self.__age           # accessing Private Data inside the class is allowed

# #     def set_age(self, age):               # setter method
# #         if age < 0:
# #             raise ValueError("Age cannot be negative")
# #         self.__age = age

# # p = Person("Alice", 25)

# # print(p.name)        # Allowed
# # print(p.show_age()) # Allowed
# # # print(p.__age)      # Error (private variable)

# # p.set_age(-30)
# # print(p.show_age())

# # print(p.name)        # Allowed
# # print(p.show_age()) # Allowed

# class BankAccount:
#     def _init_(self, holder, balance):
#         self.holder = holder        # public
#         self._bank_code = "SBI001"  # protected
#         self.__balance = balance    # private

#     def get_balance(self):          # public method
#         return self.__balance

#     def set_balance(self, amount):  # setter
#         if amount < 0:
#             raise ValueError("Invalid balance")
#         self.__balance = amount

# acc = BankAccount("Alice", 5000)

# print(acc.holder)        # ✅ public
# print(acc.get_balance()) # ✅ controlled access

# print(acc._bank_code)    # ⚠️ not recommended
# print(acc.__balance)    # ❌ error


class BankAccount:
    def _init_(self, account_holder, balance):
        self.account_holder = account_holder
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = balance          # private variable

    def get_balance(self):                # getter
        return self.__balance

    def deposit(self, amount):            # setter-like method
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        
acc = BankAccount("Alice", 5000)

print(acc.get_balance())   # 5000

acc.deposit(2000)
print(acc.get_balance())   # 7000

acc.withdraw(3000)
print(acc.get_balance())   # 4000