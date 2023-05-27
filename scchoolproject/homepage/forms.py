from django import forms
from . models import Department,Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=('department','courses')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fielda['department'].queryset = Department.objects.none()

        if department in self.data:
            try:
                dept_id=int(self.data.get('department'))
                self.fields['courses'].queryset = Course.objects.filter(dept_id=dept_id)
            except (valueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['courses'].queryset = Course.objects.filter(dept_id=dept_id)