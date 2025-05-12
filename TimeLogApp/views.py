from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
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
            createdBy="Guru"
        )

        return JsonResponse({"message": f"User '{user.userName}' created successfully."})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def user_data_api(request):
    users = UserProfile.objects.filter(createdBy="Guru").values(
        'teamMemberId',
        'userName', 'email', 'mobileNumber', 'team',
        'teamLead', 'isActive', 'isActiveRemarks',
        'isAccountLocked', 'isAccountLockedRemarks',
        'createdBy'
    )
    return JsonResponse(list(users), safe=False)

def update(request):
    return render(request,'update.html')

def update_user(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(UserProfile, teamMemberId=user_id)
        print("user",user.email)
        print(user_id)
        return render(request, 'update.html', {'user': user,'user_id': user_id})

    if request.method == 'PUT':
        print("put request received")
        try:
            data = json.loads(request.body)
            user = get_object_or_404(UserProfile, teamMemberId=user_id)
            if not user:
                return JsonResponse({"error": "User not found."}, status=404)
            user.userName = data.get("username", user.userName)
            user.email = data.get("email", user.email)
            user.mobileNumber = data.get("mobile", user.mobileNumber)
            user.team = data.get("team", user.team)
            user.teamLead = data.get("team_lead", user.teamLead)
            user.isActive = data.get("is_active", "").lower() == "yes"
            user.isActiveRemarks = data.get("remarks", "")
            user.isAccountLocked = data.get("is_locked", "").lower() == "yes"
            user.isAccountLockedRemarks = data.get("remarks_locked", "")
            user.save()
            print(data)
            print(user)
            return JsonResponse({"message": f"User '{user.userName}' updated successfully."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def delete_user(request, user_id):
    if request.method == "DELETE":
        try:
            user = get_object_or_404(UserProfile, teamMemberId=user_id)
            user.delete()
            return JsonResponse({"message": "User deleted successfully."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)

# Optional detail endpoint
def get_user_detail(request, user_id):
    user = get_object_or_404(UserProfile, teamMemberId=user_id)
    return JsonResponse({
        "id": user.teamMemberId,
        "userName": user.userName,
        "email": user.email,
        "mobileNumber": user.mobileNumber,
        "team": user.team,
        "teamLead": user.teamLead,
        "isActive": user.isActive,
        "isActiveRemarks": user.isActiveRemarks,
        "isAccountLocked": user.isAccountLocked,
        "isAccountLockedRemarks": user.isAccountLockedRemarks,
    })