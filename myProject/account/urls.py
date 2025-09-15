from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signin/', views.signin_view, name="signin"),
    path('singout/', views.signout_view, name="signout"),
    path('signup/', views.signup_view, name="signup"),
    path('createPost/', views.create_post, name="createPost"),
    path('home/', views.home_view, name="home"),
    path('profile/', views.profile_view, name="profile"),
    path('editProfile/', views.edit_profile, name="editProfile"),
    path('delete/<int:post_id>/', views.delete_post, name="deletePost"),
    path('edite/<int:post_id>/', views.edite_post, name="editePost"),
    path('like/<int:post_id>/', views.post_like, name="postLike"),

]
