class Animal:

    @classmethod
    def unknown_animal(cls):
        return cls(None, None, None)

    @staticmethod
    def general_info():
        return "Welcome to the jungle..."

    def __init__(self, type, height, weight):
        self.type = type
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f"{__class__}({self.type}, {self.height}, {self.weight})"

    def __str__(self):
        return f"A/an {self.type} of height {self.height} and weight {self.weight}"

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type