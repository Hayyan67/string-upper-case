class IOString:
    def __init__(self):
        self.str1 =" "

    def get_String(self):
        self.str1 =  input('Enter any string: ')

    def display(self):
        print('Sting is ',self.str1.upper())

OI = IOString()
OI.get_String()
OI.display()