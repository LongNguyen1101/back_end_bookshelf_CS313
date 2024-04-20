from django.urls import path
from .views import api_handler
from django.conf import settings
from django.conf.urls.static import static

# URLConf
# api/
urlpatterns = [
    path('category_list/', api_handler.get_category_list, name='category_list'),

    # book
    path('books/', api_handler.get_all_books),
    path('books/<str:str_variable>/', api_handler.get_books_by_name),
    path('book_detail/<int:book_id>/', api_handler.get_book_detail),
    path('<str:category>/', api_handler.get_books_by_category),

    # order
    path('order/', api_handler.place_order),

    #recommend
    path('book_recommend/<str:book_id>/', api_handler.get_book_recommend),
    path('book_recommend_cart/<book_id_list>/', api_handler.get_book_recommend_cart),
    path('rules', api_handler.get_rules)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)