from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A King who inherits from both Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for King"""
        # We can call super() only once, thanks to Python's MRO
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Getter for eyes"""
        return self.eyes

    def set_eyes(self, color: str):
        """Setter for eyes"""
        self.eyes = color

    def get_hairs(self):
        """Getter for hairs"""
        return self.hairs

    def set_hairs(self, color: str):
        """Setter for hairs"""
        self.hairs = color
