from django.db import models

# Create your models here.

class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer = models.TextField()
    value = models.IntegerField()
    daily_double = models.BooleanField(default=False)
    final_jeopardy = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category.name} - {self.value}"

class Player(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Wager(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return f"{self.player.name} wagered {self.amount} on {self.question.value}"

class FinalJeopardy(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    wager = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)