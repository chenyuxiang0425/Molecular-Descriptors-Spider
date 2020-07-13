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
        length = each_data_length*i + i * 1000 + first_index
        create_thread(run, length, each_data_length, './data/'+str(first_index)+"/Descriptor"+str(i)+".csv")


if __name__ == '__main__':
    start(50, 20680, 390)
