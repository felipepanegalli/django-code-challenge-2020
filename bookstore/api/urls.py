from django.urls import include, path
from rest_framework import routers

from .views import AuthorViewSet, BookList, BookDetail

router = routers.SimpleRouter()
router.register("authors", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("books/", BookList.as_view()),
    path("books/<int:pk>", BookDetail.as_view()),
]
