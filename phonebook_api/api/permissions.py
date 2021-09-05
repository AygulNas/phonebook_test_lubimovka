from rest_framework import permissions


class IsAllowedChangeCompanies(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
           or request.method == 'POST'):
            return True
        return (view.action in ['update', 'partial_update', 'destroy'] and
                (request.user == obj.creator))
