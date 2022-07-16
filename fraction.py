from mathops.gcd import computeGCD as gcd


class Fraction:
    def __init__(self, numerator, denominator):
        """
        How to initialize a fraction?
        """

        if denominator == 0:
            raise "Denominator cannot be zero"

        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)

    def __str__(self):
        """
        How to print (str) a fraction?
        """
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        """
        When are two fractions equal?
        """
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __add__(self, other):
        """
        How to add two fractions
        """
        numerator = (
            self.numerator * other.denominator + self.denominator * other.numerator
        )
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
