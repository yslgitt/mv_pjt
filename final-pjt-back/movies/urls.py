from django.urls import path
from . import views

urlpatterns = [
    # 영화 리스트를 가져올 때, view에서 추천 로직을 짜는가 vue에서 짜는가
    path('', views.movie_list),
    path('recommendation/like/', views.recommendation_like),
    path('recommendation/watch/', views.recommendation_watch),
    path('boxoffice/', views.boxoffice_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/like/', views.like_movie),
    path('<int:movie_id>/watch/', views.watch_movie),
    path('<int:person_pk>/person/', views.person_detail),
    path('<int:movie_id>/review/', views.review_create),
    path('<int:movie_id>/review/<int:review_pk>/', views.review_update_or_delete),
    path('<int:movie_id>/review/<int:review_pk>/like/', views.like_review),
]
