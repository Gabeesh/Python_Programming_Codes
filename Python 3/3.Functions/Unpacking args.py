def add_number(args):
    total =0
    for a in args:
        total += a
    print total

def add_number1(*args):
    total =0
    for a in args:
        total += a
    print total


a=(2,3,4)
add_number(a)
add_number1(2,45,234)

def life_calculator(age,apples,cigs):
    answer = (100-age)+apples*3-cigs*2
    print answer

akki_data = [20,1,6]
life_calculator(akki_data[0],akki_data[1],akki_data[2])
life_calculator(*akki_data)

