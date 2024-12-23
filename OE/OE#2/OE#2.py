class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price:.2f}"

    def update_property(self, property_name, value):
        if hasattr(self, property_name):
            setattr(self, property_name, value)
        else:
            print("Property does not exist.")

def main_menu():
    phones = []
    while True:
        print("\nMain Menu:\n1. Add Phone\n2. Modify Phone\n3. Delete Phone\n4. Display Phones\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            brand = input("Enter phone brand: ")
            model = input("Enter phone model: ")
            price = float(input("Enter phone price: "))
            phones.append(Phone(brand, model, price))
            print("Phone added successfully!")

        elif choice in ['2', '3']:
            if not phones:
                print("No phones to modify/delete.")
                continue
            
            for i, phone in enumerate(phones, start=1):
                print(f"{i}. {phone.display_info()}")

            index = int(input("Select phone by number: ")) - 1
            if 0 <= index < len(phones):
                phone = phones[index]
                if choice == '2':
                    property_name = input("Enter property name to modify (brand/model/price): ")
                    new_value = input(f"Enter new value for {property_name}: ")
                    if property_name == "price":
                        new_value = float(new_value)
                    phone.update_property(property_name, new_value)
                    print("Phone updated successfully!")
                else:
                    phones.pop(index)
                    print("Phone deleted successfully!")
            else:
                print("Invalid phone number.")

        elif choice == '4':
            if not phones: 
                print("No phones in the list.")
            else:
                print("\n".join(f"{i + 1}. {phone.display_info()}" for i, phone in enumerate(phones)))

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

main_menu()