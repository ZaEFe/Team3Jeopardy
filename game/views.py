from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Question, Player, Wager

# View for displaying the game board
def game_board(request):
    categories = Category.objects.all()
    return render(request, 'game_board.html', {'categories': categories})

# View for revealing a specific question (when a contestant selects it)
def reveal_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'reveal_question.html', {'question': question})

# View for the instructor to control the game and see the correct answer
def host_panel(request):
    return render(request, "host_panel.html")

# API to get the current active question (for the host panel)
def get_current_question(request):
    question = Question.objects.filter(active=True).first()
    if question:
        return JsonResponse({"question": question.question_text, "answer": question.answer})
    return JsonResponse({"question": None})

# API to set the current question (when a question is picked by the contestant)
def set_current_question(request, question_id):
    # Deactivate all other questions first
    Question.objects.update(active=False)
    question = get_object_or_404(Question, id=question_id)
    question.active = True
    question.save()

    return JsonResponse({"question": question.question_text})

# API for updating the score of a player
def update_score(request, player_id, question_id, correct):
    player = get_object_or_404(Player, id=player_id)
    question = get_object_or_404(Question, id=question_id)

    if correct:
        player.score += question.value
    else:
        player.score -= question.value

    player.save()
    return JsonResponse({"new_score": player.score})

# API for placing a wager during Final Jeopardy or Daily Double
def place_wager(request, player_id, question_id, amount):
    player = get_object_or_404(Player, id=player_id)
    question = get_object_or_404(Question, id=question_id)

    # Ensure the player has enough points to wager
    if player.score >= amount:
        Wager.objects.create(player=player, question=question, amount=amount)
        return JsonResponse({"status": "Wager placed successfully"})
    else:
        return JsonResponse({"status": "Not enough points to place this wager"})

# View to get the leaderboard or show player scores (optional)
def leaderboard(request):
    players = Player.objects.all().order_by('-score')
    return render(request, 'leaderboard.html', {'players': players})