import re
from  comment import  pre_process
if __name__ == '__main__':
 my_file_path = 'F:\\tongxue\\zhangyi\\eng_train2.txt'
 save_file_path = 'F:\\tongxue\\zhangyi\\3.txt'
# 打开文件
 my_file = open(my_file_path, 'r', encoding='utf-8')
# 只保留英文、数字和空格换行的正则表达式
 #cop = re.compile(u'[^0-9a-zA-Z\']+', re.UNICODE)

 cop=re.compile(u"^[a-zA-Z?><;,{}[\]\-_+=!@#$%\^&*|'\s)]*$",re.UNICODE)
 # 只保留中文、数字.的正则表达式
 #cop = re.compile(u'[^0-9\u4E00-\u9FA5\']+', re.UNICODE)


 for line in my_file.readlines():
    string = cop.sub("", line)
    string=pre_process.prepare_text_for_lda(string)
    save_file = open(save_file_path, 'a', encoding='utf-8')
    save_file.write(string)
    save_file.flush()
    save_file.close()

# ascii(my_file.read(3)[0]) 获取unicode编码
# 关闭文件
 my_file.close()
