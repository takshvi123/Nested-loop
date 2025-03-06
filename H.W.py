# Store localized messages in a dictionary for future scalability
MESSAGES = {
    "welcome": "🌟 Welcome to the Decimal to Binary Converter Program! 🌟",
    "start": "💻 This program will help you convert a decimal number into its binary equivalent. 💡",
    "input": "👉 Please enter a non-negative decimal number (or type 'exit' to quit): ",
    "exit": "👋 Goodbye! Thank you for using the Decimal to Binary Converter Program. See you again! 🌟",
    "invalid": "❌ Oops! That doesn't seem like a valid number. Please enter a whole number. 🙏",
    "negative": "❌ Sorry, this program only works with non-negative integers. Please try again. 🙏",
    "complete": "✅ Conversion complete!",
    "binary": "🎉 The binary representation of {decimal} is: {binary}",
    "thank_you": "🙏 Thank you for using the Decimal to Binary Converter Program. Have an amazing day! 🌈",
}

def show_welcome_message():
    """Prints the welcome message."""
    print(MESSAGES["welcome"])
    print(MESSAGES["start"])

def decimal_to_binary(decimal_number):
    """Converts a decimal number to binary."""
    return bin(decimal_number)[2:]  # Remove the '0b' prefix

def get_user_input():
    """Handles user input with validation."""
    user_input = input(MESSAGES["input"]).strip()
    if user_input.lower() == 'exit':
        return None  # Exit condition
    try:
        decimal_number = int(user_input)
        if decimal_number < 0:
            print(MESSAGES["negative"])
            return get_user_input()
        return decimal_number
    except ValueError:
        print(MESSAGES["invalid"])
        return get_user_input()

def main():
    """Main program loop."""
    show_welcome_message()
    while True:
        user_input = get_user_input()
        if user_input is None:  # Handle exit condition
            print(MESSAGES["exit"])
            break

        decimal_number = user_input
        if decimal_number == 0:  # Special case for zero
            print(f"\n{MESSAGES['complete']}")
            print(f"🎉 The binary representation of 0 is: 0")
        else:
            binary_number = decimal_to_binary(decimal_number)
            print(f"\n{MESSAGES['complete']}")
            print(MESSAGES["binary"].format(decimal=decimal_number, binary=binary_number))
        print(MESSAGES["thank_you"])

# Run the program
if __name__ == "__main__":
    main()
