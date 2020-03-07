from lab1.MyCrawler import MyCrawler
import pandas as pd


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
    def main():
        dataframe = pd.read_csv('moleculeList.csv', header=0)
        URL = "http://michem.disat.unimib.it/mole_db/desc_values.php"

        groups = [1, 2, 4, 5, 6, 8, 10, 12, 15, 16, 17, 18, 20]
        id = CrawlerRunner.dataFrameToList(dataframe, "ID")
        name = CrawlerRunner.dataFrameToList(dataframe, "Name")

        myCrawler = MyCrawler()
        for (id, name) in zip(id, name):
            for group in groups:
                url = myCrawler.getUrl(URL, id, group)
                print(url)
                coarseResponse = myCrawler.response(url)
                response = myCrawler.dealWithResponse(group, coarseResponse)
                print(response)

            CrawlerRunner.writeInCsv(name, response)


if __name__ == '__main__':
    CrawlerRunner.main()
