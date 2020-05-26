# blood_analysis.py


def Total_cholesterol_analysis(total):
    if total < 200:
        return "Normal"
    elif 200 <= total < 240:
        return "Borderline High"
    else:
        return "High"


def get_total(LDL, HDL):
    LDL_list = LDL.split("=")
    HDL_list = HDL.split("=")
    LDL_val = LDL_list[1]
    LDL_val = int(LDL_val)
    HDL_val = HDL_list[1]
    HDL_val = int(HDL_val)
    return LDL_val + HDL_val


def Total_cholesterol_interface():
    print("\nTotal Cholesterol analysis")
    print("Please enter your LDL test results in the following format:")
    print("LDL=### where ### is the numerical result")
    LDL_res = input("Result: ")
    print("Now enter your HDL test results in the following format:")
    print("HDL=### where ### is the numerical result")
    HDL_res = input("Result: ")
    Total_chol = get_total(LDL_res, HDL_res)
    print("\nTotal cholesterol levels are:")
    print(Total_cholesterol_analysis(Total_chol))


def LDL_analysis(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result < 160:
        return "Borderline high"
    elif 160 <= LDL_result < 190:
        return "High"
    else:
        return "Very High, you are dead"


def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"


def chol_interface():
    # Input should be HDL=66
    print("\ncholesterol_check_interface")
    print("Please input the result in the following format:")
    print("  HDL=## where ## is the numerical result")
    print("  Or LDL=### where ### is the numerical result")
    print("  Or TOTAL if you would like to check total cholesterol")
    chol_input = input("Result: ")
    chol_result = chol_input.split('=')
    if chol_result[0] == "HDL":
        HDL_status = HDL_analysis(int(chol_result[1]))
        print("HDL_status is {}".format(HDL_status))
    elif chol_result[0] == "LDL":
        LDL_status = LDL_analysis(int(chol_result[1]))
        print("LDL_status is {}".format(LDL_status))
    else:
        Total_cholesterol_interface()


def interface():
    print("My Blood Analysis Calculator")
    keep_runing = True
    while keep_runing:
        print("\nOptions:")
        print("1-cholesterol_check")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_runing = False
        elif choice == '1':
            chol_interface()

if __name__ == "__main__":
    interface()
