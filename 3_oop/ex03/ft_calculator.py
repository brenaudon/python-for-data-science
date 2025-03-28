class calculator:
    """A calculator class that can do scalar operations on a single vector"""

    def __init__(self, vector: list[float]):
        """
        Constructor
        :param vector: A list of floats
        """
        self.vector = vector

    def __add__(self, obj) -> None:
        """Vector + scalar"""
        if isinstance(obj, (int, float)):
            self.vector = [v + obj for v in self.vector]
            print(self.vector)
        else:
            raise TypeError("Right operand must be int or float.")

    def __sub__(self, obj) -> None:
        """Vector - scalar"""
        if isinstance(obj, (int, float)):
            self.vector = [v - obj for v in self.vector]
            print(self.vector)
        else:
            raise TypeError("Right operand must be int or float.")

    def __mul__(self, obj) -> None:
        """Vector * scalar"""
        if isinstance(obj, (int, float)):
            self.vector = [v * obj for v in self.vector]
            print(self.vector)
        else:
            raise TypeError("Right operand must be int or float.")

    def __truediv__(self, obj) -> None:
        """
        Vector / scalar
        """
        if isinstance(obj, (int, float)):
            if obj == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [v / obj for v in self.vector]
            print(self.vector)
        else:
            raise TypeError("Right operand must be int or float.")
