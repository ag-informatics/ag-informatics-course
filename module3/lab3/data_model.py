from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import date


# Create a base class for our models (tables)
class Base(DeclarativeBase):
    pass


# Let's start by creating a model for the crops table
class Crop(Base):
    __tablename__ = "crops"  # The name of the table in the database
    crop_id: Mapped[int] = mapped_column(primary_key=True)  # The primary key column
    crop_name: Mapped[str]
    maturity_date: Mapped[int]
    note: Mapped[Optional[str]]  # A nullable column

    # Leave the line below commented until the instruction in Jupyter notebook asks you to uncomment it
    plots: Mapped[List["Plot"]] = relationship(back_populates="crop")

    def __repr__(
        self,
    ):  # A string representation of the object. It will give you a nice output when you print the object
        return f"{self.crop_id}: {self.crop_name} - Maturity date: {self.maturity_date} days"


class Plot(Base):
    __tablename__ = "plots"
    plot_id: Mapped[int] = mapped_column(primary_key=True)
    planted_date: Mapped[date]
    crop_id: Mapped[int] = mapped_column(
        ForeignKey("crops.crop_id")
    )  # A foreign key to the crops table
    # complete the model

    # Leave the line below commented until the instruction in Jupyter notebook asks you to uncomment it
    crop: Mapped["Crop"] = relationship(back_populates="plots")

    def __repr__(self):
        return f"{self.crop.crop_name}"  # complete the string representation

    # def expected_harvest_date(self):
    #     return self.planted_date + timedelta(days=self.crop.maturity_date)
