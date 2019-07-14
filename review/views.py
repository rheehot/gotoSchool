from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm

def list(request):
    reviews = Review.objects
    return render(request, 'list.html', {'reviews':reviews})

def show(request, review_id):
    review_show = get_object_or_404(Review, pk = review_id)
    return render(request, 'show.html', {'review':review_show})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
        return render(request, 'new.html', {'form':form }) #form : not valid
    else:
        form = ReviewForm()
        return render(request, 'new.html', {'form':form })

def edit(request):
    return render(request, 'edit.html')

def update(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method=='POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('show', review_id=review.pk)
    else:
        form = ReviewForm(instance=review)
        return render(request, 'edit.html', {'form':form})

def delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('list')