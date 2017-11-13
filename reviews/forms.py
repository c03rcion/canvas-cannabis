from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User
from reviews.models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "method",
            "content",
            "photo",
            "rating",
        ]

    def save(self):
        instance = super(ReviewForm, self).save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "body"
        ]
