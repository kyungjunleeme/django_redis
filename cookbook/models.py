from django.db import models


class Food(models.Model):
    """An edible item."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """A preparation of food."""
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(
        'cookbook.Food',
        through='cookbook.Ingredient',
        through_fields=('recipe', 'food')
    )
    instructions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """food that is used in a recipe."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=3,
        null=True,
        blank=True,
    )  # ex. 1/8 = 0.125, 1/4 = 0.250
    unit_of_measure = models.CharField(max_length=255)  # ex. tsp, tbsp, cup
    desc = models.TextField()  # ex. 2 cloves of garlic, minced

    def __str__(self):
        return f'{self.recipe}: {self.amount} {self.unit_of_measure} {self.food}'
