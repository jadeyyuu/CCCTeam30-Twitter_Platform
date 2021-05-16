from django.urls import path, re_path
from ccc_backend.api.views.yangjing import *

urlpatterns = [
    path('pic/payroll_line_Barwon_South_West', payroll_line_Barwon_South_West),
    path('pic/monthly_covidTweets_Bar', monthly_covidTweets_Bar),
    path('pic/monthly_dist_pie', monthly_dist_pie),
    path('pic/payroll_line_Gippsland', payroll_line_Gippsland),
    path('pic/payroll_line_Grampians', payroll_line_Grampians),
    path('pic/payroll_line_Greater_Melbourne', payroll_line_Greater_Melbourne),
    path('pic/payroll_line_Hume', payroll_line_Hume),
    path('pic/payroll_line_Loddon_Mallee', payroll_line_Loddon_Mallee),
]