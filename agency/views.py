from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TopicsSearchForm, RedactorsSearchForm, NewspapersSearchForm
from .models import Topic, Redactor, Newspaper


@login_required
def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    num_redactors = Redactor.objects.count()
    num_newspapers = Newspaper.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_topics": num_topics,
        "num_redactors": num_redactors,
        "num_newspapers": num_newspapers,
        "num_visits": num_visits + 1,
    }

    return render(request, "agency/index.html", context=context)


class NewspapersListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspapers_list"
    template_name = "agency/newspapers_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspapersListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspapersSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = self.model.objects.all()
        title = self.request.GET.get("title")
        if title:
            return queryset.filter(title__icontains=title)
        return queryset


class NewspapersCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("agency:newspapers-list")
    context_object_name = "newspapers_form"
    template_name = "agency/newspapers_form.html"


class NewspapersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("agency:newspapers-list")


class NewspapersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("agency:newspapers-list")


class RedactorsListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactors_list"
    template_name = "agency/redactors_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorsListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorsSearchForm(
            initial={"username": username}
        )

    def get_queryset(self):
        queryset = self.model.objects.all()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class RedactorsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("agency:redactors-list")
    context_object_name = "redactors_form"
    template_name = "agency/redactors_form.html"


class RedactorsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("agency:redactors-list")
    template_name = "agency/redactors_form.html"


class RedactorsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactors-list")


class RedactorsDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    context_object_name = "redactors"
    template_name = "agency/redactor_detail.html"


class TopicsListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    paginate_by = 5
    context_object_name = "topics_list"
    template_name = "agency/topics_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopicsListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TopicsSearchForm(
            initial={"name": name}
        )

    def get_queryset(self):
        queryset = self.model.objects.all()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class TopicsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topics-list")
    context_object_name = "topics_form"
    template_name = "agency/topics_form.html"


class TopicsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topics-list")


class TopicsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("agency:topics-list")

