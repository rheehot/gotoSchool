from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from membership.models import Member

def list(request):
    reviews = Review.objects.all()
    user = request.user
    interest = user.interest
    interests = []

    a = len(interest)
    for i in range(a):
        if interest[i] == '1':
            interests.append('건국대학교')
        elif interest[i] == '2':
            interests.append('서울대학교')
        elif interest[i] == '3':
            interests.append('성신여자대학교')
        elif interest[i] == '4':
            interests.append('숙명여자대학교')
        elif interest[i] == '5':
            interests.append('한국산업기술대학교')
            
    reviews = reviews.filter(univ__in=interests)
    search2 = request.GET.get('search_coursename', None)
    if search2 :
        reviews = reviews.filter(coursename__icontains=search2)
        return render(request, 'list.html', {'reviews' : reviews})
    else :
        return render(request, 'list.html', {'reviews': reviews})

def alllist(request):
    reviews = Review.objects.all()
    search2 = request.GET.get('search_coursename', None)
    if search2 :
        reviews = reviews.filter(coursename__icontains=search2)
        return render(request, 'alllist.html', {'reviews' : reviews})
    else :
        return render(request, 'alllist.html', {'reviews': reviews})

def show(request, review_id):
    user = request.user
    review_show = get_object_or_404(Review, pk = review_id)
    return render(request, 'show.html', {'review':review_show, 'user':user})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
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