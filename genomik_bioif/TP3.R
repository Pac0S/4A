rm(list=ls())

data <- read.table("genome_size.txt", h=T, sep ='\t')
head(data)
#SP = Espèce
#GEN = nb de gènes
#G_SIZE = taille du génome mégabase
#CAT = catégorie
  #cat 1 = procaryotes
  #cat2 = eucaryotes unicellulaires
  #cat3 = invertébrés
  #cat4 = plantes
  #cat 5 = vertébrés
#ETA = Taux de mutation
#INTN = nombre d'introns en moyenne
#INTL = Taille des introns
#TEL = Taille des ET (Elements Transposables)


species <- data$SP
gen <- data$GEN
g_size <- data$G_SIZE
cat <- data$CAT
eta <- data$ETA
int_n <- data$INT_N
int_l <- data$INT_L
tel <- data$TE_N

proc <- data[data$CAT == 1,]
euc <- data[data$CAT == 2,]
inv <- data[data$CAT == 3,]
plants <- data[data$CAT == 4,]
vert <- data[data$CAT == 5,]

##Représentation du nombre de gènespar catégorie
barplot (log(data$G_SIZE),col = data$CAT)
boxplot (log(data$G_SIZE)~data$CAT)
#Les procaryotes ont peu de gènes mais il est plus difficile de faire  la différence
#entre les autres catégories

##Représentation du taux de mutation par catégorie
barplot (data$ETA,col = data$CAT)
#Trop de lignes sans la donnée du taux de mutation

reduced_data=na.omit(data[,c(1,4,5)])
ordered_reduced <- reduced_data[rev(order(reduced_data$ETA)),]
dim(reduced_data)

barplot(ordered_reduced$ETA, col = ordered_reduced$CAT, log = 'y')

#On veut faire un test de corrélation.
#La première hypothèse est que les données soient normales
#On n'a pas vérifié si les données étaient normales
#Test de Shapiro

shapiro.test(data$G_SIZE)
#p-val < 5%  donc H0 : Les données sont normales est rejetée

#On essaye de transformer les données pour les rendre normales
shapiro.test(log10(data$G_SIZE)) #Toujours pas
shapiro.test(log10(data$ETA)) #Distribution des catégories normale en log10

#On utilise un test non paramétrique car les données de taille de genome ne sont pas normales

cor.test(log10(data$G_SIZE), log10(data$ETA), method = "spearman")
#Rho = facteur de corrélation
#H0 : rho = 0 : il n'y a pas de corrélation
#Conclusion : Il y a une corrélation entre la taille du génome et le taux de mutation


reduced_ten <- na.omit(data[c(1,3,8)])
plot(log(reduced_ten$TE_N)~log(reduced_ten$G_SIZE))

lm_ten<-lm(log(reduced_ten$TE_N)~log(reduced_ten$G_SIZE))

