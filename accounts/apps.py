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

            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@gmail.com",
                    password="Admin@123"
                )
                print("✅ Admin user auto-created on Render")

        except Exception as e:
            print("Admin auto-create skipped:", e)