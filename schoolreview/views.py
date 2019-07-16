from django.shortcuts import render, get_object_or_404, redirect
from .models import SchoolReview
from .forms import SchoolReviewForm
# Create your views here.

def reviewlist(request):
    s_reviews = SchoolReview.objects.all()
    return render(request, 'reviewList.html', {'s_reviews': s_reviews})

def schoolshow(request, s_review_id):
    s_review = get_object_or_404(SchoolReview, pk = s_review_id)
    return render(request, 'schoolshow.html', {'s_review': s_review})

def schoolnew(request):
    return render(request, 'schoolnew.html')

def schoolcreate(request):
    if request.method == 'POST':
        form = SchoolReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reviewList')
    else:
        form = SchoolReviewForm()
        return render(request, 'schoolnew.html', {'form': form})

def schooledit(request):
    return render(request, 'schooledit.html')

def schoolupdate(request, s_review_id):
    s_review = get_object_or_404(SchoolReview, pk = s_review_id)
    if request.method == 'POST':
        form = SchoolReviewForm(request.POST, instance=s_review)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('schshow', s_review_id=s_review.pk)
    
    else:
        form = SchoolReviewForm(instance=s_review)
        return render(request, 'schooledit.html', {'form': form})

def schooldelete(request, s_review_id):
    s_review = get_object_or_404(SchoolReview, pk = s_review_id)
    s_review.delete()
    return redirect('reviewList')