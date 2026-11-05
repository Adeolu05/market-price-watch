from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.city}"


class Item(models.Model):
    class Category(models.TextChoices):
        GRAINS = "grains", "Grains and Staples"
        PRODUCE = "produce", "Fruits and Vegetables"
        PROTEIN = "protein", "Meat, Fish and Eggs"
        FUEL = "fuel", "Fuel and Energy"
        OTHER = "other", "Other"

    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50, help_text="e.g. 50kg bag, 1 paint bucket, 1 litre")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.unit})"


class PriceReport(models.Model):
    photo = models.ImageField(upload_to="price_photos/", blank=True)
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="reports")
    market = models.ForeignKey(Market, on_delete=models.PROTECT, related_name="reports")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    reported_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["-reported_at"]

    def __str__(self):
        return f"{self.item.name} at {self.market.name}: ₦{self.price}"