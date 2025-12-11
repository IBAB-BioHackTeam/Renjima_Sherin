# ibab-task01-Renjimasherin

The main aim of this task is to:
- Setup a local development environment
- Create and configure SSH keys and link them with GitHub
- Use Git from the terminal (clone, edit, commit, push) instead of only using the GitHub website
- Write a simple Bubble Sort program
- Add a basic project document using README.md

This repository has :
- C program for bubble sort
- Readme.md file with instructions and explanations

BubbleSort logic:
Bubble Sort is a simple sorting algorithm. We repeatedly go through the list, compare neighbouring elements, and swap 
them if they are in the wrong order.
The user inputs number of elements 'n' and then 'n' integers.
- We use two loops:
  The outer loop runs 'n - 1' times.
  The inner loop starts from the last element and moves towards the beginning.
- In each step of the inner loop, we compare 'a[j]' and 'a[j - 1]'.
  If 'a[j]' is smaller than 'a[j - 1]', we swap them.
- After all passes, the array becomes sorted in ascending order.

To run the code we require:

- A C compiler like 'gcc'
- Terminal access (WSL + Ubuntu / Linux / macOS)

Steps:
- Compile the C program
  gcc bubble_sort.c -o bubble_sort
- Run the program
  ./bubble_sort
 
