def palindrome(number_received):
    temp_number = number_received
    number = 0
    while temp_number > 0:
        number = number * 10 + temp_number % 10
        temp_number //=1 0
    if number_received == number:
        return "Palindrome"
    else:
        return "Non-Palindrome"
while True:
    string_received = input("Enter the number to check for Palindromicity : ")
    print(palindrome(int(string_received)))
    if input("Enter yes to continue : ").lower().strip() == "yes":
        continue
    else:
        break
