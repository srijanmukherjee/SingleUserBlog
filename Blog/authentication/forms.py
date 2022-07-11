from django import forms


class UserAuthenticationForm(forms.Form):
    CLASSNAME = "input is-normal"

    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}), label='username',
                               label_suffix="", max_length=100, min_length=5, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label_suffix="", label='password', required=True,
                               min_length=8)

    template_name = 'form/UserAuthenticationForm.html'

    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input is-normal'
