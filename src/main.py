import threading
import CrawlerRunner


def run(begin_index, length, filename):
    CrawlerRunner.CrawlerRunner.main_function(begin_index, length, filename)


def create_thread(target, begin_index, length, filename):
    t = threading.Thread(target=target, args=(begin_index, length, filename))
    t.start()


def start(number_of_threading, first_index, each_data_length):
    """创建启动线程"""
    for i in range(0, number_of_threading):
        first_index_for_each_one = each_data_length * i + first_index # 计算每个线程的初始 index
        create_thread(run, first_index_for_each_one, each_data_length, './data/'+str(first_index)+"/Descriptor"+str(i)+".csv")


if __name__ == '__main__':
    number_of_threading = input("你想开几个线程(how many threads you want?)10~100:")
    first_index = input("你想获取的第一个分子库的MC number是哪个(which is you first 'MC number' you want in its library ?)10000~500000:")
    each_data_length = input("每个线程你想获取多少个分子就停止？(how many molecular you want for each thread?10~100):<1000(大于1000，csv读写困难)")
    start(int(number_of_threading), int(first_index), int(each_data_length))
