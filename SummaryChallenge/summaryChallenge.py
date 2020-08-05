menu_string = "Please select one option from below \n " \
      "1. Learn Python\n 2. Learn JavaScript\n 3. Machine Learning\n " \
      "4. Data Science\n 5. Algorithms and Data Structures\n 0. Exit\n"

user_input = -1

while user_input != 0:
    if user_input in [1, 2, 3, 4, 5]:
        print(f"You Choose to Learn Option Number {user_input}")
    else:
        print(menu_string)

    user_input = int(input("Please Press the Valid Number button from "
                           "above Menu Between 0 - 5.\n"))
else:
    print(f"You Choose To Quit.")
