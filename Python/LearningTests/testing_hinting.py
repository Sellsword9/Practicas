"""
This is for testing hinting, main function dosen't do anything meaningful
"""
string: str = "Hello World"

tupla: tuple[str, ...] = ("Hello", "World", "!", "This", "is", "a", "tuple")

def main():
    """
    Testing hinting
    """
    print(string)
    print(tupla)

main()
 # Note to self:
 # Notable that in VSCode hoving over the variable should show the type
    # of the variable, but it dosen't work (for me) (yet? Am I missing extensions?)
