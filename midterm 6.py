def days_since_birthday(birthday):
    # Extract the birth year from the birthday string
    birth_year = int(birthday[-4:])

    # Extract the current year
    current_year = 2024  # Assuming the current year is 2024

    # Calculate the number of whole years passed
    years_passed = current_year - birth_year - 1

    # Calculate the number of days passed excluding the birth year and the current year
    days_passed = years_passed * 365

    return days_passed


# Example usage:
birthday = "05-10-1990"  # Format: DD-MM-YYYY
print(days_since_birthday(birthday))  # Output: Number of days passed since the birthday
