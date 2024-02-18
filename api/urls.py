from rest_framework.routers import DefaultRouter

from api import views

router=DefaultRouter()
router.register("v1/books",views.BookViewSetView,basename="books")

urlpatterns=[

] +router.urls