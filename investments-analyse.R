library(tidyverse)

#On fixe le dossier de ce fichier comme le dossier d'exécution du script
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

#On importe les données
investments = read.csv("investments.csv", sep=";")

#investments
summary(investments)

pdf("Rapport investissements October.eu.pdf", title="Rapport investissement October.eu", width=9, height = 8) #On enregiste tout les graphique suivant dans un pdf

plot(0:10, type = "n", xaxt="n", yaxt="n", bty="n", xlab = "", ylab = "")


text(6, 5, "Rapport sur vos investissements sur October.eu", cex = 1.5)
text(6, 3, "Git Repo: https://github.com/NandyBa/October.eu", cex = 0.5)

par(mar=c(5.1,4.1,4.1,2.1))
#Plot1
data_rate_score = investments[,c(4, 5)] #Taux du prêt selon la catégorie

data_rate_score$Score <- factor(data_rate_score$Score,c("A+","A","B+","B","C")) #On réordonne les modalités de Score de data

par(mfrow=c(2,2))
plot(data_rate_score, main="Répartition des taux des projets de votre portefeuille selon le score de ceux-ci", cex.main=0.8, xlab="Score", ylab="Taux des prêts", cex.axis=0.7, cex.lab=0.8)

#Plot2
data_rate_country = investments[,c(3, 5)] #Taux du prêt selon le pays

plot(data_rate_country, main="Répartition des taux des projets de votre portefeuille selon le pays de ceux-ci", cex.main=0.8, xlab="Pays", ylab="Taux des prêts", cex.axis=0.7, cex.lab=0.8)

#Plot 3
data = as_tibble(investments)
data_investment_country = data %>%
  group_by(Country) %>%
  mutate(total = sum(Investment)) %>%
  select(Country, total) %>%
  distinct()

countries = data_investment_country %>%
  pull(Country)
Invest = data_investment_country %>%
  pull(total)

## On augmente un petit peu ylim pour pouvoir afficher la somme investis en haut de la barre de chaque pays
ylim <- c(0, 1.1*max(Invest))
p3 = barplot(Invest, names.arg=countries, main="Répartition de votre portefeuille selon les pays", cex.main=0.8, xlab="Pays", ylab="Somme prêtée aux entreprises (en euros)", cex.axis=0.7, cex.names=0.7, width = 0.85, ylim = ylim)
text(x = p3, y = Invest, label = as.numeric(as.character(Invest)), pos = 3, cex = 0.5, col = "black")


dev.off() #On arrête d'écrire dans le pdf