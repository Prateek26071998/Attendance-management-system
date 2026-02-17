from django.apps import AppConfig
import os

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        # Run only on Render
        if os.environ.get("RENDER") != "true":
            return

        try:
            from django.contrib.auth import get_user_model
            User = get_user_model()

            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="Admin@123"
                )
                print("✅ Admin user auto-created on Render")

        except Exception as e:
            print("⚠️ Admin auto-create skipped:", e)
