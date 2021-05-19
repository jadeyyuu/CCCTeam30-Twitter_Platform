# func_list = ['payroll_line_Barwon_South_West', 'monthly_covidTweets_Bar', 'monthly_dist_pie', 'payroll_line_Gippsland', \
#     'payroll_line_Grampians', 'payroll_line_Greater_Melbourne', 'payroll_line_Hume', 'payroll_line_Loddon_Mallee']
func_list = ['age_pie_Barwon_South_West',
 'payroll_line_Greater_Melbourne',
 'Map_bySuburb_August',
 'age_pie_Gippsland',
 'Map_bySuburb_September',
 'Map_bySuburb_October',
 'Map_bySuburb_June',
 'Map_bySuburb_December',
 'Map_bySuburb_November',
 'Map_bySuburb_March',
 'payroll_line_Hume',
 'age_pie_Loddon_Mallee',
 'monthly_covidTweets_Bar',
 'payroll_line_Gippsland',
 'age_pie_Grampians',
 'Map_bySuburb_April',
 'payroll_line_Loddon_Mallee',
 'Map_bySuburb_July',
 'age_pie_Greater_Melbourne',
 'Map_bySuburb_May',
 'payroll_line_Grampians',
 'age_pie_Hume',
 'monthly_dist_pie',
 'payroll_line_Barwon_South_West']



html_format = ['<!DOCTYPE HTML>\n', '<html>\n', '<head>\n', '  <meta charset="utf-8">\n', '  <meta name="viewport" content="width=device-width, initial-scale=1">\n', '  <title>test</title>\n', '</head>\n', '<body>\n', '  {% autoescape off %}\n', '  {{ plt_div }}\n', '  {% endautoescape %}\n', '</body>\n', '</html>']

for each in func_list:
    with open(f'/Users/yuxuanliu/Documents/Documents - Yuxuan’s MacBook Pro/GitHub/CCC-Group-Project/ccc_backend/ccc_backend/templates/{each}.html', 'w', encoding='utf-8') as f:
        for ele in html_format:
            if ele == '  {{ plt_div }}\n':
                tmp = '  {{ ' + f'{each}' + ' }}\n'
                f.write(tmp)
            else:
                f.write(ele)
