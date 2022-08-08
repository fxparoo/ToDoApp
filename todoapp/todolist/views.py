from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from todolist.models import Task
from todolist.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"detail": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=id, *args, **kwargs):
        try:
            task = Task.objects.get(pk=pk)
            if task.delete():
                return Response({"detail": "Task deleted Succesfully."}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({"detail": "Task does not exist."}, status=status.HTTP_400_BAD_REQUEST)
