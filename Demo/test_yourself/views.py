from django.shortcuts import render
from .models import MCQQuestion,Category,Subcat,Comment
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
def index(request):
    cat = Category.objects.all()
    return render(request, 'test_yourself/index.html', {'catags': cat})

def about(request):
    return render(request,'test_yourself/about.html')

def catagory_exercise(request,cat):
    catag = Category.objects.get(category = cat)
    subcat = Subcat.objects.filter(catag=catag)
    Qu = MCQQuestion.objects.filter(category = catag)
    qc = MCQQuestion.objects.all()[:1].get()
    Comments = Comment.objects.filter(question = qc).order_by('-id')
    #for comment in Comments:
    #    print(comment)

    params = {
        'Qu': Qu,
        'catagory' : catag,
        'subcat' : subcat,
        'comments': Comments
    }
    return render(request, 'test_yourself/catagories.html', params)

def get_comments(request):
    qi = request.POST['mcq']
    Qu = MCQQuestion.objects.get(content=qi)
    Comments = Comment.objects.filter(question = Qu)
    comments_serialized = serializers.serialize('json', Comments)
    return JsonResponse(comments_serialized,safe=False)

def catagory_chapter(request,cat,subcatagory):
    catag = Category.objects.get(category = cat)
    subcatagories = Subcat.objects.filter(catag = catag)
    subcatag = Subcat.objects.get(subcat = subcatagory)
    Qu = MCQQuestion.objects.filter(category = catag,subcat = subcatag)
    params = {
        'Qu': Qu,
        'catagory' : catag,
        'subcat' : subcatagories,
        'subcatag' : subcatag
    }
    return render(request, 'test_yourself/catagories.html', params)

def test(request,cat,subcat):
    catag = Category.objects.get(category = cat)
    subcatag = Subcat.objects.get(subcat = subcat)
    Qu = MCQQuestion.objects.filter(category = catag, subcat = subcatag).order_by('?')[:20]
    params = {
        'Qu': Qu,
        'catagory' : catag,
        'subcatagory' : subcatag
    }
    return render(request, 'test_yourself/test.html', params)

def checkquestion(request,cat,subcat):
    answ = []
    correct_ans = []
    score = 0
    for radio_answer in [key for key in request.POST.keys() if key.startswith('answers[')]:
        answ.append(radio_answer)
    for correct_answers in [key for key in request.POST.keys() if key.startswith('correct_answer[')]:
        correct_ans.append(correct_answers)

    selectans = []
    rightans = []

    for selec in answ:
        chk = request.POST[selec]
        selectans.append(chk)

    for right in correct_ans:
        get = request.POST[right]
        rightans.append(get)

    for check in range(0,len(answ)):
        if selectans[check] == rightans[check]:
            score = score + 1

    params = {
        'user_selected': selectans,
        'right_answer': rightans,
        'score' : score,
        'catagory' : cat,
        'subcatagory' : subcat
    }

    return render(request,'test_yourself/final_result.html', params)

