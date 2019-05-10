from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # exL /polls/
    path('', views.index, name='index'),
    # exL /polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # exL /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # exL /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]