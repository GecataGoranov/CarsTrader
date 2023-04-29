from django import forms
from .models import Car

class FilterForm(forms.ModelForm):
    eurostandards = [
        (1, "Euro 1"),
        (2, "Euro 2"),
        (3, "Euro 3"),
        (4, "Euro 4"),
        (5, "Euro 5"),
        (6, "Euro 6"),
        
    ]
    

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

        self.fields["manufacturer"].widget = forms.Select(choices=[("", "---------------------------")])
        self.fields["model"].widget = forms.Select(choices=[("", "---------")])
        self.fields["eurostandard"].widget = forms.Select(choices=self.eurostandards)

        
    class Meta:
        model = Car
        exclude = ("price", "region", "place", "picture", "seller")
        fields = "__all__"

    
class PublishForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PublishForm, self).__init__(*args, **kwargs)
        self.fields["production_date"] = forms.DateField()
        self.fields["production_date"].widget.attrs.update({"type":"date"})


    class Meta:
        model = Car
        exclude = ("seller",)
        fields = "__all__"