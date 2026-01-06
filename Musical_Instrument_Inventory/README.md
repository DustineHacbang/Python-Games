# Musical Instrument Inventory

A simple Python application demonstrating object-oriented programming concepts using classes. This project is designed to help practice creating and using classes in Python.

## Overview

This application creates a `MusicalInstrument` class that represents musical instruments with their properties and behaviors. It demonstrates fundamental OOP concepts including:

- Class definition
- Constructor (`__init__`)
- Instance methods
- Object instantiation

## Class Structure

### MusicalInstrument Class

The `MusicalInstrument` class has the following structure:

```python
class MusicalInstrument:
    def __init__(self, name, instrument_type):
        # Constructor that initializes the instrument
```

**Attributes:**

- `name`: The name of the instrument (e.g., "Oboe", "Trumpet")
- `instrument_type`: The family/category of the instrument (e.g., "woodwind", "brass")

**Methods:**

- `play()`: Prints a message indicating the instrument is fun to play
- `get_fact()`: Returns a string with information about the instrument's family

## How to Use the App

### Running the Application

1. Navigate to the `Musical_Instrument_Inventory` directory
2. Run the Python script:
   ```bash
   python musical_intrument_inventory.py
   ```

### Example Output

When you run the script, you'll see:

```
The Oboe is fun to play!
The Oboe is part of the woodwind family of instruments.
The Trumpet is fun to play!
The Trumpet is part of the brass family of instruments.
```

### Creating Your Own Instruments

You can create new instrument instances by instantiating the `MusicalInstrument` class:

```python
# Create a new instrument
my_instrument = MusicalInstrument('Guitar', 'string')

# Use the methods
my_instrument.play()
print(my_instrument.get_fact())
```

**Example:**

```python
instrument_3 = MusicalInstrument('Piano', 'keyboard')
instrument_3.play()
print(instrument_3.get_fact())
```

## Learning Objectives

This project helps you practice:

1. **Class Definition**: Understanding how to define a class in Python
2. **Constructor (`__init__`)**: Learning how to initialize objects with attributes
3. **Instance Methods**: Creating methods that operate on instance data
4. **Object Instantiation**: Creating instances of a class
5. **Method Calls**: Calling methods on objects

## Extending the Application

Here are some ideas to practice more OOP concepts:

### Add More Attributes

```python
def __init__(self, name, instrument_type, price, year_made):
    self.name = name
    self.instrument_type = instrument_type
    self.price = price
    self.year_made = year_made
```

### Add More Methods

```python
def get_info(self):
    return f"{self.name} ({self.instrument_type}) - ${self.price}"
```

### Create a Collection

```python
instruments = [
    MusicalInstrument('Oboe', 'woodwind'),
    MusicalInstrument('Trumpet', 'brass'),
    MusicalInstrument('Violin', 'string')
]

for instrument in instruments:
    instrument.play()
```

## Requirements

- Python 3.x

No external dependencies required - this uses only Python's built-in features.

## File Structure

```
Musical_Instrument_Inventory/
├── musical_intrument_inventory.py  # Main application file
└── README.md                        # This file
```

## Notes

- This is a learning project focused on understanding Python classes
- The class demonstrates basic OOP principles suitable for beginners
- Feel free to modify and experiment with the code to deepen your understanding
