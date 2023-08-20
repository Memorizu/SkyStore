from django.contrib.auth.models import Group, Permission 


def create_moderators_group():
    """Create or get 'moderators' group for users"""
    
    moderators_group = Group.objects.get_or_create(name='модераторы')
    
    can_cancel_permission = Permission.objects.get(codename='can_cancel_publication')
    can_change_desc_permission = Permission.objects.get(codename='can_change_desc_permission')
    can_change_category_permission = Permission.object.get(codename='can_change_category_permission')
    can_view_product_detail_permission = Permission.objects.get(codename='can_view_product_detail')
    
    moderators_group.permissions.add(can_cancel_permission, can_change_category_permission, can_change_desc_permission, can_view_product_detail_permission)
    
    