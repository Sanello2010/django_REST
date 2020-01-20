from rest_framework import views, response, permissions


class ObjectShowMixin:
    model = None
    id_obj = None
    serializer_get = None
    serializer_post = None
    name = None

    def get(self, request):
        if request.GET.get(self.id_obj):
            id_object = request.GET.get(self.id_obj)
            if self.model.objects.filter(id=id_object):
                object_1 = self.model.objects.get(id=id_object)
                serializer_class = self.serializer_get(object_1)
                return response.Response(serializer_class.data)
            else:
                return response.Response({"status": f"{self.name} not found"})
        else:
            all_of_objects = self.model.objects.all()
            serializer_class = self.serializer_get(all_of_objects, many=True)
            return response.Response(serializer_class.data)

    def post(self, request):
        ser = self.serializer_post(data=request.data)
        if ser.is_valid():
            ser.save()
            return response.Response({'status': "Done"})
        return response.Response({"status": "Error"})
