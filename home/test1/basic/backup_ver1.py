import os
import time

#1.需要备份的文件与目录将被指定在一个列表中
# 例如在windows下
source = ['"C:\\My Documents"', 'C:\\Code']
# source = ['"E:\\upload"']

# 又例如在mac 和Linux下
# source = ['/Users/swa/notes']

#在这里要注意到我们必须在字符串中间使用双引号，用以括起其中包含空格的名称

# 2. 备份文件必须存储在一个主备份目录中
# 例如在windows下，
target_dir = 'E:\\Backup'
# 又例如在mac和linux下
# target_dir = '/Users/swa/backup'
# 要记得这里的目录地址改成你讲使用的路径

# 3.备份文件将打包压缩成zip文件
# 4.zip压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep +\
         time.strftime('%Y%m%d%H%M%S')+ '.zip'

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. 我们使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 6. 运行备份
print('Zip command is:')
print(zip_command)

print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('backUp falied')
