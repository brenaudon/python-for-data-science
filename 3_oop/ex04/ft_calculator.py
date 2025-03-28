class calculator:
    """Calculator class for vector-to-vector operations."""

    def __init__(self, vector: list[float]):
        """
        Constructor
        :param vector: A list of floats
        """
        self.vector = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates dot product of two vectors V1 and V2"""
        dot_value = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {dot_value}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds two vectors element-wise"""
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts two vectors element-wise (V1 - V2)"""
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
