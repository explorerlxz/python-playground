import sqlite3
conn = sqlite3.connect('example.db')
  
c = conn.cursor()
  
#创建table
c.execute('''create table passwd (user text, note text)''')
  
# 插入数据，执行SQL语句
c.execute('''insert into passwd (user,note)  values('mPfiJRIH9T','mPfiJRIH9T')''')
c.execute('''insert into passwd (user,note)  values('7IYcUrKWbw','7IYcUrKWbw')''')
c.execute('''insert into passwd (user,note)  values('bXB9VcPdnq','bXB9VcPdnq')''')
c.execute('''insert into passwd (user,note)  values('2JFk7EWcCz','2JFk7EWcCz')''')
c.execute('''insert into passwd (user,note)  values('QeBFAlYdPr','QeBFAlYdPr')''')
c.execute('''insert into passwd (user,note)  values('bDL4T69rsj','bDL4T69rsj')''')
c.execute('''insert into passwd (user,note)  values('BOxPqmkEd9','BOxPqmkEd9')''')
c.execute('''insert into passwd (user,note)  values('rvBegjXs16','rvBegjXs16')''')
c.execute('''insert into passwd (user,note)  values('CWrhA2eSmQ','CWrhA2eSmQ')''')
c.execute('''insert into passwd (user,note)  values('qQicfV2gvG','qQicfV2gvG')''')
c.execute('''insert into passwd (user,note)  values('s3vg1EuBQb','s3vg1EuBQb')''')
c.execute('''insert into passwd (user,note)  values('Lne4xj3Xpc','Lne4xj3Xpc')''')
c.execute('''insert into passwd (user,note)  values('PH3R86CKDT','PH3R86CKDT')''')
c.execute('''insert into passwd (user,note)  values('HEK7Ymg0Bw','HEK7Ymg0Bw')''')
c.execute('''insert into passwd (user,note)  values('lim2OCxhQp','lim2OCxhQp')''')
c.execute('''insert into passwd (user,note)  values('kVFfLljBJI','kVFfLljBJI')''')
c.execute('''insert into passwd (user,note)  values('Hpbs3VOXNq','Hpbs3VOXNq')''')
c.execute('''insert into passwd (user,note)  values('f5ubmznBIE','f5ubmznBIE')''')
c.execute('''insert into passwd (user,note)  values('beJCQA2oXV','beJCQA2oXV')''')
c.execute('''insert into passwd (user,note)  values('JyPx0iTBGV','JyPx0iTBGV')''')
c.execute('''insert into passwd (user,note)  values('4S7RQTqw2A','4S7RQTqw2A')''')
c.execute('''insert into passwd (user,note)  values('ypDgkKi27e','ypDgkKi27e')''')
c.execute('''insert into passwd (user,note)  values('Anrwx8SbIk','Anrwx8SbIk')''')
c.execute('''insert into passwd (user,note)  values('k5ZJFrd8am','k5ZJFrd8am')''')
c.execute('''insert into passwd (user,note)  values('KYcTv54QVC','KYcTv54QVC')''')
c.execute('''insert into passwd (user,note)  values('Jv6OyfMA0g','Jv6OyfMA0g')''')
c.execute('''insert into passwd (user,note)  values('kpSLsQYzuV','kpSLsQYzuV')''')
c.execute('''insert into passwd (user,note)  values('u2zkJQWdOY','u2zkJQWdOY')''')
c.execute('''insert into passwd (user,note)  values('D0aspFbW8c','D0aspFbW8c')''')
c.execute('''insert into passwd (user,note)  values('CwqhvDOrWZ','CwqhvDOrWZ')''')
c.execute('''insert into passwd (user,note)  values('Tdy5LA9sWO','Tdy5LA9sWO')''')
c.execute('''insert into passwd (user,note)  values('76HnRVbLX0','76HnRVbLX0')''')
c.execute('''insert into passwd (user,note)  values('B3aoFibRPV','B3aoFibRPV')''')
c.execute('''insert into passwd (user,note)  values('7Q6lNdL5JP','7Q6lNdL5JP')''')
c.execute('''insert into passwd (user,note)  values('Hsob6Jyv4A','Hsob6Jyv4A')''')
 
 
#将变动保存到数据库文件，如果没有执行词语句，则前面的insert 语句操作不会被保存
conn.commit()
 
c.execute('''select * from passwd ''').fetchall()
#得到所有的记录
rec = c.execute('''select * from passwd''')
print(c.fetchall())
