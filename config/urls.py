from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/category/', include('category.urls')),
    path('api/v1/posts/', include('post.urls')),
    path('api/v1/posts/comments/', include('comment.urls')),
]
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
