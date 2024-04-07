from django.urls import path
from .views import BookHandler
from django.conf import settings
from django.conf.urls.static import static

# URLConf
# api/
urlpatterns = [
    # book
    path('books/', BookHandler.get_all_book),
    path('books/<str:str_variable>/', BookHandler.get_books_by_name),
    path('book_detail/<int:book_id>/', BookHandler.get_books_by_id)

    #
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)