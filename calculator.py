class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        is_negative = False

        if (b < 0):
            b = -b
            is_negative = not is_negative
        if (a < 0):
            a = -a
            is_negative = not is_negative

        for _ in range(b):
            result = self.add(result, a)

        if is_negative:
            result = -result

        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        a_sign = 1 if a >= 0 else -1
        b_sign = 1 if b >= 0 else -1
        sign = a_sign * b_sign

        a_abs, b_abs = abs(a), abs(b)
        result = 0

        while a_abs >= b_abs:
            a_abs = self.subtract(a_abs, b_abs)
            result = self.add(result, 1)

        if sign < 0:
            if a_abs > 0:
                result = self.add(result, 1)
            result = -result

        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")

        # Compute floor division
        quotient = self.divide(a, b)
        # Compute the product of quotient and divisor
        product = self.multiply(quotient, b)
        # Compute the remainder
        remainder = self.subtract(a, product)
        return remainder