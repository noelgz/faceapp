from django.urls import path

from user import views

urlpatterns = [
    path(
        route='login/', 
        view=views.login_view, 
        name="login"
    ),

    path(
        route='logout/', 
        view=views.logout_view, 
        name="logout"
    ),

    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name="signup"
    ),

    path(
        route='profile/me/update_profile/', 
        view=views.update_profile, 
        name="update"
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )

]