from selenium import webdriver
from time import sleep
import csv

from secret import username, password
from ProjectInvestment import ProjectInvestment

class October():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def getDriver(self):
        return self.driver

    def login(self):
        self.driver.get('https://app.october.eu/login')
        sleep(3)
        
        username_input = self.driver.find_element_by_xpath('//*[@name="email"]')
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_xpath('//*[@name="password"]')
        password_input.send_keys(password)
        
        login_btn = self.driver.find_element_by_xpath('//*[@class="actions"]/button')
        login_btn.click()

    def wait_until_page_has_loaded(self):
        # on attend que la page soit chargée
        while(not('pace-done' in self.driver.find_element_by_css_selector('body').get_attribute("class"))):
            sleep(1)   
        
    def getOrwnInvestments(self):
        self.wait_until_page_has_loaded() # on attend que la page soit chargée

        sleep(3) #On attend quelques secondes avant de changer de page afin de récupérer les tokens d'identification
        self.driver.get('https://app.october.eu/transactions/loans')

        self.wait_until_page_has_loaded() # on attend que la page soit chargée

        load_all_projects_btn = self.driver.find_element_by_class_name('load-more')
        load_all_projects_btn.click()
        
        Investments = []
        table = self.driver.find_element_by_class_name('investment-table')

        for row in table.find_elements_by_xpath(".//ul")[1: ]: #la première ligne contient les labels des colonnes du tableau
            
            #On récupère l'ensemble des projets
            li_tab = row.find_elements_by_xpath(".//li")
            
            name = li_tab[0].find_element_by_class_name('project-name').text
            
            country = ""
            flag_class = li_tab[0].find_elements_by_xpath(".//strong/i")[0].get_attribute("class")

            if 'icon-flag fr' in flag_class:
                country = 'France'

            elif 'icon-flag es' in flag_class:
                country = 'Espagne'

            elif 'icon-flag it' in flag_class:
                country = 'Italie'

            elif 'icon-flag es' in flag_class:
                country = 'Espagne'

            elif 'icon-flag nl' in flag_class:
                country = 'Pays-Bas'

            else:
                raise ValueError("projet d'un pays inconnu")

            score = li_tab[1].text
            rate = li_tab[2].text
            investment = li_tab[3].text
            back = li_tab[4].text
            toback = li_tab[5].text

            investment = ProjectInvestment(name, country, score, rate, investment, back, toback)
            Investments.append(investment)
        return Investments

    def createInvestmentsCsv(self):
        Investments = self.getOrwnInvestments()
        with open('investments.csv', 'w', newline='') as csvfile:
            thewriter = csv.writer(csvfile, delimiter=';', dialect='excel')

            thewriter.writerow(['Company name', 'Project number', 'Country', 'Score', 'Rate', 'Investment', 'Back', 'Toback'])
            
            for investment in Investments:
                thewriter.writerow([investment.name, investment.index, investment.country, investment.score, investment.rate,
                                    investment.investment, investment.back, investment.toback])
        

app = October()
app.login()
app.createInvestmentsCsv()
