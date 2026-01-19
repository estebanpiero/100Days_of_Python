# Day 16: Object Oriented Programming (OOP)

## Project: Coffee Machine (OOP Version)

### Description
A refactored version of the Coffee Machine project using Object-Oriented Programming principles. This implementation uses classes and objects to create a more modular, maintainable, and scalable coffee machine simulator.

### What I Learned
- Object-Oriented Programming fundamentals
- Creating and using classes
- Class attributes and methods
- Creating objects (instances)
- Working with methods
- Importing and using external classes
- OOP vs procedural programming
- Encapsulation and modularity

### How to Run
```bash
cd "Day16Project_CoffeMachine_OOP"
python3 [main_file].py
```

### OOP Concepts Applied

#### Classes Used
- **CoffeeMachine**: Main class managing the machine
- **MenuItem**: Represents a drink item
- **Menu**: Manages available menu items
- **MoneyMachine**: Handles payment processing
- **CoffeeMaker**: Manages resources and drink making

### Key Differences from Procedural Version
- **Encapsulation**: Data and functions grouped in classes
- **Modularity**: Each class has a specific responsibility
- **Reusability**: Classes can be reused in other projects
- **Maintainability**: Easier to modify and extend

### Key Concepts
- **Class**: Blueprint for creating objects
- **Object**: Instance of a class
- **Attributes**: Data stored in objects (properties)
- **Methods**: Functions that belong to objects
- **Constructor**: `__init__` method for initializing objects
- **Encapsulation**: Bundling data with methods

### Files
- Project folder with OOP implementation
- Multiple class files
- `day16_main.py`: Main program file

### Example Class Structure
```python
class CoffeeMaker:
    def __init__(self):
        self.resources = {...}

    def report(self):
        # Display resources

    def is_resource_sufficient(self, drink):
        # Check if enough resources

    def make_coffee(self, order):
        # Deduct resources and make coffee
```

### Benefits of OOP Approach
1. Better code organization
2. Easier to understand and maintain
3. Reusable components
4. Scalable for future features
5. Real-world modeling

### Learning Focus
Understanding how to structure programs using classes and objects instead of just functions and variables.
