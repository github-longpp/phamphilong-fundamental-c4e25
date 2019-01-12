from gmail import *
from random import *
from datetime import *
sickness_list = ["Thương hàn" , "Kiết lị" , "Tiêu chảy"]
html = ''' 
<p>ABC abc<strong>&nbsp;</strong></p>
<p><strong>ABC abc<span style="text-decoration: underline;">&nbsp;</span></strong></p>
<p><strong><span style="text-decoration: underline;">ABC abc</span>&nbsp;</strong></p>
<p><strong><em>ABC abc&nbsp;</em></strong></p>
<p><strong><em><span style="text-decoration: underline;">ABC abc</span></em>&nbsp;</strong></p>
<p><strong>ABC abc&nbsp;</strong></p> 
'''
ch = choice(sickness_list)
html_content = html.replace("ABC" , ch)
print(html_content)
now = datetime.now()
once = True
while once:
    if now.hour >= 7:
        gmail = GMail('Pham Phi Long<20158235@student.hust.edu.vn>','neverchange')
        msg = Message('Send email',to='qhuydtvt@gmail.com',text="ABC abc ABC abc ABC abc ABC abc ABC abc ABC abc ", html= html_content)
        gmail.send(msg)
        once = False   


