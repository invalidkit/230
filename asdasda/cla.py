class Pet:
    def __init__(self, name: str, age: float, species: str, status: str = 'Alive'):
        self.Name: str = name
        self.Age: float = age
        self.Species: str = species
        self.Status: str = status
