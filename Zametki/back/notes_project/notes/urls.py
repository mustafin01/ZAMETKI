# notes/urls.py
from django.urls import path
from .views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),
]
