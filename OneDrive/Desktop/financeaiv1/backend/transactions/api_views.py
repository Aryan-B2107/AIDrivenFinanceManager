from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionList(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
