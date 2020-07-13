from MyCrawler import MyCrawler
import pandas as pd
import time
import random

class CrawlerRunner:
    def __init__(self):
        pass

    @staticmethod
    def dataFrameToList(dataframe, label):
        """

        :param dataframe: data frame
        :param label: what label the data frame you want to become list
        :return: list
        """
        list = []
        for index, row in dataframe.iterrows():
            list.append(row[label])
        return list

    @staticmethod
    def writeInCsv(label, listData, filename='MolecularDescriptors.csv'):
        """
        :param filename: filename
        :param label: what label you want to write to csv file
        :param listData: the values have been dealt with
        :exception : if no such file exists, we will create this file
        """
        dataframe = pd.DataFrame(listData)
        try:
            oldData = pd.read_csv(filename)
            newValues = dataframe[1]
            oldData[label] = newValues
            oldData.to_csv(filename, index=False)
        except FileNotFoundError:
            oldData = dataframe
            oldData.rename(columns={0: 'Name', 1: label}, inplace=True)
            oldData.to_csv(filename, index=False)



    @staticmethod
    def main_function(begin_index,length,filename):

        def check_symbol(symbol):
            list_a = ['Br', 'Cl', 'B', 'F', 'Si', 'P', 'Al', 'Se']
            for a in list_a:
                if symbol.count(a):
                    return True
            return False

        # dataframe = pd.read_csv('moleculeList.csv', header=0)
        URL = "http://michem.disat.unimib.it/mole_db/desc_values.php"

        groups = [1, 2, 4, 5, 6, 8, 10, 12, 15, 16, 17, 18, 20]
        # id = CrawlerRunner.dataFrameToList(dataframe, "ID")
        # name = CrawlerRunner.dataFrameToList(dataframe, "Name")
        ids = [i for i in range(begin_index, begin_index+length)]
        myCrawler = MyCrawler()
        #for (id, name) in zip(id, name):
        for id in ids:
            url = myCrawler.getUrl(URL, id, 1)
            response_for_name = myCrawler.response_for_name(url)
            # symbol
            response_for_symbol = myCrawler.response_for_symbol(url)
            time.sleep(random.randint(1, 4))
            if (response_for_name == '<b><i>No name</i></b>' ):
                print("%d pass" %(id))
                continue

            if (check_symbol(response_for_symbol)):
                print("%d has nonconforming symbol" %(id))
                continue


            for group in groups:
                url = myCrawler.getUrl(URL, id, group)
                print(url)
                coarseResponse = myCrawler.response(url)
                response = myCrawler.dealWithResponse(group, coarseResponse)
                #print(response)
            response.append(['id',id])
            response.append(['symbol',response_for_symbol])
            CrawlerRunner.writeInCsv(response_for_name, response,filename)


if __name__ == '__main__':
    CrawlerRunner.main_function(10000,11000,"test.csv")

