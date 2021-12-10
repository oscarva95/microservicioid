from rest_framework import status, views
from authApp.models import createid
from rest_framework import mixins
from rest_framework.response import Response
from authApp.serializers.createidSerializer import createidSerializer

class createidCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = createidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {
                     "namepc": request.data["namepc"],
                     "ubicationpc": request.data["ubicationpc"],
                     }

        return Response(status=status.HTTP_201_CREATED)



    def get(self, request, format=None):
        createids = createid.objects.all()
        serializer = createidSerializer(createids, many=True)
        return Response(serializer.data)
    
   
