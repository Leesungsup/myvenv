from django import forms

#클라이언트 화면에 입력 폼
#데이터 전처리
class AddProductForm(forms.Form):
    quantity=forms.IntegerField()
    is_update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
