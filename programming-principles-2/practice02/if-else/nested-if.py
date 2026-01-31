# You can have if statements inside if statements. This is called nested if statements.
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
        
# Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.
# Checking multiple conditions with nesting.
age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")
    
# You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.
# Three levels of nesting.
score = 85
attendance = 90
submitted = True
if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")
    
# Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.
temperature = 25
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")
        
# Could also be written with and.
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
    print("Perfect beach weather!")
    
# Login validation with nested checks.
username = "Emil"
password = "python123"
is_active = True
if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")
    
# Grade calculation with nested logic.
score = 92
extra_credit = 5
if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade or below")