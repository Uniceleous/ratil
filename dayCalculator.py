dd = 0
mm = 0
yyyy = 0
f_date = None
f_month = None
f_year = None
n_date = None
n_month = None
n_year1 = None
n_year2 = None
condition = None

def day():
    global dd, mm, yyyy, f_date, f_month, f_year, n_date, n_month, n_year1, n_year2, condition
    inp = input("""
    Enter a date, and I will calculate the day for you!
    Example - 1/1/2023
    -> """)
    
    dd, mm, yyyy = inp.split("/")
    c_date = dd.isnumeric()
    c_mm = mm.isnumeric()
    c_yyyy = yyyy.isnumeric()

    if c_date: f_date = True
    else: f_date = False
    if c_mm: f_month = True
    else: f_month = False
    if c_yyyy: f_year = True
    else: f_year = False

    if f_date and f_month and f_year and len(dd) == 1 and len(mm) == 1 and len(yyyy) == 4: condition = True
    else: print("False")

    if condition:
        n_year1 = list(yyyy)
        n_year1 = n_year1[2:0]
        print(n_year1)

day()