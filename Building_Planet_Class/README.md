# Building Planet Class

A Python project demonstrating object-oriented programming principles, focusing on creating reusable code through classes and methods. This project showcases how to build a `Planet` class that can be instantiated multiple times to create different planet objects.

## Overview

This application creates a `Planet` class that represents celestial planets with their properties and behaviors. The project emphasizes:

- **Reusable Code**: Write the class once, use it many times
- **Input Validation**: Ensuring data integrity through constructor validation
- **Method Design**: Creating useful methods that work with instance data
- **String Representation**: Customizing how objects are displayed

## Class Structure

### Planet Class

The `Planet` class is designed to be reusable - you define it once and can create as many planet instances as needed.

```python
class Planet:
    def __init__(self, name, planet_type, star):
        # Constructor with validation
```

**Attributes:**

- `name`: The name of the planet (e.g., "Earth", "Mars", "Jupiter")
- `planet_type`: The classification of the planet (e.g., "terrestrial", "gas giant", "ice giant")
- `star`: The star the planet orbits (e.g., "Sun", "Proxima Centauri")

**Methods:**

- `__init__(self, name, planet_type, star)`: Constructor that initializes the planet with validation
- `orbit()`: Returns a string describing the planet's orbital behavior
- `__str__()`: Returns a formatted string representation of the planet

## Key Features

### 1. Input Validation

The constructor includes validation to ensure data quality:

```python
# Validates that all inputs are strings
if not all(isinstance(arg, str) for arg in (name, planet_type, star)):
    raise TypeError("name, planet type, and star must be strings")

# Validates that inputs are not empty
if not all(arg.strip() for arg in (name, planet_type, star)):
    raise ValueError("name, planet type, and star cannot be empty")
```

This ensures:

- Only string values are accepted
- Empty strings or whitespace-only strings are rejected
- Better error messages for debugging

### 2. Reusable Code Pattern

The class demonstrates the power of reusable code:

**Without Classes (Repetitive):**

```python
# Bad: Repetitive code
earth_name = "Earth"
earth_type = "terrestrial"
earth_star = "Sun"
print(f"Planet: {earth_name} | Type: {earth_type} | Star: {earth_star}")

mars_name = "Mars"
mars_type = "terrestrial"
mars_star = "Sun"
print(f"Planet: {mars_name} | Type: {mars_type} | Star: {mars_star}")
```

**With Classes (Reusable):**

```python
# Good: Reusable class
earth = Planet("Earth", "terrestrial", "Sun")
mars = Planet("Mars", "terrestrial", "Sun")
print(earth)
print(mars)
```

## How to Use the App

### Basic Usage

1. **Create a Planet Instance:**

   ```python
   earth = Planet("Earth", "terrestrial", "Sun")
   ```

2. **Use the Methods:**

   ```python
   # Get orbital information
   print(earth.orbit())
   # Output: Earth is orbiting around Sun...

   # Get string representation
   print(earth)
   # Output: Planet: Earth | Type: terrestrial | Star: Sun
   ```

### Complete Example

```python
from building_planet_class import Planet

# Create multiple planets (demonstrating reusability)
earth = Planet("Earth", "terrestrial", "Sun")
mars = Planet("Mars", "terrestrial", "Sun")
jupiter = Planet("Jupiter", "gas giant", "Sun")
kepler_22b = Planet("Kepler-22b", "super-Earth", "Kepler-22")

# Use the orbit method
print(earth.orbit())
print(mars.orbit())
print(jupiter.orbit())

# Use string representation
print(earth)
print(mars)
print(jupiter)
print(kepler_22b)
```

### Working with Collections

One of the best demonstrations of reusable code is creating collections:

```python
# Create a list of planets
solar_system = [
    Planet("Mercury", "terrestrial", "Sun"),
    Planet("Venus", "terrestrial", "Sun"),
    Planet("Earth", "terrestrial", "Sun"),
    Planet("Mars", "terrestrial", "Sun"),
    Planet("Jupiter", "gas giant", "Sun"),
    Planet("Saturn", "gas giant", "Sun"),
    Planet("Uranus", "ice giant", "Sun"),
    Planet("Neptune", "ice giant", "Sun")
]

# Process all planets with a loop (reusable code in action!)
for planet in solar_system:
    print(planet)
    print(planet.orbit())
    print()  # Blank line for readability
```

## Learning Objectives

This project helps you practice:

1. **Reusable Code Design**

   - Write code once, use it many times
   - Avoid code duplication
   - Create templates for similar objects

2. **Class Construction**

   - Understanding `__init__` method
   - Setting up instance attributes
   - Organizing related data and behavior

3. **Input Validation**

   - Ensuring data quality
   - Providing helpful error messages
   - Defensive programming practices

4. **Method Design**

   - Creating instance methods
   - Using `self` to access instance data
   - Designing useful behaviors

5. **Special Methods**

   - `__str__()` for string representation
   - Customizing object display

6. **Object Instantiation**
   - Creating multiple instances from one class
   - Understanding that each instance is independent

## Benefits of Reusable Code

### 1. **DRY Principle (Don't Repeat Yourself)**

- Write the class definition once
- Create unlimited instances without rewriting code

### 2. **Maintainability**

- Fix bugs in one place (the class)
- All instances benefit from improvements

### 3. **Consistency**

- All planets follow the same structure
- Same methods available for all instances

### 4. **Scalability**

- Easy to add new planets
- Easy to extend functionality

## Extending the Application

Here are ideas to practice more reusable code patterns:

### Add More Methods

```python
def get_info(self):
    """Returns detailed information about the planet"""
    return f"{self.name} is a {self.planet_type} planet orbiting {self.star}"

def compare_star(self, other_planet):
    """Compare if two planets orbit the same star"""
    return self.star == other_planet.star
```

### Add More Attributes

```python
def __init__(self, name, planet_type, star, distance_from_star):
    # ... validation ...
    self.name = name
    self.planet_type = planet_type
    self.star = star
    self.distance_from_star = distance_from_star  # in AU
```

### Create Helper Functions

```python
def create_planet_from_dict(planet_data):
    """Factory function to create planets from dictionaries"""
    return Planet(
        planet_data['name'],
        planet_data['type'],
        planet_data['star']
    )

# Usage
planet_data = {"name": "Earth", "type": "terrestrial", "star": "Sun"}
earth = create_planet_from_dict(planet_data)
```

## Error Handling

The class includes validation that will raise helpful errors:

```python
# This will raise TypeError
try:
    invalid_planet = Planet(123, "terrestrial", "Sun")
except TypeError as e:
    print(e)  # "name, planet type, and star must be strings"

# This will raise ValueError
try:
    empty_planet = Planet("", "terrestrial", "Sun")
except ValueError as e:
    print(e)  # "name, planet type, and star cannot be empty"
```

## Requirements

- Python 3.x

No external dependencies required - uses only Python's built-in features.

## File Structure

```
Building_Planet_Class/
├── building_planet_class.py  # Planet class definition
└── README.md                  # This file
```

## Practice Exercises

1. **Create Multiple Planets**: Make 5-10 different planet instances
2. **Store in a List**: Create a list of planets and iterate through them
3. **Add Methods**: Create new methods like `get_description()` or `is_habitable()`
4. **Extend Attributes**: Add attributes like `mass`, `radius`, or `moons`
5. **Create Functions**: Write functions that work with Planet objects

## Notes

- This project emphasizes the **reusability** aspect of object-oriented programming
- The validation in the constructor demonstrates **defensive programming**
- The `__str__` method shows how to customize object representation
- Each instance is independent - changing one planet doesn't affect others
- This pattern can be applied to any scenario where you need multiple similar objects

## Real-World Application

This pattern is used everywhere in programming:

- User accounts in a system
- Products in an e-commerce site
- Students in a school management system
- Cars in a dealership inventory
- Any scenario with multiple similar objects

The key is: **Define once, use many times!**
