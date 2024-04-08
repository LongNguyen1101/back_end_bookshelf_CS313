from django.urls import path
from .views import api_handler
from django.conf import settings
from django.conf.urls.static import static

# URLConf
# api/
urlpatterns = [
    # book
    path('books/', api_handler.get_all_books),
    path('books/<str:str_variable>/', api_handler.get_books_by_name),
    path('book_detail/<int:book_id>/', api_handler.get_book_by_id),

    # order
    path('order/', api_handler.place_order)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)