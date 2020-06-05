'''
Function to reverse a string.
Driver Code:
Input : "Hi how are you?"
Output : "?uoy era woh iH"
'''


def reverse(string):
    """
    Function to reverse string
    """
    try:
        if string or len(string) > 2:
            string = list(string)
            string = string[::-1]
            string = "".join(string)
            return string
    except KeyboardInterrupt:
        print("Check Your Input")


if __name__ == "__main__":
    word = reverse("This function Reverses string")
    print(word)
