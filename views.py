from . models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from . serializers import *
from rest_framework.permissions import IsAuthenticated


@permission_classes(IsAuthenticated)
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'DELETE', 'PUT'])
    

    def api(request, id=None):
        if request.method == 'GET':
            if id:
                try:
                    instance =model_class.objects.get(id=id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            if id:
                try:
                    instance =model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
                
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'})
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})
    return api

manage_department= generic_api(Department, DepartmentSerializer)
manage_role= generic_api(Role, RoleSerializer)
manage_staff= generic_api(Staff, StaffSerializer)
manage_shift= generic_api(Shift, ShiftSerializer)
manage_attendance= generic_api(Attendance, AttendanceSerializer)
        
