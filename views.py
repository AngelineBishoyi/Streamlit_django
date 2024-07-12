# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer

# class MyModelCreateView(APIView):
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"Data stored sucessfully....!"}, status=status.HTTP_201_CREATED)
#         return Response({"message":"Please check the code....!"}, status=status.HTTP_400_BAD_REQUEST) 

#     def get(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         try:
#             instance = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"Data updated successfully....!"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             instance = Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Response({"message": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
#         instance.delete()
#         return Response({"message":"Data deleted successfully....!"}, status=status.HTTP_200_OK)


# students/views.py
# students/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# students/views.py

from django.shortcuts import render

def student_management_view(request):
    return render(request, 'students/index.html')

