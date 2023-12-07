from django import forms
from .models import EnquiryForm

class MyForm(forms.ModelForm):
    PURPOSE_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Admission', 'Admission'),
        ('Campus Facilities', 'Campus Facilities'),
        ('Transfer Policies', 'Transfer Policies'),


    ]

    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    MATERIALS_CHOICES = [
        ('notebook', 'Notebook'),
        ('pen', 'Pen'),
        ('ID CARD', 'ID CARD'),
        ('OLD GUIDE', 'OLD GUIDE'),

    ]

    materials_provide = forms.MultipleChoiceField(
        choices=MATERIALS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    DEPARTMENT_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Medicine', 'Medicine'),
        ('Bachelor', 'Bachelor')
    ]

    COURSE_CHOICES = {
        'Engineering': [
            ('Computer Engineering', 'Computer Engineering'),
            ('Chemical Engineering', 'Chemical Engineering'),
            ('Electrical Engineering', 'Electrical Engineering'),
            ('Mechanical Engineering', 'Mechanical Engineering'),
            ('Civil Engineering', 'Civil Engineering'),
        ],
        'Medicine': [
            ('MBBS', 'MBBS'),
            ('BDS', 'BDS'),
            ('Pharmacy', 'Pharmacy'),
        ],
        'Bachelor': [
            ('BBA', 'BBA'),
            ('BCA', 'BCA'),
            ('BCOM', 'BCOM'),
        ]
    }
    department_name = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    course_name = forms.ChoiceField(choices=(), required=False)

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].choices = self.COURSE_CHOICES.get('Engineering', [])
    class Meta:
        model = EnquiryForm
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address',  'department_name', 'course_name', 'purpose', 'materials_provide']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'materials_provide': forms.CheckboxSelectMultiple,
        }



