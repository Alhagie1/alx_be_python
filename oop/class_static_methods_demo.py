#  Class Methods and Static Methods
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print (f"Calculation type: {Calculator.calculation_type}")
        return a * b
    