from django.db import models

# 정성평가
class QualEval(models.Model):
    ID_num = models.CharField(max_length=200) # 접수 ID
    category = models.CharField(max_length=200) # 카테고리 : 모범, 개선, Value-add
    stage = models.CharField(max_length=200) # 단계 초안, OA, CA
    part_name = models.CharField(max_length=200) # 파트명
    reviewer = models.CharField(max_length=200) # 검토자
    office_name = models.CharField(max_length=200) # 대리인 사무소명
    office_attorney = models.CharField(max_length=200) # 대리인
    review_date = models.DateField() # 검토일
    comment = models.TextField() # 검토 내용
    create_date = models.DateTimeField(auto_now=True) # 생성일
    
    def __str__(self):
        return self.ID_num