from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('user/create', views.create),
    path('user/go_create', views.go_create),
    path('user/<user_id>/display',views.display_buddie),
    path('user/<user_id>/edit', views.edit_user),
    path('user/<user_id>/update', views.update_user),

    path('login', views.login),
    path('logout', views.logout),

    path('hobbies/<int:hobby_id>', views.display_hobby),
    path('hobbies/<int:hobby_id>/delete', views.delete_hobby),
    path('hobbies/new', views.new),
    path('hobbies/<int:hobby_id>/edit', views.edit_hobby),
    path('hobbies/<int:hobby_id>/update', views.update_hobby),
    path('hobbies/create',views.create_hobby),
    path('hobbies/<int:hobby_id>/like', views.like),
    path('hobbies/<int:hobby_id>/dislike', views.dislike),

    path('hobbies/<int:hobby_id>/comment' ,views.post_comment),
    path('comment/<comment_id>/delete', views.delete_comment)
    
    
    
]