from os import walk
import json
from django.shortcuts import render
from django.http import HttpResponse
import plotly.io as pio
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly


_, _, filenames = next(walk('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2'))

with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Barwon South West.json') as f:
    for each in f:
        data = each
        data = json.loads(each)

def pics_show(request):
    plt_div = plotly.offline.plot(data,output_type='div')
    return render(request, 'pics_show.html', context={'plt_div':plt_div})