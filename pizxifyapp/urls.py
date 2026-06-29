from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('photographer-dashboard/', views.photographer_dashboard, name='photographer_dashboard'),
    path('client-dashboard/', views.client_dashboard, name='client_dashboard'),
    path('freelance-dashboard/', views.freelance_dashboard, name='freelance_dashboard'),




    #Photographer
    path('photographer-profile/',views.photographer_profile,name='photographer_profile'),
    path('create-folder/', views.create_folder, name='create_folder'),
    path('view-folders/', views.view_folders, name='view_folders'),
    path('edit-folder/<int:id>/', views.edit_folder, name='edit_folder'),
    path('delete-folder/<int:id>/', views.delete_folder, name='delete_folder'),
    path('folder/<int:id>/',views.folder_details,name='folder_details'),
    path('folder/<int:id>/upload/',views.upload_folder_photos,name='upload_folder_photos'),
    path('delete-photo/<int:id>/',views.delete_photo,name='delete_photo'),
    path('create-album/<int:folder_id>/',views.create_album,name='create_album'),
    path('save-crop/',views.save_crop,name='save_crop'),
    path('rotate-photo/',views.rotate_photo,name='rotate_photo'),
    path('update-photo-order/',views.update_photo_order,name='update_photo_order'),
    path('preview-album/<int:id>/', views.preview_album, name='preview_album'),
    path('album-designer/<int:id>/',views.album_designer,name='album_designer'),
    path('generate-album/<int:id>/',views.generate_album,name='generate_album'),
    path('view-album/<int:id>/',views.view_album,name='view_album'),
    path('my-albums/',views.my_albums,name='my_albums'),
    path('delete-album/<int:id>/',views.delete_album,name='delete_album'),
    path('download-album-pdf/<int:id>/<str:orientation>/', views.download_album_pdf, name='download_album_pdf'),
    path('album-share/<uuid:token>/', views.album_share, name='album_share'),

    #Client
    path('access-folder/', views.access_folder, name='access_folder'),
    path('folder-gallery/<int:id>/', views.folder_gallery, name='folder_gallery'),
    path('toggle-like/<int:photo_id>/', views.toggle_like, name='toggle_like'),
    path('client-albums/<int:folder_id>/', views.client_albums, name='client_albums'),
    path('client-view-album/<int:id>/',views.client_view_album,name='client_view_album'),
    path('client-download-album-pdf/<int:id>/<str:orientation>/',views.client_download_album_pdf,name='client_download_album_pdf'),
    path('client-profile/', views.client_profile, name='client_profile'),
    path('favorite-photos/',views.favorite_photos,name='favorite_photos'),

    #Freelance
    path('freelance-profile/', views.freelance_profile, name='freelance_profile'),
    path('update-freelance-profile/', views.update_freelance_profile, name='update_freelance_profile'),
    path('freelance-create-folder/', views.freelance_create_folder, name='freelance_create_folder'),
    path('freelance-view-folders/', views.freelance_view_folders, name='freelance_view_folders'),
    path('freelance-edit-folder/<int:id>/', views.freelance_edit_folder, name='freelance_edit_folder'),
    path('freelance-delete-folder/<int:id>/', views.freelance_delete_folder, name='freelance_delete_folder'),
    path('freelance-folder-details/<int:id>/',views.freelance_folder_details,name='freelance_folder_details'),
    path('freelance-upload-photos/<int:id>/',views.freelance_upload_photos,name='freelance_upload_folder_photos'),
    path('freelance-delete-photo/<int:id>/',views.freelance_delete_photo,name='freelance_delete_photo'),
    path('freelance/create-album/<int:folder_id>/', views.freelance_create_album, name='freelance_create_album'),
    path('freelance/album-designer/<int:id>/', views.freelance_album_designer, name='freelance_album_designer'),
    path('freelance/preview-album/<int:id>/', views.freelance_preview_album, name='freelance_preview_album'),
    path('freelance/generate-album/<int:id>/', views.freelance_generate_album, name='freelance_generate_album'),
    path('freelance/save-crop/',views.freelance_save_crop,name='freelance_save_crop'),
    path('freelance/update-photo-order/',views.freelance_update_photo_order,name='freelance_update_photo_order'),
    path('freelance/rotate-photo/',views.freelance_rotate_photo,name='freelance_rotate_photo'),
    path('freelance/view-album/<int:id>/', views.freelance_view_album, name='freelance_view_album'),
    path('freelance/my-albums/', views.freelance_my_albums, name='freelance_my_albums'),
    path('freelance/delete-album/<int:id>/', views.freelance_delete_album, name='freelance_delete_album'),
    path('freelance/download-album-pdf/<int:id>/<str:orientation>/',views.freelance_download_album_pdf,name='freelance_download_album_pdf'),
    path('freelance/share/<uuid:token>/',views.freelance_album_share,name='freelance_album_share'),
]