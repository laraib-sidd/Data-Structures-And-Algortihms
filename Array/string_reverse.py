'''
Function to reverse a string.
Example:
Input : "Hi how are you?"
Output : "?uoy era woh iH"
'''
def reverse(string):
    """
    Function to reverse string
    """
    string = list(string)
    string = string[::-1]
    string = "".join(string)
    return string


word = reverse("This function Reverses string")
print(word)