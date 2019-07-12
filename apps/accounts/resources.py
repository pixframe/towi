# THIRD APP IMPORTS
from import_export import resources

# TOWI IMPORTS
from .models import Children, User


class ChildrenResource(resources.ModelResource):
    class Meta:
        model = Children
        fields = [
            'id', 'first_name', 'last_name', 'dob', 'grade', 'genre',
            'laterality', 'videogames_usage', 'learning_disabilities',
            'failed_grades', 'school', 'school__name', 'school__type',
            'school__regular_special', 'school__mixed_differetiated',
            'school__city', 'user'
        ]


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'user_type',
            'date_joined',
        )

    def after_save_instance(self, instance, using_transactions, dry_run):
        password = instance.password
        instance.set_password(password)
        instance.save()
