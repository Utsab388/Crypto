from string import ascii_lowercase, ascii_uppercase

def caesar_cipher(s, n1):
  # Create the translation table
  lowercase_table = str.maketrans(ascii_lowercase, ascii_lowercase[n1:] + ascii_lowercase[:n1])
  uppercase_table = str.maketrans(ascii_uppercase, ascii_uppercase[n1:] + ascii_uppercase[:n1])

  # Encode or decode the string using the translation table
  return s.translate(lowercase_table).translate(uppercase_table)

# Test the function
encoded = caesar_cipher("hello", 3)
print(encoded)  # Output: khoor
decoded = caesar_cipher(encoded, 3)
print(decoded)  # Output: hello
