from django.shortcuts import render
from github import Github
from .models import Milestone
from .. import secret
from ..repositories.models import Repository


def get_milestone(request):
    
    if 'id' not in request.session:
        if request.method == 'GET' and 'id' in request.GET:

            user_login = request.session['login']
            token = request.session['token']

            repo_id = request.GET["id"]

            request.session['id'] = repo_id

            token = request.session['token']

            g = Github(token)
            
            repo = g.get_repo(full_name_or_id=int(repo_id))

            repository = Repository.objects.get(repositoryID=repo.id)
            if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
                refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestone_number)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            else:
                save_milestone(repo, repository)
                milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
                milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
                milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

            return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})
        else:
            sem_id = "Selecione um repositório"
            return render(request, 'milestone.html', {'id':sem_id})
    else:
        user_login = request.session['login']
        token = request.session['token']

        repo_id = request.session['id']

        token = request.session['token']

        g = Github(token)
        
        repo = g.get_repo(full_name_or_id=int(repo_id))

        repository = Repository.objects.filter(repositoryID=repo.id)
        if bool(Milestone.objects.filter(repository__repositoryID=repo.id)):
            milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
            refresh_milestones(repo, list(milestones)[-1].repository, list(milestones)[-1].milestone_number)
            milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
            milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
            milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

        else:
            save_milestone(repo, repository)
            milestones = Milestone.objects.filter(repository__repositoryID=repo.id).order_by('milestone_number')
            milestones_open = Milestone.objects.filter(repository__repositoryID=repo.id, state='open')
            milestones_closed = Milestone.objects.filter(repository__repositoryID=repo.id, state='closed')

        return render(request, 'milestone.html', {'milestones': milestones, 'milestones_open': milestones_open, 'milestones_closed': milestones_closed})
       