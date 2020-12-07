from django import forms
from .models import Memo

class PostForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['content']
        widgets = {
            'content': forms.Textarea
        }

CHOICE_FIELD_RECODE_NUMBERS = (
    ('10', '10件'),
    ('15', '15件'),
    ('30', '30件'),
)

class RecordNumberForm(forms.Form):
    record_number = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}),
        choices=CHOICE_FIELD_RECODE_NUMBERS
    )

CHOICE_FIELD_ORDER_OPTION = (
    ('False', '古い順'),
    ('True', '新着順'),

)

class OrderOptionForm(forms.Form):
    order_option = forms.ChoiceField(
        widget=forms.Select(attrs={'onchange': 'submit(this.form)'}),
        choices=CHOICE_FIELD_ORDER_OPTION
    )