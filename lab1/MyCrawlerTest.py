from lab1.CrawlerRunner import CrawlerRunner

listData = [['MW', '1111.19'],
            ['AMW', '5.68'],
            ['Sv', '10.6'],
            ['Se', '21.06'],
            ['Sp', '11.48'],
            ['Ss', '22'],
            ['Mv', '0.5'],
            ['Me', '1'],
            ['Mp', '0.55'],
            ['Ms', '2.75'],
            ['nAT', '21'],
            ['nSK', '8']]


crawlerRunner = CrawlerRunner()
crawlerRunner.writeInCsv("DEA", listData)


