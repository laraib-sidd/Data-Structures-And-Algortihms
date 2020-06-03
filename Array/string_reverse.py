'''
Function to reverse a string.
Example:
Input : "Hi how are you?"
Output : "?uoy era woh iH"
'''
def reverse(string):
    string = list(string)
    string = string[::-1]
    string = "".join(string)
    return string

