# ex 1
import math

eps = 1e-8


def example_one(x):
    k = 0
    s = 1
    term = 1

    while abs(term) > 1e-8:
        k += 1
        term *= x / k
        s += term

    return s


print(f"Example One: {example_one(float(5)):.8f}")


# ex 2
def example_two(x):
    i = 1
    first = 1
    second = first - ((((i + 1) * (i + 2)) / 2) * x ** i)

    while abs(first - second) > eps:
        i += 1
        first = second

        if i % 2 == 0:
            second = first + ((((i + 1) * (i + 2)) / 2) * x ** i)
        else:
            second = first - ((((i + 1) * (i + 2)) / 2) * x ** i)

    return first


print(f"Example Two: {example_two(0.5)}")


# ex 3
def example_three(x):
    i = 1
    first = -x
    second = first - ((x ** (i + 1)) / (i + 1))

    while abs(second - first) > 0.0001:
        i += 1
        first = second
        second = first - ((x ** (i + 1)) / (i + 1))

    return first


print(f"Example Three: {example_three(float(-1))}")


# ex 4
def example_four(x):
    i = 1
    first = 1
    tuSo = 1
    mauSo = 2

    second = first + (tuSo / mauSo) * x
    tuSoStep = 1
    mauSoStep = 4

    while abs(first - second) > eps:
        i += 1
        first = second

        tuSo *= tuSoStep
        mauSo *= mauSoStep

        tuSoStep += 2
        mauSoStep += 2

        if i % 2 == 0:
            second -= (tuSo / mauSo) * x ** i
        else:
            second += (tuSo / mauSo) * x ** i

    return first


print(f"Example Four: {example_four(float(0.5))}")


# ex 5
def example_five(x):
    i = 1
    first = 1
    tuSo = 1
    mauSo = 2
    tuSoStep = 3
    mauSoStep = 4

    second = first - (tuSo / mauSo) * x
    while abs(first - second) > eps:
        i += 1
        tuSo *= tuSoStep
        mauSo *= mauSoStep

        tuSoStep += 2
        mauSoStep += 2
        first = second

        if i % 2 == 0:
            second += (tuSo / mauSo) * x ** i
        else:
            second -= (tuSo / mauSo) * x ** i

    return first


print(f"Example Five: {example_five(0.5)}")


# ex 6
def example_six(x):
    i = 3

    first = 1
    second = 1 - (x ** i) / math.factorial(i)
    y = 0

    while abs(first - second) > eps:
        i += 2
        y += 1

        first = second

        if i % 2 == 0:
            second -= x ** i / math.factorial(i)
        else:
            second += x ** i / math.factorial(i)

    return first


print(f"Example Six: {example_six(1)}")


# ex 7
def example_seven(x):
    i = 2

    first = 1
    second = 1 - (x ** i) / math.factorial(i)
    y = 0

    while abs(first - second) > eps:
        y += 1
        i += 2

        first = second

        if i % 2 != 0:
            second -= x ** i / math.factorial(i)
        else:
            second += x ** i / math.factorial(i)

    return first


print(f"Example Seven: {example_seven(1)}")


# ex # ex 8
def example_eight(x):
    i = 3
    first = x
    tuSo = 1
    mauSo = 2
    second = first + ((tuSo / mauSo) * (x ** i) / i)
    while abs(first - second) > eps:
        i += 2
        tuSo = tuSo * (i - 2)
        mauSo = mauSo * (i - 1)

        first = second
        second = first + ((tuSo / mauSo) * (x ** i) / i)
    return first


print(f"Example Eight: {example_eight(0.5)}")


# ex 9
def example_nine(x):
    step = 2
    i = 0
    first = 1
    second = (first - x ** step / math.factorial(step + 1))

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if i % 2 != 0:
            second = first + x ** step / math.factorial(step + 1)
        else:
            second = first - x ** step / math.factorial(step + 1)
    return first


print(f"Example Nine: {example_nine(1)}")


# ex 10
def example_ten(x):
    step = 3
    i = 0
    first = x
    second = (first - x ** step / step)

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if i % 2 != 0:
            second = first + x ** step / step
        else:
            second = first - x ** step / step

    return first


print(f"Example Ten: {example_ten(0.5)}")


# ex 11
def example_eleven(x):
    step = 3
    first = x
    second = first + x ** step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / step
    return first


print(f"Example Eleven: {example_eleven(0.5)}")


# ex 12
def example_twelve(x):
    step = 3
    first = x
    second = first + x ** step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / step
    return first


print(f"Example Twelve: {example_twelve(0.5)}")


# ex 13
def example_thirteen(x):
    step = 3
    first = x
    second = first + x ** step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / math.factorial(step)
    return first


print(f"Example Thirteen {example_thirteen(0.5)}")


# ex 14
def example_fourteen(x):
    step = 2
    first = x
    second = first + x ** step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x ** step / math.factorial(step)
    return first


print(f"Example Fourteen: {example_fourteen(0.5)}")
