import unittest
from models import news 
News = news.News


class  NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("WABC-TV","Eyewitness News","Largest container ship ever docked along east coast arrives in Elizabeth, New Jersey - WABC-TV","The Port Authority welcomed the CMA CGM Brazil to its marine terminal in Elizabeth, New Jersey.","https://abc7ny.com/cma-cgm-brazil-port-authority-largest-container-ship-docks-on-east-coast/6420397/","https://cdn.abcotvs.com/dip/images/6420416_large-container-ship-edit.jpg?w=1600","2020-09-12T23:20:45Z")



    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()