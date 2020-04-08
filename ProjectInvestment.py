

class ProjectInvestment():
    def __init__(self, name, country, score, rate, selfInvestment, back, toback):
        self.name, self.index = self.format_name(name)
        self.country = country
        self.score = score
        self.rate = self.format_rate(rate)
        self.investment = self.format_investment(selfInvestment)
        self.back = self.format_back(back)
        self.toback = self.format_back(toback)
        
    def __str__(self):
        message = ""
        message += "Entreprise: " + self.name
        message += " projet n°: " + str(self.index)
        message += " Pays: " + self.country
        message += " Score: " + self.score
        message += " Taux: " + str(self.rate) +"%"
        message += " Somme prêtée: " + str(self.investment) + '€'
        message += " Somme remboursée: " + str(self.back) + '€'
        message += " Encours: " + str(self.toback) + '€'
        return message
    
    def format_name(self, name):
        """
        Renvoit le nom de l'entreprise et le numéro du prêt
        retour(nom entreprise, n°)
        """
        company_name = name
        n = 1
        if('#' in name): #car actuelement les i-eme projets d'une entreprise sont appellés "nom de l'entreprise #i" et le premier uniquement "nom de l'entreprise"
            company_name = name.split('#')[0].rstrip()
            n = int(name.split('#')[1])
        return (company_name, n)

    def format_rate(self, rate):
        """
        Revoit le taux sous forme d'un flotant
        """
        #Actuelement le taux est donné par October.eu sous la forme "x,xx %"
        return float(rate[:-2].replace(',','.'))

    def format_investment(self, investment):
        """
        Revoit la somme prêtée sous forme d'entier
        """
        #Actuelement la somme prêtée est donné par October.eu sous la forme "xxx €"
        return int(investment[:-2])

    def format_back(self, back):
        """
        Revoit la somme remboursée sous forme d'un flotant
        """
        #Actuelement la somme remboursée est donnée par October.eu sous la forme "xx,xx €"
        return float(back[:-2].replace(',','.'))

    def format_toback(self, toback):
        """
        Revoit la somme en attente de remboursements sous forme d'un flotant
        """
        #Actuelement la somme en attente de remboursements est donnée par October.eu sous la forme "xx,xx €"
        return float(toback[:-2].replace(',','.'))