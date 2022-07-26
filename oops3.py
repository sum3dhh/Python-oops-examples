class hardy:
    def __init__(self) -> None:
        print("King created")
    def __del__(self):
        print("DESTRUCTION 100 BOOM BAAM ")

def cobj():
    print("Creating a Object.....")
    obj = hardy()
    print("Almost done.......")
    return obj

print("Processing functions........")
obj = cobj()
print("program ends..........")
