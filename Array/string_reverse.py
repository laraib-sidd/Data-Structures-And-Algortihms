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
    try:
        if string or len(string)>2:
            string = list(string)
            string = string[::-1]
            string = "".join(string)
            return string
    except:
        print("Check Your Input")

word = reverse("This function Reverses string")
print(word)
