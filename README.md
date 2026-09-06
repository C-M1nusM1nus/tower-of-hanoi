# Tower Of Hanoi
A simple Python program that solves the Tower of Hanoi puzzle using recursion.

The program moves a specified number of disks from the first rod to the third rod while following the rules of the Tower of Hanoi.

# Features
* Solves the Tower of Hanoi puzzle recursively.
* Supports any number of disks greater than or equal to zero.
* Tracks the arrangement of all three rods after every move.
* Returns the complete sequence of moves as a string.
* Demonstrates the use of recursion and nested functions.

## hanoi_solver(n)
The hanoi_solver() function solves the Tower of Hanoi puzzle for the specified number of disks.

hanoi_solver(3)

The disks start on the first rod and are moved to the third rod.

The rods are represented as three lists:

| Rod 1 | Rod 2 | Rod 3 |
| :---: | :---: | :---: |
| [3, 2, 1] | [] | [] |

The largest disk is represented by the largest number, and the smallest disk is represented by 1.

# How It Works
The solver uses the following recursive process:
1. Move n - 1 disks from the source rod to the auxiliary rod.
2. Move the largest remaining disk to the target rod.
3. Move the n - 1 disks from the auxiliary rod to the target rod.
4. Repeat until all disks have been moved.

After every disk movement, the current state of all three rods is recorded.

# Example
print(hanoi_solver(2))

Output:

[2, 1] [] []

[2] [] [1]

[] [] [2, 1]

[] [1] [2]

[] [2, 1] []

Each line represents the current contents of the three rods.

# Functions
## record()
Records the current state of all three rods and adds it to the list of moves.

## move_disks(count, source, target, auxiliary)
A recursive helper function that moves the specified number of disks between rods.

It performs the actual Tower of Hanoi algorithm.

# Requirements
* Python 3.x
* No external libraries are required.
