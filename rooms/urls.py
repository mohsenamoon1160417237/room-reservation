from django.urls import path
from .views.manager.add_room import CreateUpdateDeleteRoom
from .views.manager.add_room_date_time import CreateDeleteRoomDateTime
from .views.active_rooms_list import ActiveRoomsList
from .views.create_reservation import CreateReservation
from .views.manager.reservation_list import ReservationList
from .views.manager.cancel_reservation import CancelReservation
from .views.my_reservation_list import MyReservationList
from rooms.views.change_my_reservation import ChangeMyReservation


urlpatterns = [
    path('room/add/', CreateUpdateDeleteRoom.as_view(), name='add_room'),
    path('room/date_time/add/<str:room_name>/', CreateDeleteRoomDateTime.as_view(), name='add_room_date_time'),
    path('', ActiveRoomsList.as_view(), name='active_rooms_list'),
    path('reserve/', CreateReservation.as_view(), name='create_reservation'),
    path('reservations/', ReservationList.as_view(), name='reservation_list'),
    path('reservations/cancel/', CancelReservation.as_view(), name='cancel_reservation'),
    path('my_reservations/', MyReservationList.as_view(), name='my_reservation_list'),
    path('my_reservations/change/', ChangeMyReservation.as_view(), name='change_my_reservation'),
]
