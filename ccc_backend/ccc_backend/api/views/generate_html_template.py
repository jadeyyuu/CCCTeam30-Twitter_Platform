func_list = ['payroll_line_Barwon_South_West', 'monthly_covidTweets_Bar', 'monthly_dist_pie', 'payroll_line_Gippsland', \
    'payroll_line_Grampians', 'payroll_line_Greater_Melbourne', 'payroll_line_Hume', 'payroll_line_Loddon_Mallee']

html_format = ['<!DOCTYPE HTML>\n', '<html>\n', '<head>\n', '  <meta charset="utf-8">\n', '  <meta name="viewport" content="width=device-width, initial-scale=1">\n', '  <title>test</title>\n', '</head>\n', '<body>\n', '  {% autoescape off %}\n', '  {{ plt_div }}\n', '  {% endautoescape %}\n', '</body>\n', '</html>']

for each in func_list:
    with open(f'/Users/yuxuanliu/Documents/Documents - Yuxuan’s MacBook Pro/GitHub/CCC-Group-Project/ccc_backend/ccc_backend/templates/{each}.html', 'w', encoding='utf-8') as f:
        for ele in html_format:
            if ele == '  {{ plt_div }}\n':
                tmp = '  {{ ' + f'{each}' + ' }}\n'
                f.write(tmp)
            else:
                f.write(ele)
