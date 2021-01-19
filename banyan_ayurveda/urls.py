from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('landing.urls')),
    path('about/', include('about.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('newsletters/', include('newsletters.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)