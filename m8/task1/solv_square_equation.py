import argparse


def validate_param(p):

    return type(p) is int


def discriminant(a, b, c):
    disc = b ** 2 - 4 * a * c
    return disc


def roots(d, a, b, c):
    if d > 0:  
        x1 = ((-b + d**0.5) / (2 * a) )
        x2 = ((-b - d**0.5) / (2 * a) )
        answer = x1, x2
        return  answer
    elif d == 0:
        x1 = (-b / 2)
        answer = x1
        return  answer    
    else:
        return ("no roots")

def solv_square(a, b, c) -> roots:
    d = discriminant(a, b, c)
    return roots(d, a, b, c)


def square_print(a, b, c, res: roots):
    answer = res
    print(f'result is {answer}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=int, required=True)
    parser.add_argument("-b", type=int, required=True)
    parser.add_argument("-c", type=int, required=True)
    a, b, c = None, None, None
    try:
        args = vars(parser.parse_args())
        a, b, c = args['a'], args['b'], args['c']
    except:
        print(
            f'please enter three integers (a,b,c) separated with spaces or just blank line to exit:\n'
        )
        tries = 3
        while tries > 0:
            res = input()
            tries -= 1
            if tries == 0 or res == '':
                exit()

            try:
                a, b, c = res.split(" ")
                a, b, c = int(a), int(b), int(c)
                if not (validate_param(a) or validate_param(b)
                        or validate_param(c)):
                    print(f'wrong input {(a,b,c)}\n')
                else:
                    break
            except Exception as e:
                print(f'{e} , you have {tries} more tries')

    res = solv_square(a, b, c)
    square_print(a, b, c, res)


if __name__ == "__main__":
    main()
