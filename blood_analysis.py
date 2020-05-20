# blood_analysis.py

def interface():
    print("My Blood Analysis Calculator")
    keep_runing = True
    while keep_runing:
        print("Options:")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_runing = False
        
if __name__ == "__main__":
    interface()