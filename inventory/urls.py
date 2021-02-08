"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from django.conf import settings
from django.conf.urls.static import static
from stockmgmt.views import home,list_item,add_items,update_items,delete_items,stock_detail,issue_items,receive_items,reorder_level,list_history


urlpatterns = [
    # authentications
    path('login/', LoginView.as_view(template_name='add_item.html',), name='login'),
    path('logout/', LogoutView.as_view(template_name='add_item.html'), name='logout'),
    # module path
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list_item/', list_item, name='list_item'),
    path('add_items/', add_items, name='add_items'),
    path('update_items/<str:pk>/', update_items, name="update_items"),
    path('delete_items/<str:pk>/', delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', stock_detail, name="stock_detail"),
    path('issue_items/<str:pk>/', issue_items, name="issue_items"),
    path('receive_items/<str:pk>/',receive_items, name="receive_items"),
    path('reorder_level/<str:pk>/', reorder_level, name="reorder_level"),
    path('list_history/', list_history, name='list_history'),



]

if settings.DEBUG:
    urlpatterns = urlpatterns +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
