from django.shortcuts import redirect, render

from employee.models import Rental, Car
from user.models import CustomUser, Role, RoleEnum
from user.views import get_custom_user_roles


def index(request):
    # check user
    if not request.user.is_authenticated:
        return redirect('user:login')
    user_roles = get_custom_user_roles(request.user.id)
    if request.user.is_superuser:
        return redirect('/admin/')
    if not user_roles['is_owner']:
        return redirect('home:index')
    # get all()
    reservations = Rental.objects.all()
    cars = Car.objects.all()
    users = CustomUser.objects. \
        exclude(is_superuser=True). \
        exclude(is_staff=True). \
        exclude(roles__in=Role.objects.filter(
        name__in=(
            RoleEnum.CLIEN.value,

        )
    )
    )

    return render(
        request,
        'employee/index.html',
        {
            # employee
            'employee_name': request.user.first_name + ' ' + request.user.last_name,
            'employee_avatar_url': CustomUser.objects.get(id=request.user.id).picture.url,
            'is_owner': user_roles['is_owner'],

        }
    )
