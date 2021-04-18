from django import forms


class user_form(forms.Form):

    #boolean_field=forms.BooleanField()




#field=forms.ChoiceField(choices=(('','--Select Option'),('1','First'),('2','Second'),('3','Third')))

    #choices=(('A','A'),('B','B'),('C','C'));

#    field=forms.ChoiceField(choices=choices,widget=forms.RadioSelect)


    """
    user_name=forms.CharField(required='True',label="Name  ",
    widget=forms.TextInput(
    attrs={'placeholder' : 'Enter Your Full Name',
    'style':'width:300px'}
    ))
    user_dob=forms.DateField(label='Date Of Birth',widget=forms.TextInput(attrs={'type':'date'}));

    user_email=forms.EmailField(label="Email  ")
    """
