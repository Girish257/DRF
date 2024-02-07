from . import views
from django.urls import path

urlpatterns = [
    # path('homepage/', views.homepage, name='posts_home'),
    # path("", views.list_posts, name='list_posts'),
    # path("<int:post_id>", views.post_details, name='post_details'),
    # path("update/<int:post_id>/", views.update_post, name='update_post'),
    # path("delete/<int:post_id>/", views.delete_post, name='delete_post'),

    # for class based function urls

    # path("", views.PostListCreateView.as_view(), name='list_posts'),
    # path("<int:post_id>/", views.PostRetrieveUpdateDeleteView.as_view(), name='update_delete_posts'),
    
    # For Generic API Views
    path("", views.PostListCreateGenericView.as_view(), name='list_posts'),
    path("<int:pk>/", views.PostRetrieveUpdateDeleteGenericView.as_view(), name='update_delete_posts'),


]


# djaneiro extension for auto-write
#  pip install black - for formatted code
