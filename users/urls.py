from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),



    path('',views.profiles,name='profiles'),
    path('profile/<str:pk>',views.userProfile,name='user-profile'),
    path('account/',views.userAccount,name='account'),
    path('edit-account/',views.editAccount,name='edit-account'),
    path('create-skills/',views.createSkill,name='create-skills'),
    path('update-skills/<str:pk>',views.updateSkill,name='update-skills'),
    path('delete-skills/<str:pk>',views.deleteSkill,name='delete-skills'),
    path('inbox/',views.inbox,name='inbox'),
    path('message/<str:pk>',views.viewMessage,name='message'),
    path('create-message/<str:pk>',views.createMessage,name='create-message'),

]
