class PythonNotes:

    def __init__(self):
        self.notes = {
            1: "Introduction to Python:\nPython is a high-level, interpreted programming language known for its simplicity and readability.",            
            2: "Variables:\nVariables are used to store data values.\nExample:\nx = 10\ny = 'Hello'",            
            3: "Data Types:\nCommon data types are int, float, string, list, tuple, set, dictionary.",            
            4: "Operators:\nOperators are used to perform operations on variables.\nExamples: +, -, *, /, %, ==, !=, >, <",            
            5: "Conditional Statements:\nUsed to make decisions.\nExample:\nif x > 10:\n    print('Greater')\nelse:\n    print('Smaller')",            
            6: "Loops:\nLoops are used to repeat a block of code.\nTypes: for loop and while loop.",           
            7: "Functions:\nFunctions are reusable blocks of code.\nExample:\ndef add(a,b):\n    return a+b",          
            8: "Lists:\nLists store multiple items in a single variable.\nExample:\nfruits = ['apple','banana','mango']",          
            9: "Tuples:\nTuples are similar to lists but immutable.\nExample:\nt = (1,2,3)",
            10: "Dictionaries:\nDictionary stores data in key:value pairs.\nExample:\nstudent = {'name':'Rahul','age':20}"
        }

    def show_topics(self):
        print("\nPython Notes Topics")
        for key in self.notes:
            print(key, ".", self.notes[key].split(":")[0])

    def show_note(self, choice):
        print("\n", self.notes.get(choice, "Invalid Topic"))


notes = PythonNotes()

while True:
    notes.show_topics()
    print("0. Exit")

    ch = int(input("Enter topic number: "))

    if ch == 0:
        print("Thank you for using Python Notes")
        break
    else:
        notes.show_note(ch)