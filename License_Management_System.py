import random
from datetime import datetime, timedelta

class UserDetails:
    def __init__(self):
        self.users = {}
        self.passwords = {}
        self.dates = {}
        self.licenses = {}

    def create(self):
        customer_id = random.randint(112233, 999876)
        print(f"{customer_id} is your customer ID")
        username = input("Enter customer name: ")
        self.users[customer_id] = username
        password = input("Enter the password: ")
        self.passwords[customer_id] = password

        curr_date = datetime.now()
        print("1. 3 months = 299/-\n2. 6 months = 549/-\n3. 1 year = 999/-")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Successfully activated for 3 months")
            expiry_date = curr_date + timedelta(days=90)
            product_id = "product_3months"
        elif choice == 2:
            print("Successfully activated for 6 months")
            expiry_date = curr_date + timedelta(days=182)
            product_id = "product_6months"
        elif choice == 3:
            print("Successfully activated for 1 year")
            expiry_date = curr_date + timedelta(days=365)
            product_id = "product_1year"
        else:
            print("Invalid choice")
            return

        print(f"Your product ID is: {product_id}")
        print(f"Registered date: {curr_date}")
        print(f"Expiring on: {expiry_date}")

        self.dates[customer_id] = expiry_date
        license_id = random.randint(100, 999)
        print(f"{license_id} is your license ID")
        self.licenses[license_id] = customer_id  # Mapping license ID to customer ID

    def lic_activation(self):
        license_id = int(input("Enter the license ID: "))
        password = input("Enter the password: ")

        if license_id in self.licenses:
            customer_id = self.licenses[license_id]
            if self.passwords.get(customer_id) == password:
                curr_date = datetime.now()
                if curr_date < self.dates.get(customer_id, curr_date):
                    print("Valid")
                else:
                    print("Not valid")
            else:
                print("Incorrect password")
        else:
            print("No such license ID... try again!!")

    def display(self):
        if not self.users:
            print("No licenses")
            return

        for customer_id, username in self.users.items():
            expiry_date = self.dates.get(customer_id, "No expiry date")
            license_id = next((lid for lid, cid in self.licenses.items() if cid == customer_id), "No license ID")
            formatted_expiry_date = expiry_date.strftime("%d-%m-%Y") if isinstance(expiry_date, datetime) else expiry_date
            print(f"Customer ID: {customer_id}, Username: {username}, License ID: {license_id}, Expiry Date: {formatted_expiry_date}")

    def renew(self):
        license_id = int(input("Enter the license ID for license renewal: "))
        if license_id in self.licenses:
            customer_id = self.licenses[license_id]
            curr_date = datetime.now()
            expiry_date = self.dates.get(customer_id)

            if curr_date < expiry_date:
                print("Renewing license...")
                print("1. 3 months = 299/-\n2. 6 months = 549/-\n3. 1 year = 999/-")
                renewal_choice = int(input("Enter your renewal choice: "))

                if renewal_choice == 1:
                    print("Successfully renewed for 3 months")
                    new_expiry_date = expiry_date + timedelta(days=90)
                elif renewal_choice == 2:
                    print("Successfully renewed for 6 months")
                    new_expiry_date = expiry_date + timedelta(days=182)
                elif renewal_choice == 3:
                    print("Successfully renewed for 1 year")
                    new_expiry_date = expiry_date + timedelta(days=365)
                else:
                    print("Invalid renewal choice")
                    return

                print(f"Expiring on: {new_expiry_date}")
                self.dates[customer_id] = new_expiry_date
            else:
                print("License has expired. Renewal not possible.")
        else:
            print(f"No record found for license ID: {license_id}")

    def check_expired_licenses(self, month, year):
        expired_count = 0
        active_count = 0
        for customer_id, expiry_date in self.dates.items():
            if expiry_date.month == month and expiry_date.year == year:
                if datetime.now() > expiry_date:
                    expired_count += 1
                else:
                    active_count += 1

        print(f"Active licenses in {month}/{year}: {active_count}")
        print(f"Expired licenses in {month}/{year}: {expired_count}")

# Main program
sys = UserDetails()
while True:
    print("Enter your choice:")
    choice = int(input("1. Create\n2. Check license activation\n3. Display\n4. Renew license\n5. Check expiries\n6. Exit\n"))
    if choice == 1:
        sys.create()
    elif choice == 2:
        sys.lic_activation()
    elif choice == 3:
        sys.display()
    elif choice == 4:
        sys.renew()
    elif choice == 5:
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))
        sys.check_expired_licenses(month, year)
    elif choice == 6:
        break
    else:
        print("Invalid choice, please try again.")
