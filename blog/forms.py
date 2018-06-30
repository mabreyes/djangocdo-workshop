from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

    # Source: https://gist.github.com/rochacon/1514222
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label})
