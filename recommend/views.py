from django.shortcuts import render
from .models import Review    
from collections import Counter
import itertools

# Create your views here.
def topfive(request):
    recommend = Review.objects.all().order_by('-recommend')
    recommend = recommend[:5]
    return render(request, 'topfive.html', {'recommend':recommend})

def schoolfive(request):
    #kunkuk = ['숙명여자대학교', '서울대학교', '성신여자대학교' , '서울산업기술대학교']
    #sookmyung = ['서울대학교', '건국대학교', '성신여자대학교' , '서울산업기술대학교']
    #seoul = ['숙명여자대학교', '건국대학교', '성신여자대학교' , '서울산업기술대학교']
    #sungshin = ['건국대학교', '숙명여자대학교', '서울대학교', '서울산업기술대학교']
    #kpu = ['숙명여자대학교', '서울대학교', '성신여자대학교' , '건국대학교']
    #순서는 숙명, 성신, 서울, 산기, 건국
    value = {
        '숙명여자대학교' : Counter({
            '숙명여자대학교' : 0,
            '성신여자대학교' : 1,
            '서울대학교' : 2,
            '서울산업기술대학교' : 0.5,
            '건국대학교' : 1.5}),
        '성신여자대학교' : Counter({
            '숙명여자대학교' : 1.5,
            '성신여자대학교' : 0,
            '서울대학교' : 1,
            '서울산업기술대학교' : 0.5,
            '건국대학교' : 2}),
        '서울대학교' : Counter({
            '숙명여자대학교' : 2,
            '성신여자대학교' : 1,
            '서울대학교' : 0,
            '서울산업기술대학교' : 0.5,
            '건국대학교' : 1.5}),
        '서울산업기술대학교' : Counter({
            '숙명여자대학교' : 2,
            '성신여자대학교' : 1,
            '서울대학교' : 1.5,
            '서울산업기술대학교' : 0,
            '건국대학교' : 0.5}),
        '건국대학교' : Counter({
            '숙명여자대학교' : 2,
            '성신여자대학교' : 1,
            '서울대학교' : 1.5,
            '서울산업기술대학교' : 0.5,
            '건국대학교' : 0})
    }
    
    sook_count = Review.objects.filter(univ='숙명여자대학교').count()
    sung_count = Review.objects.filter(univ='성신여자대학교').count()
    seo_count = Review.objects.filter(univ='서울대학교').count()
    kpu_count = Review.objects.filter(univ='서울산업기술대학교').count()
    kun_count = Review.objects.filter(univ='건국대학교').count()
    count = Counter({
        '숙명여자대학교' : sook_count,
        '성신여자대학교' : sung_count,
        '서울대학교' : seo_count,
        '서울산업기술대학교' : kpu_count,
        '건국대학교' : kun_count})

    search1 = request.GET.get('select_univ', None)
    your_choice = search1
    if search1 :
        result = value[search1]
        result = Counter({k:result[k]*count[k] for k in count})
        schools = result.most_common()
     

        schoolList = dict(schools)
        key = list(schoolList.keys())
        topthree = []

        for i in range(3):
            topthree.append(key[i])

        #schools = sorted(result.items(), key=operator.itemgetter(1),reverse = True)
        return render(request, 'schoolfive.html', {'choice' : your_choice, 'schools' : schools, 'topthree':topthree,})
    else :
        return render(request, 'schoolfive.html',{'choice' : your_choice})