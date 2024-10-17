def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return (n%pow(10,k+1))//pow(10,k)


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return sum([a,b,c]) - min([a,b,c]) - max([a,b,c])


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    c = n
    if k != 0:
        for i in range(1,k):
            c *= (n-i)
        return c
    return 1



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    c = 0
    if n%k ==0:
        division = n//k
        for i in range(1,division+1):
            c += k
            print(c)
        return division
    return c
## please browse the code carefully and make sure the starting


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    dig_count = 1
    sum_dig = 0
    x=y
    while x //10 != 0:
        x //= 10
        dig_count += 1
   
    for i in range(dig_count):
        sum_dig += y%pow(10,i+1)//pow(10,i)
    return sum_dig
## yokatta, i did it, divide it two face digits. i am so happy to be zero.


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    dig_count = 1
    x = n
    while x //10 != 0:
        x //= 10
        dig_count += 1
    # find digit count
    for i in range(dig_count):
        if (n%pow(10,i+1)//pow(10,i) == 8) and (n%pow(10,i+2)//pow(10,i+1) == 8):
            return True
    return False