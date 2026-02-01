def decorator(original_function):
    def wrapper():
        v_1, v_2, t, a = original_function()
        s = (v_2 + v_1)/2*t
        print(s)
    return wrapper

@decorator
def uskorenie():
    try :
        v_1 = int(input())
        v_2 = int(input())
        t = int(input())
        a = (v_2 - v_1) / t
        print(a)
        return v_1, v_2, t, a
    except ValueError:
        print('Нельзя вводить строки ')
    except ZeroDivisionError:
        print('Нельзя делить на 0 ')

uskorenie()