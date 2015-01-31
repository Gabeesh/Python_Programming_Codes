__author__ = 'AKHIL REDDY'

while True:
    try:
        number = int(input("What's your favourite number guru?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and Enter a number?")
    except ZeroDivisionError:
        print("Don't Pick Zero !Boss!!!")
    except:
        break
    finally:
        print("Loop Complete")
