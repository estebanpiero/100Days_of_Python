# Day 13: Debugging - How to Find and Fix Errors in your Code

## Topic: Debugging Techniques

### Description
This day focuses on debugging strategies and techniques for finding and fixing errors in Python code. Learn systematic approaches to identify syntax errors, runtime errors, and logical errors.

### What I Learned
- Debugging strategies and methodologies
- Using print() statements for debugging
- Understanding error messages and tracebacks
- Identifying syntax vs runtime vs logic errors
- Using Python debugger tools
- Code review and testing practices
- Common Python pitfalls and how to avoid them

### Debugging Techniques Covered

#### 1. Print Statement Debugging
- Strategic placement of print() statements
- Tracking variable values
- Verifying code execution flow

#### 2. Error Types
- **Syntax Errors**: Code doesn't follow Python rules
- **Runtime Errors**: Code runs but crashes
- **Logic Errors**: Code runs but produces wrong results

#### 3. Debugging Strategies
- Reproduce the bug consistently
- Read and understand error messages
- Use the traceback to locate the error
- Check variable values at key points
- Test assumptions
- Simplify the problem
- Take breaks and return with fresh eyes

#### 4. Common Errors
- IndentationError
- NameError
- TypeError
- IndexError
- KeyError
- Off-by-one errors

### Key Concepts
- **Systematic Debugging**: Following a methodical approach
- **Reading Tracebacks**: Understanding Python error messages
- **Rubber Duck Debugging**: Explaining code to find issues
- **Edge Cases**: Testing boundary conditions
- **Error Prevention**: Writing code that's easier to debug

### Best Practices
1. Read error messages carefully
2. Check indentation
3. Verify variable names and types
4. Test with simple inputs first
5. Comment out sections to isolate problems
6. Use descriptive variable names
7. Keep functions small and focused

### Tools and Techniques
- Python's built-in `print()` function
- Python debugger (pdb)
- VS Code debugger
- Linting tools
- Type hints for error prevention

### Example Debugging Workflow
```python
# Bug: Function returns wrong result
def calculate_total(items):
    total = 0
    for item in items:
        # Add print to debug
        print(f"Current item: {item}, Current total: {total}")
        total += item
    return total

# Run and observe output to find the issue
```

### Learning Focus
Developing systematic debugging skills that will be valuable throughout your programming career.
