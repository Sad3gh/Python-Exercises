def palindrome_checker(s):
    #removing non-alphanumeric chars and converting to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    #checking to see if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

print(palindrome_checker("a man a plan a canal panama"))
print(palindrome_checker("1661"))