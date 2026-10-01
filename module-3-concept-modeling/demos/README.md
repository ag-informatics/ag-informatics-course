# Demo: Objects in Python

ASM 532 - Module 3 - Lecture 3.3

This is the demo from class. Poke around at your own pace. Nothing here is graded.

1. A notebook version of the `farm.py` read-along: classes, inheritance, encapsulation and polymorphism, using farm animals.

To run it:

1. Open `farm-oop-demo.ipynb` in VS Code.
2. Select the `.venv` kernel you used in Lab 2 (no extra libraries are needed; it only uses Python's built-in `datetime`).
3. Run the cells in order, top to bottom.

## farm.py, as a notebook

Source file: [farm-oop-demo.ipynb](farm-oop-demo.ipynb)

The same steps as the lecture slides, one cell per step:
- a reusable `Animal` class
- a `Goat` that inherits from it
- methods added to `Animal`
- a `Cow` that overrides `details()`

Look at what happens to `Goat` when `Animal` gets new methods. It has to be re-defined to pick them up, because a class keeps the parent it was built from.
