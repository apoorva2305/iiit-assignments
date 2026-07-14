# find plaindrome
def is_palindrome(text):
    # Convert to string and make it lowercase for a fair comparison
    clean_text = str(text).lower()
    return clean_text == clean_text[::-1]

# Testing the function
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome(12321))      # Output: True
print(is_palindrome("python"))   # Output: False
