from django.urls import path

from agency.views import (
    index,
    NewspapersCreateView,
    NewspapersListView,
    NewspapersUpdateView,
    NewspapersDeleteView,
    RedactorsListView,
    RedactorsCreateView,
    RedactorsUpdateView,
    RedactorsDeleteView,
    TopicsListView,
    TopicsCreateView,
    TopicsUpdateView,
    TopicsDeleteView,
    RedactorsDetailView,
    TopicsDetailView,
    NewspapersDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspapersListView.as_view(), name="newspapers-list"),
    path("newspapers/create/", NewspapersCreateView.as_view(), name="newspapers-create"),
    path("newspapers/<int:pk>/", NewspapersDetailView.as_view(), name="newspapers-detail"),
    path("newspapers/<int:pk>/update/", NewspapersUpdateView.as_view(), name="newspapers-update"),
    path("newspapers/<int:pk>/delete/", NewspapersDeleteView.as_view(), name="newspapers-delete"),
    path("redactors/", RedactorsListView.as_view(), name="redactors-list"),
    path("redactors/create/", RedactorsCreateView.as_view(), name="redactors-create"),
    path("redactors/<int:pk>/", RedactorsDetailView.as_view(), name="redactor-detail"),
    path("redactors/<int:pk>/update/", RedactorsUpdateView.as_view(), name="redactors-update"),
    path("redactors/<int:pk>/delete/", RedactorsDeleteView.as_view(), name="redactors-delete"),
    path("topics/", TopicsListView.as_view(), name="topics-list"),
    path("topics/create/", TopicsCreateView.as_view(), name="topics-create"),
    path("topics/<int:pk>/", TopicsDetailView.as_view(), name="topics-detail"),
    path("topics/<int:pk>/update/", TopicsUpdateView.as_view(), name="topics-update"),
    path("topics/<int:pk>/delete/", TopicsDeleteView.as_view(), name="topics-delete"),

]
