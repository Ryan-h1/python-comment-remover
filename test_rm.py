

print("Hello, World!")  


def tricky_strings():
    
    print("This is a tricky case: # This is not a comment")
    print('And so is this: # Not a comment because it\'s inside single quotes')

    
    print("An escaped double quote: \" and an escaped single quote: \' in the same string")
    print('Similarly, an escaped single quote: \' and an escaped double quote: \" here')

    
    print("This is a string that spans "
          "multiple lines, using implicit "  
          "concatenation")

    
    print("A string ending with a backslash\\")

    
    print("Just a string")  



triple_quoted_with_hashes =        """This is a triple-quoted string with a # hash and a backslash \\ in it."""



@decorator  
def function_with_decorator():
    pass


class ExampleClass:
    
    def method(self):
        return "Method result"



print("A string with a nested 'single quote', an escaped single quote \', and a # hash")


print("""This string has "double quotes" and 'single quotes' inside, plus a # hash.""")


print("Special characters in strings should not confuse the parser")


print("Part 1 of a concatenated string" +  
      " and part 2 of the concatenated string.")


print("Finished parsing edge cases.")  
