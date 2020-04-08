from django.urls import path

from .views import index, by_rubric, by_vid_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<str:rubric_id>/', by_vid_rubric, name='vid_rubr'),
    path('index/', index, name='index')
    ]
