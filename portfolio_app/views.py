from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio, Student, Project
from .forms import ProjectForm

# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'portfolio_app/index.html', {'portfolios': Portfolio.objects.all(), 'projects': Project.objects.all(), 'students': Student.objects.all()})

def portfolio(request, args):
   return render(request, 'portfolio_app/portfolio.html', {'portfolio':Portfolio.objects.all()[int(args)-1], 'projects': Project.objects.filter(portfolio=Portfolio.objects.all()[int(args)-1])})

def project(request, args):
   return render(request, 'portfolio_app/project.html', {'project':Project.objects.all()[int(args)-1], 'portfolio':Project.objects.all()[int(args)-1].portfolio})

def newProject(request, args):
   if (request.method=="POST"):
      form = ProjectForm(request.POST)
      if (form.is_valid()):
         project = form.save()
         return redirect('portfolio-detail', project.portfolio.id)
   else:
      form = ProjectForm()
   return render(request, 'portfolio_app/new_project.html', {'portfolio':Portfolio.objects.all()[int(args)-1], 'form':form, 'args':args})

def editProject(request, args, id):
   project=Project.objects.get(id=id)
   if (request.method == 'POST'):
        form = ProjectForm(request.POST , instance=project)
        if (form.is_valid()):
            project = form.save()
            return redirect('portfolio-detail', project.portfolio.id)
   else:
        form = ProjectForm(instance=project)
   return render(request, 'portfolio_app/edit_project.html', {'portfolio':Portfolio.objects.all()[int(args)-1], 'form':form, 'args':args})

def delProject(request, args, id):
   project=Project.objects.get(id=id)
   if (request.method == 'POST'):
      project.delete()
      return redirect('portfolio-detail', project.portfolio.id)
   return render(request, 'portfolio_app/del_project.html', {'portfolio':Portfolio.objects.all()[int(args)-1], 'args':args, 'project':project})
   