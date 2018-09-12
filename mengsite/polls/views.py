from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import mModelForm

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Choice, Question, mModel


class myView(generic.DetailView):
    model = mModel
    template_name = 'polls/mview.html'
    # This objectname to be used in template's django code -- ie the placeholder
    # if not set, will use model name by lowercased all of the word, mModel -> mmodel
    context_object_name = 'mview_details'

class MModelListView(generic.ListView):
    template_name = 'polls/mmodel_all.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return reversed(mModel.objects.all())

    def get_context_data(self, **kwargs):
        ctx = super(MModelListView, self).get_context_data(**kwargs)
        ctx['form'] = mModelForm()
        return ctx


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # The object name for this view is the list, the list name will be used in the index.html for used in django code
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).

        __lte >>> less than equal

        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def mmodel_new(request):
#     form = mModelForm
#     return render(request, 'polls/mmodel_edit.html', {'form':form})

def mmodel_new(request):
    if request.method == "POST":
        form = mModelForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            data = form.cleaned_data
            entry.name = data['name']
            entry.gender = data['gender']
            entry.age = data['age']
            entry.email = data['email']
            entry.dob = data['dob']
            entry.job = data['job']

            entry.save()

            # remember to use namespace when finding view in redirect(), ie polls:mview
            # else will keep returning NoReverseMatch error
            return redirect('polls:mview', pk=entry.pk)

    else:
        form = mModelForm()
    return render(request, 'polls/mmodel_edit.html', {'form': form})

def mmodel_paginator(request):
    list = mModel.objects.all()
    form = mModelForm()
    paginator = Paginator(list, 3) # Show 25 items per page

    page = request.GET.get('page')
    mModelList = paginator.get_page(page)

    return render(request, 'polls/mmodel_paginator.html', {'list': mModelList, 'form':form})

def experimentalPage(request):
    path = request.path
    path_info = request.path_info
    body = request.body
    encoding = request.encoding if request.method == "ENCODING" else "None"
    content_types = request.content_type
    content_params = request.content_params
    cookies = request.COOKIES['cookie_name'] if 'cookie_name' in request.COOKIES else "None"
    host = request.get_host()
    port = request.get_port()
    get_full_path = request.get_full_path()
    build_absolute_uri = request.build_absolute_uri() # Default to get_full_path()
    is_secure = request.is_secure()
    is_ajax = request.is_ajax()

    response = render(request, 'polls/experiment.html', {'path':path,
                                                     'path_info': path_info,
                                                     'body':body,
                                                     'encoding': encoding,
                                                     'content_types': content_types,
                                                     'content_params': content_params,
                                                     'cookies': cookies,
                                                     'host': host,
                                                     'port': port,
                                                     'is_secure': is_secure,
                                                     'is_ajax': is_ajax,
                                                     'get_full_path': get_full_path,
                                                     'build_absolute_uri': build_absolute_uri,
                                                     'result': request.META.items()

                                                     })
    response.set_cookie('cookie_name', cookies)
    return response

