# Demo: the Farm tracker

ASM 532 - Module 3 - Lecture 3.3

This is the demo from class. Poke around at your own pace. Nothing here is graded.

1. A notebook version of the Farm tracker from the lecture: the object model, the data model in Crow's Foot notation, and the SQL that builds and queries it.

To run it:

1. Open `farm-tracker-demo.ipynb` in VS Code.
2. Select the `.venv` kernel you used in Lab 2 (no extra libraries are needed; it only uses Python's built-in `sqlite3`).
3. Run the cells in order, top to bottom.

## The Farm tracker, as a notebook

Source file: [farm-tracker-demo.ipynb](farm-tracker-demo.ipynb)

The same steps as the lecture slides, in the same order:
- the object model, the Crow's Foot legend, and the full data model
- building the tables, and the farm data so far
- a join: which crops are growing in which fields
- two inserts the database accepts but shouldn't, and a foreign key it refuses
- the joins that catch them

It uses an in-memory database, so nothing is written to disk.

The Objects in Python half of Lecture 3.3 moved to [Module 4, Lecture 4.1](../../module-4-web-applications/lecture-4.1.html).
