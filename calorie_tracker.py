print("=== Simple Calorie Tracker ===")
print("Track your daily calorie intake!")

# Basic variables
daily_limit = 0
current_calories = 0
food_list = []

# Main program loop
while True:
    print("\n--- Main Menu ---")
    print("1. Set Daily Calorie Limit")
    print("2. Add Food and Calories")
    print("3. View Today's Progress")
    print("4. Exit Program")
    
    choice = input("Enter your choice (1-4): ")
    
    # Option 1: Set daily limit
    if choice == "1":
        user_input = input("Enter your daily calorie limit: ")
        
        # Simple number checking
        if user_input.isdigit():
            daily_limit = int(user_input)
            print(f"Great! Your daily limit is set to {daily_limit} calories")
        else:
            print("Please enter a valid number ")
    
    # Option 2: Add food
    elif choice == "2":
        if daily_limit == 0:
            print("Please set your daily limit first ")
        else:
            food_name = input("Enter food name: ")
            calorie_input = input("Enter calories: ")
            
            if calorie_input.isdigit():
                calories = int(calorie_input)
                current_calories += calories
                food_list.append(food_name)
                print(f"Added {food_name} - {calories} calories")
                print(f"Total calories today: {current_calories}")
            else:
                print("Please enter a valid number for calories")
    
    # Option 3: View progress
    elif choice == "3":
        if daily_limit == 0:
            print("Please set your daily limit first ")
        else:
            remaining = daily_limit - current_calories
            
            print(f"\n=== Your Daily Progress ===")
            print(f"Daily Limit: {daily_limit} calories")
            print(f"Calories Eaten: {current_calories} calories")
            print(f"Remaining: {remaining} calories")
            
            # Simple progress message
            if remaining > 0:
                print(f"You have {remaining} calories left for today! ✅")
            else:
                over_limit = -remaining
                print(f"You are {over_limit} calories over your limit! ⚠️")
            
            # Show food list
            if food_list:
                print(f"\nFoods you've eaten today:")
                for i, food in enumerate(food_list, 1):
                    print(f"  {i}. {food}")
            else:
                print("\nNo foods added yet today.")
    
    # Option 4: Exit
    elif choice == "4":
        print("Thank you for using Calorie Tracker!")
        print("Goodbye! 👋")
        break
    
    # Invalid choice
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")