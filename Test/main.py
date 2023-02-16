import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Testing that the anchor tags are not dead and link to real github pages
class AnchorTagsAlive(unittest.TestCase):

    #def setUp(self):
    # def __init__(self, driver):
    #     super().__init__()
    #     driver=webdriver.Chrome(executable_path="chromedriver")
    #     self.driver = driver
    #     #self.driver.get("https://mbengtanyi.github.io/")
    #     self.base_url = "https://mbengtanyi.github.io/"
    
    def __init__(self, driver):
        driver = webdriver.Chrome(executable_path="chromedriver")
        self.driver = driver
        self.base_url ="https://mbengtanyi.github.io/"
        #self.verificationErrors = []


    def test_title(self):
        time.sleep(2)
        self.assertTrue("Tanyi Mbeng - Portfolio", self.driver.title)

        # elem = driver.find_element(By.NAME, "q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # self.assertNotIn("No results found.", driver.page_source)

    def test_data_vis_card_anchor(self):
        # driver = self.driver
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, '//*[@id="two"]/div/article[1]/h3/a')
        expected = 'https://github.com/mbengtanyi/Data-Visualisation-App'
        self.assertTrue(expected, actual)

    def tearDown(self): 
        self.driver.close()
        
# class MainPageTags(unittest.TestCase):
#     #Testing the title
#     def test_title(self):
#         driver = self.driver
#         driver.get("https://mbengtanyi.github.io/")
#         time.sleep(3)
#         self.assertTrue("Tanyi Mbeng - Portfolio", driver.title) 
    
#     # Testing the cards title tags
#     def test_cards_title(self):
#         driver = self.driver
#         driver.get("https://mbengtanyi.github.io/")
#         time.sleep(3)
#         self.assertTrue("Tanyi Mbeng - Portfolio", driver.title) 
    

if __name__ == "__main__":
    unittest.main()