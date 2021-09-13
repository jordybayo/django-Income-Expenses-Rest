# from django.shortcuts import render
# import datetime
# from expenses.models import Expenses
# from rest_framework.views import APIView
# from rest_framework import response, status

# # Create your views here.
# class ExpenseSummaryStats(APIView):

#     def get_amount_for_category(self, expense_list, category) :
#         expenses =  expense_list.filter(category=category)
#         amount = 0

#         for expense in expenses:
#             amount += expense.amount
#         return {'amount': amount,}

#     def get_category(self, request):
#         return request.category

#     def get(self, request):
#         todays_date = datetime.date.today()
#         ayear_ago=todays_date - datetime.timedelta(days=365)
#         expenses=Expenses.objects.filter(
#             owner=request.user, date__range=[ayear_ago,todays_date])

#         final = {}
#         categories = list(set(map(self.get_category, expenses)))
        
#         for expense in expenses:
#             for category in categories:
#                 final[category] = self.get_amount_for_category(expenses, category) 
                
#         return response.Response({'category_data':final}, status=status.HTTP_200_OK)

