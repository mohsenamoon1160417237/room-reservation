from rest_framework.response import Response


def register(data, serializer_class, user_type):
    serializer_data = {
        'username': data['username'],
        'password': data['password'],
        'user_type': user_type
    }

    serializer = serializer_class(data=serializer_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = Response()
    serializer_data.pop('password')
    response.data = serializer_data
    response.data['status'] = 'registered'
    return response
