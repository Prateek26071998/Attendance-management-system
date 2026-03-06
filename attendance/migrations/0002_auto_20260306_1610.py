from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE attendance_attendance RENAME COLUMN user_id TO employee_id;",
            reverse_sql="ALTER TABLE attendance_attendance RENAME COLUMN employee_id TO user_id;"
        ),
    ]