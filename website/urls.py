from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete'),
    path('add_record', views.add_record, name='add'),
    path('update_record/<int:pk>', views.update_record, name='update'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]