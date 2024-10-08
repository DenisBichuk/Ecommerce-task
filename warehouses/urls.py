from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Stock API',
        default_version='v1',
        description='Documentation for warehouse system',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="example@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += [
                       path('__debug__/', include('debug_toolbar.urls')),
                       re_path(
                           r'^redoc/$',
                           schema_view.with_ui('redoc', cache_timeout=0),
                           name='schema-redoc'
                       ),
                       re_path(
                           r'^swagger(?P<format>\.json|\.yaml)/$',
                           schema_view.without_ui(cache_timeout=0),
                           name='schema-json'
                       ),
                       re_path(
                           r'^swagger/$',
                           schema_view.with_ui('swagger', cache_timeout=0),
                           name='schema-swagger-ui'
                       ),
                   ] + static(document_root=settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
