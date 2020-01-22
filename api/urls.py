"""dj_backend URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from users.views import UserViewSet
from bill.views import BillViewSet
from categories.views import CategoriesViewSet,CategoriesIdViewSet
from events.views import EventsViewSet,EventsIdViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bill', BillViewSet)
router.register(r'categories', CategoriesViewSet,)
router.register(r'events', EventsViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', ObtainAuthToken.as_view()),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token',TokenObtainPairView.as_view()),
    # path('api/token/refresh',TokenRefreshView.as_view()),

    path('?P<^events/{pk}/$',EventsIdViewSet.as_view()),
    # path('^categories/{basename}/$',CategoriesIdViewSet.as_view),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]
