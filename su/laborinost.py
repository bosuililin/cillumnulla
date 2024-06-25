def test(*args):
    if not args:
        print("Note: You have not passed any argument")
    else:
        print("You have passed " + str(len(args)) + " arguments")

test(1, 5, 8)  # Output: You have passed 3 arguments
test()  # Output: Note: You have not passed any argument
