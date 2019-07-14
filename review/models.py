from django.db import models

class Review(models.Model):
    UNIVS = [(univ, univ) for univ in ('숙명여자대학교','성신여자대학교','서울대학교','한국산업기술대학교','건국대학교')]
    YEARS = [(year, year) for year in (2018,2019)]
    SEMESTERS = [(semester, semester) for semester in ('1학기','여름학기','2학기','겨울학기')]
    STARS = [(x,str(x)) for x in range(1, 6)]

    univ = models.TextField(choices=UNIVS, default='숙명여자대학교') #학교
    coursename = models.CharField(max_length=30, default='강의명') #강의제목
    prof = models.CharField(max_length=30, default='교수') #교수
    courseyear = models.IntegerField(choices=YEARS, default='2019') #수강학기(년도)
    coursesemester = models.TextField(choices=SEMESTERS, default='1학기') #수강학기(학기)
    content = models.TextField(default='강의평을 작성하세요.') #강의평
    star = models.IntegerField(choices=STARS, default=5) #별점

    def __str__(self):
        return self.coursename