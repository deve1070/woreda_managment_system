from django.db.models.signals import post_save,post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User,Group,Permission
from .models import Profile,CustomUser
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a Profile only if the user is a resident
        if instance.role == 'resident':
            Profile.objects.create(user=instance)
    else:
        # Ensure the profile exists before attempting to save it
        if hasattr(instance, 'profile'):
            instance.profile.save()


@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    resident_group, _ = Group.objects.get_or_create(name='Resident')
    staff_group, _ = Group.objects.get_or_create(name='Staff')
    admin_group, _ = Group.objects.get_or_create(name='Admin')

    # Assign permissions
    content_type = ContentType.objects.get_for_model(CustomUser)

    resident_group.permissions.set([
        Permission.objects.get_or_create(codename='view_own_profile', name='Can view own profile', content_type=content_type)[0],
        Permission.objects.get_or_create(codename='update_own_profile', name='Can update own profile', content_type=content_type)[0],
    ])

    staff_group.permissions.set([
        Permission.objects.get_or_create(codename='post_announcement', name='Can post announcements', content_type=content_type)[0],
        Permission.objects.get_or_create(codename='update_request_status', name='Can update request status', content_type=content_type)[0],
    ])

    admin_group.permissions.set([
        *staff_group.permissions.all(),
        Permission.objects.get_or_create(codename='manage_staff', name='Can manage staff', content_type=content_type)[0],
    ])
