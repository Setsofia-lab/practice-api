from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get (self, request, format=None):
       """returns a lsit of API features"""
       an_apiview =[
          'Uses HTTP method as fucntion (get, post, patch,put, delete)'
          'Is similar to a traditional Django View' 
          'Give you the most control over your app logiv'
          'Is mapped manually to urls'
       ]

       return Response({'message':'Hello', 'an_apiview': an_apiview})