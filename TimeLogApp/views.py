from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import UserProfile, Team
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        request.session['username'] = username
        return redirect('dashboard') 
    return render(request, 'login.html')


def dashboard(request):
    username = request.session.get('username', 'Guest')
    return render(request, 'dashboard.html', {'username': username})

def home(request):
    return render(request,'form.html')
def grid_view(request):
    return render(request, 'grid.html')

@require_http_methods(["POST"])
@csrf_exempt
def create_user(request):
    try:
        data = json.loads(request.body)
        required_fields = ['username', 'email', 'mobile', 'employee_id', 'team', 'team_lead', 'is_active', 'remarks', 'is_locked']
        missing_fields = [field for field in required_fields if not data.get(field)]

        if missing_fields:
            return JsonResponse({"errors": {field: ["This field is required."] for field in missing_fields}}, status=400)

        if UserProfile.objects.filter(email=data["email"]).exists():
            return JsonResponse({"errors": {"email": ["This email is already in use."]}}, status=400)

        user = UserProfile.objects.create(
            userName=data["username"],
            email=data["email"],
            mobileNumber=data["mobile"],
            team=data["team"],
            teamLead=data["team_lead"],
            isActive=(data["is_active"].lower() == "yes"),
            isActiveRemarks=data.get("remarks", ""),
            isAccountLocked=(data["is_locked"].lower() == "yes"),
            isAccountLockedRemarks=data.get("remarks_locked", ""),
            createdBy="Thamarai"
        )

        return JsonResponse({"message": f"User '{user.userName}' created successfully."})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def user_data_api(request):
    users = UserProfile.objects.all().values(
        'userName', 'email', 'mobileNumber', 'team',
        'teamLead', 'isActive', 'isActiveRemarks',
        'isAccountLocked', 'isAccountLockedRemarks',
        'createdBy'
    )
    return JsonResponse(list(users), safe=False)