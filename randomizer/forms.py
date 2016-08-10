from django import forms
from randomizer.models import Restaurant
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions

class RestaurantForm(forms.ModelForm):
	name = forms.CharField(required=False)
	
	class Meta:
		model = Restaurant
		fields = ('name',)
		
	helper = FormHelper()
	helper.form_class = 'form-horizontal'
	helper.label_class = 'col-lg-2'
	helper.field_class = 'col-lg-8'
	helper.form_method = 'POST'
	helper.layout = Layout(
		Field('name', css_class='input-sm', placeholder='Add a new Restaurant'),
		FormActions(Submit('submit', 'Submit', css_class='btn-primary'))
		)