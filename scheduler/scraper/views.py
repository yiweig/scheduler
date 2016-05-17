from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Department


def index(request):
    department_list = Department.objects.order_by('abbreviation')
    # template = loader.get_template('scraper/index.html')
    context = {'department_list': department_list}

    # output = ', '.join([d.abbreviation for d in department_list])

    # return HttpResponse(template.render(context=context, request=request))
    return render(request=request, template_name='scraper/index.html', context=context)


def detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    context = {'department': department}
    return render(request=request, template_name='scraper/detail.html', context=context)


def results(request, department_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % department_id)


def vote(request, department_id):
    return HttpResponse("You're voting on question %s." % department_id)
