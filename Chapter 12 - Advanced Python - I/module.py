def myfunc():
    print("Hello! from module")

# myfunc()
# print(__name__)


if __name__ == "__main__":
    print("Hello! from main")
    myfunc()
    print(__name__)

# just run the program and check the output results.