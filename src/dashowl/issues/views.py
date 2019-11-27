from django.shortcuts import render
from github import Github
import requests
import json
from .models import Issue
from .. import secret


#É nescessario passar para as todas essas funcoes o request ?
#Faltando criar as variaveis para o repositorio, acces_token do github e do zenhub , etc


def get_issues(request):

    g = Github(secret.login, secret.password)
    repo = g.get_repo("fga-eps-mds/2019.2-DashboardAgil-Wiki")
    """
        dar um jeito de pegar o id do repositório atual
    """


    if bool(Issue.objects.filter(repository__repositoryID=repo.id)):
        all_issues = Issue.objects.filter(repository__repositoryID=repo.id)

        author1 = Issue.objects.filter(repository__repositoryID=repo.id, author = 'Matheus-AM')
        author2 = Issue.objects.filter(repository__repositoryID=repo.id, author = 'KalebeLopes')
        author3 = Issue.objects.filter(repository__repositoryID=repo.id, author = 'joao15victor08')
        author4 = Issue.objects.filter(repository__repositoryID=repo.id, author = 'ailamaralves')
        author5 = Issue.objects.filter(repository__repositoryID=repo.id, author = 'muriloschiler')
        author6 = Issue.objects.filter(repository__repositoryID=repo.id, author = 'damarcones')

        date1o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=1)
        date2o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=2)
        date3o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=3)
        date4o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=4)
        date5o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=5)
        date6o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=6)
        date7o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=7)
        date8o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=8)
        date9o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=9)
        date10o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=10)
        date11o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=11)
        date12o = Issue.objects.filter(repository__repositoryID=repo.id, date__month=12)

        date1c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=1, state='closed')
        date2c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=2, state='closed')
        date3c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=3, state='closed')
        date4c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=4, state='closed')
        date5c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=5, state='closed')
        date6c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=6, state='closed')
        date7c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=7, state='closed')
        date8c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=8, state='closed')
        date9c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=9, state='closed')
        date10c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=10, state='closed')
        date11c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=11, state='closed')
        date12c = Issue.objects.filter(repository__repositoryID=repo.id, date__month=12, state='closed')


    else:
        raise TypeError

#Retorna o valor de cada issue
    req= requests.get('https://api.zenhub.io/p1/repositories/206358281/issues/39?access_token=02a009e06e4926091eadce6ef1dffc9f9b3f7b5bd417b116ea90c55bf6fb68dda7eb367ab6544c07')
    issue_json = req.json()
    point_issue = issue_json["estimate"]["value"]

    return render(request, 'issues.html', {'all_issues': all_issues, 'author1': author1,'author2': author2,'author3': author3,'author4': author4,'author5': author5,'author6': author6,
     'date1o': date1o, 'date2o': date2o,'date3o': date3o,'date4o': date4o,'date5o': date5o,'date6o': date6o,
    'date7o': date7o,'date8o': date8o,'date9o': date9o,'date10o': date10o,'date11o': date11o,'date12o': date12o, 'date1c': date1c, 'date2c': date2c,
    'date3c': date3c,'date4c': date4c,'date5c': date5c,'date6c': date6c, 'date7c': date7c,'date8c': date8c,'date9c': date9c,'date10c': date10c,
    'date11c': date11c,'date12c': date12c})


