daycare_name = "Happy Pets Care"  # Text (String)
food_fee = 50.0  # Decimal Number (Float)

# LIST: The types of animals we accept
pet_types = ["Dog", "Cat"]

# TUPLE: The address of our daycare (this never changes)
daycare_address = ("Main Street", "Room 10")

# DICTIONARIES: Animal names connected to their Price and Room Left
fees = {"Dog": 500, "Cat": 300}
spaces_left = {"Dog": 3, "Cat": 5}

# SET: Keeps a list of unique animal types that visited today
animals_seen_today = set()

print("Welcome to", daycare_name)

while True:
    print("\nWhat do you want to do?")
    print("1. See available spaces and prices")
    print("2. Check-in a pet")
    print("3. Close Daycare & Exit")

    choice = input("Type 1, 2, or 3: ")

   
    if choice == "1":
        print("\n--- Current Spaces ---")
        # Loop through our list one by one
        for animal in pet_types:
            print(f"- {animal}: Fee is ₹{fees[animal]}, Spaces left: {spaces_left[animal]}")
    elif choice == "2":
        print("\n--- Check-in a Pet ---")
        pet_chosen = input("Is your pet a Dog or a Cat?: ").capitalize()

        # Check if we accept this kind of pet
        if pet_chosen in pet_types:
            # Check if we have space left (Comparison Operator: >)
            if spaces_left[pet_chosen] > 0:
                # Take away 1 space because a pet moved in (Assignment Operator: -=)
                spaces_left[pet_chosen] -= 1

                # Calculate the final bill (Arithmetic Operators: +)
                total_bill = fees[pet_chosen] + food_fee

                # Add the animal type to our SET
                animals_seen_today.add(pet_chosen)

                print("\n PET CHECKED IN SUCCESSFULLY!")
                print("Basic Daycare Fee: ₹", fees[pet_chosen])
                print("Food Fee: ₹", food_fee)
                print("Total Bill to Pay: ₹", total_bill)
            else:
                print("Sorry! No space left for a", pet_chosen)
        else:
            print("We do not accept that kind of animal here.")

    elif choice == "3":
        print("\nClosing the daycare for today...")
        # Show what types of animals came today using our Set
        print("Types of animals cared for today:", animals_seen_today)
        print("Goodbye!")
        break  # This stops the program safely

    else:
        print(" Invalid choice! Please type 1, 2, or 3.")