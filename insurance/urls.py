from django.urls import path
from django.contrib.auth.views import LogoutView
from .  import views

urlpatterns=[
    path("index",views.StartingPage,name="index"),
    path("",views.LoginClass.as_view(),name="login"),
    path("history/",views.historytables,name="requests"),
    path("ext/",views.extends,name="extensions"),
    path("request/",views.InsuranceRequest.as_view(),name="request"),
    path("accept/",views.admin_requests,name="accept"),
    path('process_request/', views.process_request, name='process_request'),
    path('sign-up/',views.SignUpClass.as_view(),name="signup"),
    path("info/", views.UserInfoClass.as_view(), name="information"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('success/',views.success, name='success'),


]