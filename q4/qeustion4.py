def fact(n):

    if(n==1 or n==0):
        return 1
    return n* fact(n-1)

if __name__ == "__main__":

    print("0 : {0:d}".format(fact(0)))
    print("2 : {0:d}".format(fact(2)))
    print("4 : {0:d}".format(fact(4)))
    print("6 : {0:d}".format(fact(6)))
    print("8 : {0:d}".format(fact(8)))
    print("10 : {0:d}".format(fact(10)))
    print("12 : {0:d}".format(fact(12)))
    print("14 : {0:d}".format(fact(14)))

                         
