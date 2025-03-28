from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for Character
        :param first_name: The name of the character
        :param is_alive:   Boolean indicating if the character is alive
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to kill the character"""
        self.is_alive = False


class Stark(Character):
    """The Stark family class, inherits from Character"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for Stark
        :param first_name: The name of the Stark
        :param is_alive:   Boolean indicating if the character is alive
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Kills the character by setting is_alive to False"""
        super().die()
