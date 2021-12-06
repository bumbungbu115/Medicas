from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home, name="index" ),
    path('search/',views.search,name='search'),
    path('<int:id>/',views.Detailsp, name="details"),
    path('advise/<phanloai>/',views.tuvan,name="tuvan"),
    path('congdung/<congdung>/',views.congdung,name="congdung"),
    path('advisors/',views.advisorlist,name="advisor"),
    path('load-more-data',views.load_more_data,name='load_more_data'),
    path('medicine/',views.Medicine,name="medicine"),
    path('spec/',views.selection,name="selection")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)