s = "Moin Khan"  # A sequence of unicodes is known as string
# s = 'Moin Khan'   # Valid
s = """Moin Khan"""  # Valid - widely used to make a string of multiline
s = """What is your name?
My Name is Moin Khan
    """
# s='''My Name Is Khan''' # Valid
print(s)
# s[1]="K";   # Not Valid (Strings are immutable)
print(s[::-1])
print(s[1:9:])
print(s[::2])
print(len(s))
