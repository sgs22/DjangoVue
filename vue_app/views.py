from django.shortcuts import render
from .models import User

# Create your views here.
def test_vue(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, 'vue_app/test.html', context)
