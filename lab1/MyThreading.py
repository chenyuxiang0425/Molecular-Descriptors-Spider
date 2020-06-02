import threading
import lab1.CrawlerRunner


def run(begin_index, length, filename):
    lab1.CrawlerRunner.CrawlerRunner.main_function(begin_index, length, filename)


def main():
    """创建启动线程"""
    def create_thread(target, begin_index, length, filename):
        t = threading.Thread(target=target, args=(begin_index, length, filename))
        t.start()

    # 725000
    for i in range(0, 50):
        first_index, length = 20680, 390

        create_thread(run, length*i + i * 1000 + first_index, length, "20680/Descriptor"+str(i)+".csv")


if __name__ == '__main__':
    main()
