from django.shortcuts import render
from group.models import Group
from authentication.models import CustomUser
from django.db.models import Q
from django.core.paginator import Paginator

def group_list(request, page):
    if not request.user.is_authenticated:
        groups = []
    else:
        user = CustomUser.objects.get(pk=request.user.id)
        groups = Group.objects.filter(Q(admin=user) | Q(moderators=user) | Q(members=user)).distinct()
    p = Paginator(groups, 27)
    page = p.get_page(page)

    return render(request, 'group/group_list.html', {'groups': page.object_list, 'p':page})

def group_detail(request, pk):
    group = Group.objects.get(pk=pk)
    all_members = group.members.all().union(group.moderators.all())
    
    members_with_roles = []

    for member in all_members:
        role = "Member"
        if member in group.moderators.all():
            role = "Moderator"
        if member == group.admin:
            role = "Admin"

        members_with_roles.append({'user': member, 'role': role})
        
    return render(request, 'group/group_detail.html', {'group': group, 'members_with_roles': members_with_roles})
