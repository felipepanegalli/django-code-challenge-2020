from django.urls import include, path
from rest_framework import routers

from .views import (
    AuthorViewSet,
    BookList,
    BookDetail,
    CustomerViewSet,
    OrderViewSet,
    OrderItemsViewSet,
)

router = routers.SimpleRouter()
router.register("authors", AuthorViewSet)
router.register("customers", CustomerViewSet)
router.register("orders", OrderViewSet)
router.register("order-items", OrderItemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("books/", BookList.as_view()),
    path("books/<int:pk>", BookDetail.as_view()),
]
