from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracao/',include('administracao.urls', namespace='administracao')),
    path('api/',include('api.urls', namespace='api')),
    path('auth/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_obtain_pair_refresh'),

]
