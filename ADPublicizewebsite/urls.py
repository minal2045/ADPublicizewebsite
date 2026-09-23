from django.contrib import admin
from django.urls import path
from ADPublicize import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('advpage/', views.advpage),
    path('pubpage/', views.pubpage),
    path('advreg', views.advreg, name='advreg'),
    path('pubreg', views.pubreg, name='pubreg'),
    path('login', views.clientlogin),
    path('logout', views.logout),
    path('contform', views.contform),
    path('adadvpage', views.adadvpage),
    path('addlocation', views.addlocation),
    path('viewloc', views.viewloc),
    path('advviewloc', views.advviewloc),
    path('pubdetails', views.pubdetails),
    path('advertiserprofile', views.advertiserprofile),
    path('publisherprofile', views.publisherprofile),
    path('advrequest', views.advrequest),
    path('requestdtl', views.requestdtl),
    path('requestdtlinpub', views.requestdtlinpub),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("admin_logout/", views.admin_logout, name="admin_logout"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin_advertisers/", views.admin_advertisers, name="admin_advertisers"),
    path("edit_advertiser/<int:id>/", views.edit_advertiser, name="edit_advertiser"),
    path("delete_advertiser/<int:id>/", views.delete_advertiser, name="delete_advertiser"),
    path("admin_publishers/", views.admin_publishers, name="admin_publishers"),
    path("edit_publisher/<int:id>/", views.edit_publisher, name="edit_publisher"),
    path("delete_publisher/<int:id>/", views.delete_publisher, name="delete_publisher"),
    path("admin_locations/", views.admin_locations, name="admin_locations"),
    path("edit_location/<int:id>/", views.edit_location, name="edit_location"),
    path("delete_location/<int:id>/", views.delete_location, name="delete_location"),
    path("admin_requests/", views.admin_requests, name="admin_requests"),
    path("edit_request/<int:id>/", views.edit_request, name="edit_request"),
    path("delete_request/<int:id>/", views.delete_request, name="delete_request"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
