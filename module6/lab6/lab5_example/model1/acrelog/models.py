from django.db import models

OPERATION_TYPES = [
    ("tillage", "Tillage"),
    ("plant", "Plant"),
    ("spray", "Spread/Spray"),
    ("soil", "Soil Sampled"),
    ("harvest", "Harvest"),
    ("other", "Other"),
]


# Create your models here.
class Operator(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.firstname}{' '+self.lastname if self.lastname else ''}"


class Field(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Machine(models.Model):
    name = models.CharField(max_length=50)
    inventory_id = models.CharField(max_length=10, blank=True, null=True)
    is_ready_to_use = models.BooleanField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Seed(models.Model):
    plant = models.CharField(max_length=20)
    genotype = models.CharField(max_length=30)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.plant} - {self.genotype}"


class Operation(models.Model):
    operation_type = models.CharField(choices=OPERATION_TYPES, max_length=30)
    date = models.DateField()
    note = models.CharField(max_length=300, blank=True, null=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    location = models.ForeignKey(Field, on_delete=models.CASCADE)
    tool = models.ForeignKey(Machine, on_delete=models.CASCADE, blank=True, null=True)
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, blank=True, null=True)
    seed_rate = models.IntegerField(blank=True, null=True)
    fertillizer = models.CharField(max_length=100, blank=True, null=True)
    fertiliizer_rate = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.date.isoformat()} {self.operator}  {self.operation_type}"

    def tag_id(self):
        return f"tag-{self.id}"

    def is_more_detail(self):
        return (
            "btn-warning"
            if (self.note or self.tool or self.seed or self.fertillizer)
            else "btn-dark disabled"
        )
