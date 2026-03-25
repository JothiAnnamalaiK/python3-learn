class InvalidAgeError(Exception):
    """custiom exception for invalid age"""  # to view details on hover

    def __init__(self, message="Age must be above 18 or older!"):
        self.message = message
        super().__init__(self.message)  # passing to base class
