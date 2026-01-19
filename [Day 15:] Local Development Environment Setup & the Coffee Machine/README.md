# Day 15: Local Development Environment Setup & the Coffee Machine

## Project: Coffee Machine

### Description
A command-line coffee machine simulator that manages resources, processes orders, accepts payment, and dispenses beverages. This project simulates a real coffee machine with inventory management, payment processing, and resource tracking.

### What I Learned
- Setting up local Python development environment
- Resource management and tracking
- Dictionary operations for inventory
- Processing transactions
- Input validation
- State management
- Modular function design

### How to Run
```bash
cd "Day15Project_CoffeMachine"
python3 [main_file].py
```

### Features
- Multiple drink options (espresso, latte, cappuccino)
- Resource tracking (water, milk, coffee)
- Coin-operated payment system
- Change calculation
- Resource reporting
- Sufficient resource checking
- Admin commands (report, off)

### Available Drinks
- **Espresso**: Water + Coffee
- **Latte**: Water + Milk + Coffee
- **Cappuccino**: Water + Milk + Coffee

### How It Works
1. User selects a drink or command
2. Machine checks if sufficient resources available
3. User inserts coins (quarters, dimes, nickels, pennies)
4. Machine validates payment
5. If successful: dispenses drink and updates resources
6. Returns change if payment exceeds cost

### Key Concepts
- **Resource Management**: Tracking and updating inventory
- **Transaction Processing**: Accepting and validating payment
- **Dictionary Operations**: Managing resource data
- **Function Modularity**: Breaking down complex logic
- **State Persistence**: Maintaining machine state across orders

### Commands
- `espresso` - Order an espresso
- `latte` - Order a latte
- `cappuccino` - Order a cappuccino
- `report` - Display current resources
- `off` - Turn off the machine

### Files
- Project folder with coffee machine implementation
- `day15.py`: Additional exercises

### Example Usage
```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.50 in change.
Here is your latte. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 200ml
Milk: 50ml
Coffee: 76g
Money: $2.50
```

### Learning Focus
Building a practical application with real-world logic: inventory, payments, and resource constraints.
