dd = 0
mm = 0
yyyy = 0
f_date = None
f_month = None
f_year = None
condition = None
m_list1 = [1, 3, 5, 7, 8, 10, 12]
m_list2 = [4, 6, 9, 11]
m_list3 = 2

def day():
    global dd, mm, yyyy, f_date, f_month, f_year, condition, m_list1, m_list2, m_list3
    inp = input("""
    Enter a date, and I will calculate the day for you!
    Example - 1/1/2023
    -> """)
    
    dd, mm, yyyy = inp.split("/")
    c_date = dd.isnumeric()
    c_mm = mm.isnumeric()
    c_yyyy = yyyy.isnumeric()

    if c_date and c_mm and c_yyyy: 
        if int(mm) <= 12 and int(mm) > 0:
            if int(mm) in m_list1:
                if int(dd) <= 31 and int(dd) > 0:
                    f_date = True
                else:
                    f_date = False
            elif int(mm) in m_list2:
                if int(dd) <= 30 and int(dd) > 0:
                    f_date = True
                else:
                    f_date = False
            elif int(mm) == m_list3:
                if int(dd) <= 28 and int(dd) > 0:
                    f_date = True
                else:
                    f_date = False
        else: 
            f_month = False
        if int(len(yyyy)) == 4 and int(yyyy) > 0:
            f_year = True
        else:
            f_year = False

        if f_date and f_month and f_year:
            condition = True      
        else:
            condition = False

    if condition:
        print(condition)
    else:
        print(False)

day()