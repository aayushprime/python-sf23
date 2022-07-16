from mathops.gcd import computeGCD as gcd


class Fraction:
    def __init__(self, numerator, denominator):

        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __add__(self, other):
        numerator = (
            self.numerator * other.denominator + self.denominator * other.numerator
        )
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
