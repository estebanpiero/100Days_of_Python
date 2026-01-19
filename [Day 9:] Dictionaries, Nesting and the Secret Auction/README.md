# Day 9: Dictionaries, Nesting and the Secret Auction

## Project: Secret Auction Program

### Description
A blind auction program where multiple users can submit bids secretly. The program clears the screen between bids to maintain privacy, then determines and announces the highest bidder at the end.

### What I Learned
- Python dictionaries (key-value pairs)
- Adding and accessing dictionary data
- Iterating through dictionaries
- Nesting data structures
- Cross-platform screen clearing
- Working with the `time` module
- Finding maximum values in dictionaries

### How to Run
```bash
cd "Da9Project_AuctionProgram"
python3 app.py
```

### Features
- Secret bidding (screen clears between bids)
- Multiple bidder support
- Automatic winner determination
- Bid summary display
- Cross-platform compatibility (Windows/Mac/Linux)
- ASCII art logo
- Privacy-focused design

### How It Works
1. Program displays logo and prompts for bidder name
2. Bidder enters their bid amount
3. Bid is stored in a dictionary
4. Screen clears to hide the bid from the next person
5. Process repeats until no more bidders
6. Program displays all bids and announces the winner

### Key Concepts
- **Dictionaries**: Storing bidder names as keys and bid amounts as values
- **Dictionary Iteration**: Looping through key-value pairs
- **Conditional Logic**: Determining the highest bid
- **OS Module**: Cross-platform screen clearing
- **Data Privacy**: Clearing screen to maintain bid secrecy

### Files
- `app.py`: Main auction program
- `art.py`: ASCII art logo

### Additional Practice Files
- `Day9.py`: Dictionary basics and exercises
- `Grading_Program.py`: Grade conversion using dictionaries

### Example Usage
```
What is your name?: Alice
What is your bid?: $150

Are there any other bidders? Type 'yes' or 'no'.
> yes

[Screen clears]

What is your name?: Bob
What is your bid?: $200

The winner is Bob with a bid of $200
```
