def myFunc():
    print("Hello world!")
myFunc()
print(__name__)



if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    print(__name__)