#This is part of our app.
from django.shortcuts import render
from . models import FlashCard
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    users = request.user.all()
    return render(request, "flashcard/home.html", {
        "user": users,
    })

def flashCard(request):
    cards = FlashCard.objects.all()
    return render(request, 'flashcards/home.html', {'cards': cards})

def createDeck(request):
    form = DeckForm(request.POST)


def flashCard_new(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            flashCard = form.save()
            return redirect('flashcard_new', pk=flashCard.pk)
    else:
        form = CardForm()

def flashCard_edit(request, pk):
    flashCard = get_object_or_404(flashCard, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=flashCard)
        if form.is_valid():
            form.save()
            return redirect('flashcard_edit', pk=flashCard.pk)
    else:
        form = CardForm(instance=flashCard)
    
def flashCard_delete(request, pk):
    flashCard = get_object_or_404(flashCard, pk=pk)
    flashCard.delete()
    return redirect('flashcard_list')
    
















# def add(request):
#     from random import randint

#     num_1 = randint(0,10)
#     num_2 = randint(0,10)

#     if request.method == "POST":
#         answer = request.POST['answer']
#         old_num_1 = request.POST['old_num_1']
#         old_num_2 = request.POST['old_num_2']

#         correct_answer = int(old_num_1) + int(old_num_2)
#         if int(answer) == correct_answer:
#             my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
#             color = "success"
#         else:
#             my_answer =  "Incorrect! " + old_num_1 + " + " + old_num_2 + " is not " + answer + " it is " + str(correct_answer)
#             color = "danger"

#         return render(request, 'add.html', {
#             'answer':answer,
#             'my_answer': my_answer,
#             'num_1':num_1,
#             'num_2':num_2,
#             'color':color, 
#             })

#         return render(request, 'add.html', {
#             'num_1':num_1,
#             'num_2':num_2,
#             })

# def subtract(request):
#     return render(request, 'subtract.html', {})

# def multiply(request):
#     return render(request, 'multiply.html', {})

# def divide(request):
#     return render(request, 'divide.html', {})