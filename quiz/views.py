from rest_framework import generics
from .models import (
    Category,
    Quiz,
    Question,
    Option
)

from .serializers import (
    CategorySerializer,
    QuizSerializer
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
