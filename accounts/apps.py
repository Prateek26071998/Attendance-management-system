from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        import os
        import sys

        # Run only on Render server
        if os.environ.get("RENDER") != "true":
            return

        # Prevent running during migrations
        if "migrate" in sys.argv:
            return

        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()

            users_data = [
                {"username": "HR", "password": "Hr@12345", "role": "HR"},
                {"username": "EMPLOYEE1", "password": "Emp1@12345", "role": "EMPLOYEE"},
                {"username": "EMPLOYEE2", "password": "Emp2@12345", "role": "EMPLOYEE"},
                {"username": "EMPLOYEE3", "password": "Emp3@12345", "role": "EMPLOYEE"},
            ]

            for user_data in users_data:
                if not User.objects.filter(username=user_data["username"]).exists():
                    user = User.objects.create_user(
                        username=user_data["username"],
                        password=user_data["password"],
                        role=user_data["role"]
                    )
                    print(f"✅ Created user: {user.username}")

        except Exception as e:
            print("User auto-create skipped:", e)