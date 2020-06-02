import requests
from bs4 import BeautifulSoup,NavigableString,Tag


class MyCrawler:
    def __init__(self):
        self.headers = {'User-Agent':
                            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                            'Chrome/39.0.2171.71 Safari/537.36'}
        # list of values from website
        self.list = []
        # check connect status
        self.NETWORK_STATUS = True

    def getUrl(self, url, id, group):
        """
        :return: return the url of the target website
        """
        id = str(id)
        group = str(group)
        return url + "?id=" + id + "&desc_group=" + group

    def response(self, url):
        """
        :param url: the target url
        :return: return the source code of the website
        """
        response = self.avoidTimeOut(url, 20)
        soup = BeautifulSoup(response.text, 'html.parser')
        tr = soup.find('table').find_all('tr')
        return tr

    def response_for_name(self, url):
        """
        :param url: the target url
        :return: return the source code of the website
        """
        response = self.avoidTimeOut(url, 20)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('b')
        return str(name)

    def response_for_symbol(self, url):
        """
        :param url: the target url
        :return: return the symbol of the website
        """
        response = self.avoidTimeOut(url, 20)
        soup = BeautifulSoup(response.text, 'html.parser')
        new_soup = str(soup).replace("</sub>", "").replace("<sub>","")
        index = 0
        for br in BeautifulSoup(new_soup, 'html.parser').findAll('br'):
            if (index == 2):
                next = br.nextSibling
                return next
            index +=1

    def dealWithResponse(self, group, response):
        """
        deal with the sourse code of the website to bring what values we want
        :param response:the sourse of the website
        :return: return values in tabels
        """
        if group == 1:
            self.list = []
        for j in response[1:]:
            td = j.find_all('td')
            Name = td[1].get_text().strip()
            Value = td[2].get_text().strip()
            # 写入标签
            #Des = td[3].get_text().strip()
            #self.list.append([Name, Value,Des])
            self.list.append([Name, Value])
        return self.list


    def avoidTimeOut(self, url, times):
        """
        :param url: target webiste
        :param times: maximun times to try to conntect to url
        :exception : Read timed out
        """
        for i in range(1, times+2):
            if not self.NETWORK_STATUS:
                print('Time out，reconnected %s times. (total %s times)' % (i - 1, times))
                self.NETWORK_STATUS = True
            try:
                res = requests.get(url, params={"show_ram": 1}, headers=self.headers, timeout=(5, 10))
                if res.status_code == 200:
                    return res
            except Exception as e:
                print(str(e))
                self.NETWORK_STATUS = False
