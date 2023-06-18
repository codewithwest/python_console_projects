from xml.dom import UserDataHandler


def user_details():
    # first name check
    f = True
    first_name = input("Insert your first name\n")
    while f:
        fn = first_name.lower()
        if (fn == "") or (fn.isalpha() == False) or (len(fn) == 0) or (fn == "\n"):
            print("Invalid first name")
            first_name = input("Insert your first name\n")
        else:
            first_name = first_name.lower()
            f = False
    l = True
    # last name check
    last_name = input("Insert your last name\n")
    while f:
        ln = last_name.lower()
        if (ln == "") or (ln.isalpha() == False) or (len(ln) == 0) or (ln == "\n"):
            print("Invalid last name")
            last_name = input("Insert your last name\n")
        else:
            last_name = last_name.lower()
            f = False
    # check for cohort/year
    k = True
    cohort = input("Insert your cohort\n")
    while k:
        kh = cohort
        if (kh == "") or (kh.isdigit() == False) or (len(kh) == 0) or (kh == "\n") or (int(kh) < 2022):
            print("Invalid cohort")
            cohort = input("Insert your cohort\n")
        else:
            cohort = int(cohort)
            k = False
    # campus call
    c = True
    while c:
        campus = input("Insert the campus you will be attending in\n").lower()
        cm = campus.lower()
        camps = ["johannesburg", "durban", "phokeng", "cape town"]
        if cm != "" and cm.isalpha() != False and cm in camps and cm != "\n":
            c = False
            campus = campus.lower()
            pass
        else:
            print("Invalid campus")

    final_campus = user_campus(campus)
    user_name = create_user_name(first_name, last_name, cohort, final_campus)
    print(user_name)


def create_user_name(first_name, last_name, cohort, final_campus):
    f_n = True
    while f_n:
        if len(first_name) < 3:
            first_name = first_name + "o"
        else:
            first_name = first_name[-3:].lower()
            f_n = False
    l_n = True
    while l_n:
        if len(last_name) < 3:
            last_name = last_name + "o"
        else:
            last_name = last_name[0:3:1].lower()
            l_n = False

    cohort = str(cohort)
    final_campus = final_campus
    return first_name + last_name + cohort + final_campus


def user_campus(campus):
    f_n = campus.lower()
    cit = True
    while cit:
        if f_n == "johannesburg":
            final_campus = "JHB"
            cit = False
        elif f_n == "cape town":
            final_campus = "CPT"
            cit = False
        elif f_n == "durban":
            final_campus = "DBN"
            cit = False
        else:
            final_campus = "PHO"
            cit = False

    return final_campus


if __name__ == '__main__':
    user_details()
