# Molecular-Descriptors-Spider
一个获取化学分子描述符数据 ([米兰比可卡大学地球与环境科学系](http://michem.disat.unimib.it/mole_db/)) 的多线程Python爬虫程序。

简介：

- 使用Requests模拟HTTP请求/响应，Beautiful Soup 4提取页面信息。
- 使用Python内置的Thread多线程爬取速度。
- 用csv文件存储数据。

## 环境依赖
- beautifulsoup4
- requests

## 使用方法
安装模块：
```
$ pip install -r requirments.txt
```
运行：
```
$ python main.py
```
## 数据
根据 http://michem.disat.unimib.it/mole_db/ 的 MC number,自定义每个 csv 数据的数量和线程数。

数据获取完毕后可使用
`CSV_combination.py`中的方法进行处理，内包含合并，删除重复数据，转置三个方法。

经过处理后的数据，每列为每个分子的不同分子描述符，每行为不同的分子。
