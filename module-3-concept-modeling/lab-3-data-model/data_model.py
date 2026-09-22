"""
ASM 532 - Lab 3: your data model, as Python classes.

One class per table. One attribute per column. One `relationship` per foreign key.

This file ships with ONE fully worked example (Crop), commented line by line, and
TWO stubs for your own objects from STEP 7. Read the example, then fill in the
stubs so they match the tables you actually built.

Nothing here talks to a database on its own — the notebook connects it up.
"""

from typing import List, Optional
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Every model class inherits from this. SQLAlchemy uses it to keep track of
    which classes map to which tables."""
    pass


# ---------------------------------------------------------------------------
# WORKED EXAMPLE — the crop tracker from STEP 6.
# Read this one. Do not edit it. It is here as the pattern to copy.
# ---------------------------------------------------------------------------


class Crop(Base):
    # The table this class maps to. It must match the name you used in SQL.
    __tablename__ = "crops"

    # PRIMARY KEY. `Mapped[int]` says "this column holds an integer".
    crop_id: Mapped[int] = mapped_column(primary_key=True)

    # A required column: no Optional, so it is NOT NULL.
    crop_name: Mapped[str]
    maturity_date: Mapped[int]

    # An optional column: Optional[...] is how you say NULL is allowed.
    note: Mapped[Optional[str]]

    # THE RELATIONSHIP, from the "one" side.
    # A crop can be planted in many plots, so this is a list. `back_populates`
    # names the attribute on the other class that points back here.
    plots: Mapped[List["Plot"]] = relationship(back_populates="crop")

    def __repr__(self):
        # How this object prints. Worth writing — it makes debugging far easier.
        return f"{self.crop_id}: {self.crop_name} - matures in {self.maturity_date} days"


class Plot(Base):
    __tablename__ = "plots"

    plot_id: Mapped[int] = mapped_column(primary_key=True)
    plot_name: Mapped[str]
    length: Mapped[int]
    width: Mapped[int]
    planted_date: Mapped[date]
    note: Mapped[Optional[str]]

    # THE FOREIGN KEY. It lives on the "many" side — each plot has one crop.
    crop_id: Mapped[int] = mapped_column(ForeignKey("crops.crop_id"))

    # THE RELATIONSHIP, from the "many" side. Singular, because one crop.
    crop: Mapped["Crop"] = relationship(back_populates="plots")

    def __repr__(self):
        return f"{self.plot_id}: {self.plot_name} ({self.length}x{self.width})"


# ---------------------------------------------------------------------------
# YOUR MODEL — STEP 7.
#
# Replace the two stubs below with your own two objects, from your STEP 5
# diagram. Rename the classes and the tables. Replace each YOUR CODE HERE as you go.
#
# Checklist for each class:
#   [ ] __tablename__ matches the table you created in SQLite
#   [ ] one primary key
#   [ ] every column from your diagram, with the right type
#   [ ] Optional[...] on the columns that are allowed to be empty
#   [ ] a __repr__ that prints something you would actually want to read
# And across the pair:
#   [ ] a ForeignKey on the "many" side
#   [ ] a relationship() on BOTH sides, with matching back_populates
# ---------------------------------------------------------------------------


class YourFirstObject(Base):
    """YOUR CODE HERE: rename this class to one of your objects, and write a
    one-line docstring saying what it represents in your domain."""

    __tablename__ = "your_first_table"   # YOUR CODE HERE: rename

    # YOUR CODE HERE: your primary key.
    # YOUR CODE HERE: your other columns. Useful types: Mapped[str], Mapped[int],
    #       Mapped[float], Mapped[date], Mapped[bool].
    # YOUR CODE HERE: the "one" side of your relationship, if this is the one side:
    #       things: Mapped[List["YourSecondObject"]] = relationship(back_populates="...")

    def __repr__(self):
        return "YOUR CODE HERE"


class YourSecondObject(Base):
    """YOUR CODE HERE: rename this class to your other object."""

    __tablename__ = "your_second_table"  # YOUR CODE HERE: rename

    # YOUR CODE HERE: your primary key.
    # YOUR CODE HERE: your other columns.
    # YOUR CODE HERE: your foreign key, if this is the "many" side:
    #       other_id: Mapped[int] = mapped_column(ForeignKey("your_first_table.your_id"))
    # YOUR CODE HERE: the matching relationship:
    #       other: Mapped["YourFirstObject"] = relationship(back_populates="things")

    def __repr__(self):
        return "YOUR CODE HERE"
