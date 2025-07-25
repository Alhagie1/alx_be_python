# Shopping List Manager program


# List of Choices 
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    

# The main function of the Program
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip() # Prompt a user for a choice

        if choice == "1":
             item = input("Enter an item name: ").strip() # prompting user to add an item to the list
             shopping_list.append(item)
        elif choice == "2":
            item = input("What is the item's name? ").strip() # asking a user the name of the item they want to remove
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"Item is not in the {shopping_list}")         
        elif choice == "3":
            if not shopping_list: # Checking if shoppin List is empty or not
                print("Your shopping list is empty")
            else:
                print("\n Your shopping list: ")
                for  item in shopping_list:
                    print(item)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

