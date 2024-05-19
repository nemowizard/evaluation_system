from django.shortcuts import render, get_object_or_404
from .models import QualEval
from django.core import serializers
import pandas as pd
import numpy as np

# 정성평가 첫화면
def index(request):
    qualEval_list = QualEval.objects.order_by('-create_date')
    context = {'qualEval_list': qualEval_list}
    return render(request, 'IPWeb/qualEval_list.html', context)

def detail(request, qualEval_id):
    qualEval = get_object_or_404(QualEval, pk=qualEval_id)
    context = {'qualEval': qualEval}
    print(context)
    return render(request, 'IPWeb/qualEval_detail.html', context)

def graph(request):
    datas = QualEval.objects.all().values()
    df = pd.DataFrame(datas)
    qualEval_group_office = pd.pivot_table(df, index='office_name', columns='category', values='ID_num', aggfunc='count')
    qualEval_group_office = qualEval_group_office.fillna(0.0)
    qualEval_group_office_dict = qualEval_group_office.to_dict(orient="index")

    datapoints=[]
    for qualEval_key, qualEval_value in qualEval_group_office_dict.items():
        datapoints.append({ 'label': qualEval_key, 'y': qualEval_value['개선']})
    print(datapoints)
    datapoints2=[]
    for qualEval_key, qualEval_value in qualEval_group_office_dict.items():
        datapoints2.append({ 'label': qualEval_key, 'y': qualEval_value['모범']})
    print(datapoints2)
    
    return render(request, 'IPWeb/qualEval_graph.html', { "datapoints" : datapoints, "datapoints2": datapoints2 })                        