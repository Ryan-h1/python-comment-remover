# A single-line comment with a tricky end: "This is not a string."

print("Hello, World!")  # An inline comment with a "string" and a # hash


def tricky_strings():
    # A string containing a comment symbol inside a function
    print("This is a tricky case: # This is not a comment")
    print('And so is this: # Not a comment because it\'s inside single quotes')

    # Escaped quotes inside strings
    print("An escaped double quote: \" and an escaped single quote: \' in the same string")
    print('Similarly, an escaped single quote: \' and an escaped double quote: \" here')

    # The following line has a string that spans multiple lines, using implicit concatenation
    print("This is a string that spans "
          "multiple lines, using implicit "  # This comment is in the middle of a string definition
          "concatenation")

    # A backslash at the end of a line inside a string (not a comment)
    print("A string ending with a backslash\\")

    # Comments with a backslash before the end-of-line character, which might confuse parsers
    print("Just a string")  # A comment with a backslash at the end \


# Triple-quoted strings with embedded # characters and backslashes
triple_quoted_with_hashes =        """This is a triple-quoted string with a # hash and a backslash \\ in it."""


# Using comments after special Python syntax
@decorator  # This is a comment after a decorator
def function_with_decorator():
    pass


class ExampleClass:
    # A comment inside a class
    def method(self):
        return "Method result"


# Complex case with nested quotes and escaped characters
print("A string with a nested 'single quote', an escaped single quote \', and a # hash")

# Edge case: Using triple quotes to start a string, but with single and double quotes inside
print("""This string has "double quotes" and 'single quotes' inside, plus a # hash.""")

# Comment with special characters: \n, \t, \\, and so on
print("Special characters in strings should not confuse the parser")

# An edge case with concatenated strings and comments
print("Part 1 of a concatenated string" +  # This comment is in the middle of concatenation
      " and part 2 of the concatenated string.")

# End of the program
print("Finished parsing edge cases.")  # This should be ignored as a comment
