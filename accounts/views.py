from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from accounts.forms import UserAdminCreationForm
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status

class PermList(ListAPIView):
    permission_classes(IsAuthenticated, )
    def get(self, request):
        logged_in_user = request.user
        pdata = logged_in_user.get_all_permissions()
        print(logged_in_user.is_superuser)
        print(pdata)
        print(len(pdata))
        return Response(({"result": "OK", "taskType": "tasktype"}), status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# def get(request):
#         logged_in_user = request.user
#         pdata = logged_in_user.get_all_permissions()
#         print(logged_in_user.is_superuser)
#         print(pdata)
#         print(len(pdata))
#         form = UserAdminCreationForm()
#         return render(request, 'register.html', {'form': form})

# def register(req):
#     form = UserAdminCreationForm()
#     logged_in_user = req.user
#     pdata = logged_in_user.get_all_permissions()
#     print(logged_in_user.is_superuser)
#     print(pdata)
#     print(len(pdata))
#     if req.method == 'POST':
#         form = UserAdminCreationForm(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('register')
#     return render(req, 'register.html', {'form': form})