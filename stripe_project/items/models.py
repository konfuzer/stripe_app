from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percent_off = models.PositiveIntegerField(null=True, blank=True)
    amount_off = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name


class Tax(models.Model):
    display_name = models.CharField(max_length=255)
    inclusive = models.BooleanField(default=False)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.display_name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    def total_price(self):
        total = sum(item.price for item in self.items.all())
        if self.discount:
            if self.discount.percent_off:
                total *= (1 - self.discount.percent_off / 100)
            elif self.discount.amount_off:
                total -= self.discount.amount_off
        return round(total, 2)

    def get_currency(self):
        # Берём валюту первого товара
        return self.items.first().currency if self.items.exists() else 'USD'

    def __str__(self):
        return f"Order {self.id}"
