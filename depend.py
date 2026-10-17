
class Arithmetic:
    def add(self, i: int, j: int) -> int:
        return i + j

    def subtract(self, i: int, j: int) -> int:
        return i - j

    def multiply(self, i: int, j: int) -> int:
        return i * j

    def divide(self, i: int, j: int) -> float:
        return i / j


# Create one instance
_obj = Arithmetic()

# Expose its methods at the module level
add = _obj.add
subtract = _obj.subtract
multiply = _obj.multiply
divide = _obj.divide

