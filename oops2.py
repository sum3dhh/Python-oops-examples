class dem:
    def __init__(self) -> None:
        print("King created")
    def __del__(self):
        print("DESTRUCTION 100 BOOM BAAM ")

obj = dem()
del obj