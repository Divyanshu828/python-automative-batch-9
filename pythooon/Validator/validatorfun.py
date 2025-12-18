
# Create a user-defined package that contains a module to validate:
# Email ID
# Mobile number
# Import this package and validate user input.



import re           #re stands for Regular Expressions, a module in Python used for string pattern matching


def validate_email(email):
    # Pattern for a valid email address
    # ^            → start of string
    # [\w\.-]+     → username (letters, numbers, dot, underscore, hyphen)
    # @            → must contain @ symbol
    # [\w\.-]+     → domain name
    # \.           → dot before domain extension
    # \w+          → domain extension (com, org, in, etc.)
    # $            → end of string
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # re.match checks if the email matches the pattern
    # bool() converts the result to True or False
    return bool(re.match(pattern, email))

def validate_mobile(mobile):
    # Pattern for Indian mobile number
    # ^            → start of string
    # [6-9]        → first digit must be 6, 7, 8, or 9
    # \d{9}        → exactly 9 more digits
    # $            → end of string
    pattern = r'^[6-9]\d{9}$'
    
    # Check if mobile number matches the pattern
    return bool(re.match(pattern, mobile))

