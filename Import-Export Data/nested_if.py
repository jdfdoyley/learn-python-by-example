# Name: Jason D'Oyley
# Date: Nov 29, 2022
# Day #: 001

# Nested if Statement
# You can nest statements within a code block to begin a new code block, as
# long as they follow their respective indentations.

x, y, z = 7, 4, 2

if x > y:
    print('x is greater than y')

    if x > z:
        print('x is greater than y and z')

# Prints
# x is greater than y
# x is greater than y and z