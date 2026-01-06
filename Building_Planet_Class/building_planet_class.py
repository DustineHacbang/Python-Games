class Planet:
    def __init__(self, name, planet_type, star):
        # Validate inputs
        if not all(isinstance(arg, str) for arg in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")
        if not all(arg.strip() for arg in (name, planet_type, star)):
            raise ValueError("name, planet type, and star cannot be empty")

        # Store attributes
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # Instance method to describe the planet's orbit
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    # String representation of the planet
    def __str__ (self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"