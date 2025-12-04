#!/usr/bin/env python3
"""
Demo script that showcases the calculator functions.
This serves as the entry point for the Docker container.
"""

from calculator import add, subtract, multiply, divide, print_hello_world


def main():
    """Run calculator demonstrations."""
    print("=" * 50)
    print("Calculator Demo")
    print("=" * 50)
    print()
    
    # Test hello world function
    print_hello_world()
    print()
    
    # Demonstrate calculator operations
    print("Calculator Operations:")
    print("-" * 50)
    
    a, b = 10, 5
    
    print(f"Numbers: a = {a}, b = {b}")
    print()
    print(f"Addition:       {a} + {b} = {add(a, b)}")
    print(f"Subtraction:    {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    print(f"Division:       {a} / {b} = {divide(a, b)}")
    print()
    
    # Test with different numbers
    x, y = 15, 3
    print(f"Numbers: x = {x}, y = {y}")
    print()
    print(f"Addition:       {x} + {y} = {add(x, y)}")
    print(f"Subtraction:    {x} - {y} = {subtract(x, y)}")
    print(f"Multiplication: {x} * {y} = {multiply(x, y)}")
    print(f"Division:       {x} / {y} = {divide(x, y)}")
    print()
    
    print("=" * 50)
    print("Demo completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
