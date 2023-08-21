
from typing import Any, Optional
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        
        user = User.objects.create(
            email='admin@gmail.com',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True, 
            is_active=True
        )
        
        user.set_password('testtest1234')
        user.save()

        