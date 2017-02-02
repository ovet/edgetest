from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin_user(apps, schema_editor):
	Author = apps.get_registered_model('news', 'Author')
	User = apps.get_registered_model('auth', 'User')
	admin = User(
		username='test_user',
		email='test@edge.com',
		password=make_password('edgeOnDemand'),
		is_superuser=False,
		is_staff=True
	)
	admin.save()
	news_author = Author(
		user=admin,
		name='Test Author'
	)
	news_author.save()



class Migration(migrations.Migration):

	dependencies = [
		('news', '0001_initial')
	]

	operations = [
		migrations.RunPython(create_admin_user),
	]
