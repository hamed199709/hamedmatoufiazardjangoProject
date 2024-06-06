from django.shortcuts import render
from .forms import UserCommentForm
from .models import Comment
from django.http import HttpResponse


def user_comment(request):
    if request.method == 'POST':
        form_comment = UserCommentForm(request.POST)
        if form_comment.is_valid():
            data = form_comment.cleaned_data
            Comment.objects.create(
                firstname=data['firstname'],
                lastname=data['lastname'],
                email=data['email'],
                comment=data['comment']
            )
            return HttpResponse('Your comment submitted')
    else:
        form_comment = UserCommentForm()
    return render(request, 'comments/comments.html', {'form_comment': form_comment})


