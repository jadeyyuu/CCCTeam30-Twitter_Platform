# from os import walk
# import json
# from django.shortcuts import render
# from django.http import HttpResponse
# import plotly.io as pio
# from plotly.offline import plot
# from plotly.graph_objs import Scatter
# import plotly


# _, _, filenames = next(walk('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2'))

# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Barwon South West.json') as f:
#     for each in f:
#         data = each
#         data = json.loads(each)

# def payroll_line_Barwon_South_West(request):
#     payroll_line_Barwon_South_West_ = plotly.offline.plot(data,output_type='div')
#     return render(request, 'payroll_line_Barwon_South_West.html', context={'payroll_line_Barwon_South_West':payroll_line_Barwon_South_West_})


# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/monthly_covidTweets_Bar.json') as f:
#     for each in f:
#         data_monthly_covidTweets_Bar = each
#         data_monthly_covidTweets_Bar = json.loads(each)

# def monthly_covidTweets_Bar(request):
#     monthly_covidTweets_Bar_ = plotly.offline.plot(data_monthly_covidTweets_Bar,output_type='div')
#     return render(request, 'monthly_covidTweets_Bar.html', context={'monthly_covidTweets_Bar':monthly_covidTweets_Bar_})



# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/monthly_dist_pie.json') as f:
#     for each in f:
#         data_monthly_dist_pie = each
#         data_monthly_dist_pie = json.loads(each)

# def monthly_dist_pie(request):
#     monthly_dist_pie_ = plotly.offline.plot(data_monthly_dist_pie,output_type='div')
#     return render(request, 'monthly_dist_pie.html', context={'monthly_dist_pie':monthly_dist_pie_})


# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Gippsland.json') as f:
#     for each in f:
#         data_payroll_line_Gippsland = each
#         data_payroll_line_Gippsland = json.loads(each)

# def payroll_line_Gippsland(request):
#     payroll_line_Gippsland_ = plotly.offline.plot(data_payroll_line_Gippsland,output_type='div')
#     return render(request, 'payroll_line_Gippsland.html', context={'payroll_line_Gippsland':payroll_line_Gippsland_})


# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Grampians.json') as f:
#     for each in f:
#         data_payroll_line_Grampians = each
#         data_payroll_line_Grampians = json.loads(each)

# def payroll_line_Grampians(request):
#     payroll_line_Grampians_ = plotly.offline.plot(data_payroll_line_Grampians,output_type='div')
#     return render(request, 'payroll_line_Grampians.html', context={'payroll_line_Grampians':payroll_line_Grampians_})


# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Greater Melbourne.json') as f:
#     for each in f:
#         data_payroll_line_Greater_Melbourne = each
#         data_payroll_line_Greater_Melbourne = json.loads(each)

# def payroll_line_Greater_Melbourne(request):
#     payroll_line_Greater_Melbourne_ = plotly.offline.plot(data_payroll_line_Greater_Melbourne,output_type='div')
#     return render(request, 'payroll_line_Greater_Melbourne.html', context={'payroll_line_Greater_Melbourne':payroll_line_Greater_Melbourne_})


# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Hume.json') as f:
#     for each in f:
#         data_payroll_line_Hume = each
#         data_payroll_line_Hume = json.loads(each)

# def payroll_line_Hume(request):
#     payroll_line_Hume_ = plotly.offline.plot(data_payroll_line_Hume,output_type='div')
#     return render(request, 'payroll_line_Hume.html', context={'payroll_line_Hume':payroll_line_Hume_})


# with open('/Users/yuxuanliu/Desktop/Desktop - Yuxuan’s MacBook Pro/graph_json2/payroll_line_Loddon Mallee.json') as f:
#     for each in f:
#         data_payroll_line_Loddon_Mallee = each
#         data_payroll_line_Loddon_Mallee = json.loads(each)

# def payroll_line_Loddon_Mallee(request):
#     payroll_line_Loddon_Mallee_ = plotly.offline.plot(data_payroll_line_Loddon_Mallee,output_type='div')
#     return render(request, 'payroll_line_Loddon_Mallee.html', context={'payroll_line_Loddon_Mallee':payroll_line_Loddon_Mallee_})





# funcs = dict()
# data = {}
# filenames = ['I','LOVE', 'YOU']
# for name in filenames:
#     funcs[name] = lambda x: func(x)




# def func(request, name):
#     tmp = plotly.offline.plot(data[name], output_type='div')
#     return render(request, name + '.html', context={name :tmp})