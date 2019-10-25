import unittest
from math import exp, log

class Diapason(Exception):
    def __init__(self, text):
        self.text = text


def inputs(f, a, b, n):
    try:
        if a < 0 or b < 0:
            raise Diapason("a аба b < 0")
        if a > b:
            raise Diapason("a > b")
        res = middlesquere(f, a, b, n)
    except NameError:
        res = "Неправильна вхідна функція"
    except Diapason as e:
        return str(e)

    return res


def middlesquere(f, a, b, n):
    h = float(b - a) / n
    result = float(b - a)*func((a+b)/2, f)
    for i in range(1, n):
        result += func(a + i * h, f)
    result *= h
    return round(result, 8)



def func(x, func):
    dd = eval(func)
    return dd


class TestCalc(unittest.TestCase):
    def test_1(self):
        res = inputs("x*exp(x)", 0, 1, 10)
        self.assertEqual(res, 0.95)

    def test_2(self):
        res = inputs("log(10*x)", 0.1, 0.1*exp(1), 10)
        self.assertEqual(res, 0.09)

    def test_3(self):
        res = inputs("x*ex(x)", 0, 1, 10)
        self.assertEqual(res, "Неправильна вхідна функція")

    def test_4(self):
        res = inputs("x*exp(x**2)", -2, 1, 10)
        self.assertEqual(res, "a аба b < 0")

    def test_5(self):
        res = inputs("x**2 + (16/x**3)", 1, exp(1), 10)
        self.assertEqual(res, 12.99)

    def test_6(self):
        res = inputs("x**2 + (16/x)", 5, exp(1), 10)
        self.assertEqual(res, "a > b")


if __name__ == "__main__":
    unittest.main()
res = inputs("x**2 + (16/x)", 5, exp(1), 10)
print(res)
res = inputs("x*ex(x)", 0, 1, 10)
print(res)
res = inputs("x*exp(x)", -2, 1, 10)
print(res)
res = inputs("x*exp(x)", 2, 1, 10)
print(res)
res = inputs("1 - x*exp(-x)", 0, 1, 1000)
print(res)

res = inputs("x", 0, 1, 10)
print('rex', res)