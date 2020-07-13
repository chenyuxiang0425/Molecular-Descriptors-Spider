import re
import os
import pandas as pd
import glob

def combine(in_dir= './1finish/',out_dir = 'result.csv'):
    csv_list = glob.glob(in_dir + '*.csv')  # 查看同文件夹下的csv文件数
    print(u'共发现%s个CSV文件' % len(csv_list))
    print(u'正在处理............')
    for i in csv_list:  # 循环读取同文件夹下的csv文件
        fr = open(i, 'rb').read()
        with open(out_dir, 'ab') as f:  # 将结果保存为result.csv
            f.write(fr)
    print(u'合并完毕！')

def remove_duplicates(in_filename='./result.csv'):
    frame = pd.read_csv(in_filename)
    frame.drop_duplicates(subset=None, keep='first', inplace=True)
    print(u'完毕！')

def transpose(in_dir='./1/', out_dir='./1finish/'):
    filenames_in = in_dir  # 输入文件的文件地址
    filenames_out = out_dir  # 新文件的地址
    pathDir = os.listdir(filenames_in)
    for allDir in pathDir:
        child = re.findall(r"(.+?).csv", allDir)  # 正则的方式读取文件名，去扩展名
        if len(child) > 0:  # 去掉没用的系统文件
            newfile = ''
            needdate = child  #### 这个就是所要的文件名
        domain1 = os.path.abspath(filenames_in)  # 待处理文件位置
        info = os.path.join(domain1, allDir)  # 拼接出待处理文件名字
        domain2 = os.path.abspath(filenames_out)  # 处理完文件保存地址
        outfo = os.path.join(domain2, allDir)  # 拼接出新文件名字
        print(info, "开始处理")
        # ------省略数据处理过程----------------------
        df = pd.read_csv(info)
        data = df.values
        index1 = list(df.keys())
        data = list(map(list, zip(*data)))
        data = pd.DataFrame(data, index=index1)
        data.to_csv(outfo, encoding='utf-8')  # 将数据写入新的csv文件
        print(info, "处理完")


if __name__ == '__main__':
    do_transpose_combine_remove_duplicate = False
    combine_remove_duplicate_result = True
    if do_transpose_combine_remove_duplicate:
        for i in range(19, 23):
            transpose(in_dir='./'+str(i)+'/', out_dir='./'+str(i)+'finish/')
            combine('./'+str(i)+'finish/', './result/result'+str(i)+'.csv')
            remove_duplicates(in_filename='./result/result'+str(i)+'.csv')

    if combine_remove_duplicate_result:

        combine(in_dir='./result/', out_dir='./result/result.csv')
        remove_duplicates(in_filename='./result/result.csv')
