from django.db import models
from django.conf import settings
from membership.models import Member

class Review(models.Model):
    UNIVS = [(univ, univ) for univ in ('숙명여자대학교','성신여자대학교','서울대학교','한국산업기술대학교','건국대학교')]
    #UNIVS = [(univ, univ) for univ in ('건국대학교','서울대학교','성신여자대학교','숙명여자대학교','한국산업기술대학교')]
    YEARS = [(year, year) for year in (2018,2019)]
    SEMESTERS = [(semester, semester) for semester in ('1학기','여름학기','2학기','겨울학기')]
    ASSIGNMENTS = [(ass, ass) for ass in ('없음','적음','보통','헬')]
    TESTS = [(test, test) for test in ('없음','1회','2회','헬')]
    ATTENDENCES = [(att, att) for att in ('안봄','보는듯마는듯','깐깐')]
    STARS = [(x,str(x)) for x in range(1, 6)]
    
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    #interest = models.ForeignKey(Member, on_delete = models.CASCADE, null=True)
    univ = models.TextField(choices=UNIVS, default='숙명여자대학교') #학교
    coursename = models.CharField(max_length=30, default='강의명') #강의제목
    prof = models.CharField(max_length=30, default='교수') #교수
    courseyear = models.IntegerField(choices=YEARS, default='2019') #수강학기(년도)
    coursesemester = models.TextField(choices=SEMESTERS, default='1학기') #수강학기(학기)
    content = models.TextField(default='강의평을 작성하세요.') #강의평
    assignment = models.TextField(choices=ASSIGNMENTS, default='없음') #과제
    test = models.TextField(choices=TESTS, default='없음') #시험
    attendence = models.TextField(choices=ATTENDENCES, default='안봄') #출결
    star = models.IntegerField(choices=STARS, default=5) #별점
    recommend = models.FloatField(default=0, help_text="(updated on save)") #전체평점

    def __str__(self):
        return self.coursename

    #이렇게 만들고 싶지 않았는데,,,,, 능력부족으로,,,,, 떄려박아 보았어욥,,,,,
    def save(self, *args, **kwargs):

        self.recommend = 0

        if self.assignment == "없음":
            self.recommend += 5
        elif self.assignment == "적음":
            self.recommend += 4
        elif self.assignment == "보통":
            self.recommend += 3
        elif self.assignment == "헬":
            self.recommend += 1
            
        if self.attendence == "안봄":
            self.recommend += 5
        elif self.attendence == "보는듯마는듯":
            self.recommend += 3
        elif self.attendence == "깐깐":
            self.recommend += 1

        if self.test == "없음":
            self.recommend += 5
        elif self.test == "1회":
            self.recommend += 4
        elif self.test == "2회":
            self.recommend += 3
        elif self.test == "헬":
            self.recommend += 1
    
        self.recommend += self.star

        self.recommend /= 4
        super(Review, self).save(*args, **kwargs)
