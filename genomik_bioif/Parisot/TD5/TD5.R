rm(list=ls())

#Différents groupes de souches d'E. coli

data <- read.table("polygensize.txt", h=T, sep = "\t")

#strain = nom de la souche
#Host..Sex : hote où la bactérie a été trouvée
#Location : Lieu de prélèvement de la bactérie
#ABCDEFG : Taille des fragments (voir carte de restriction de E. coli K12 diapo)


size = data$A+data$B+data$C+data$D+data$E+data$F+data$G
bdata <- cbind(data,size)

#1.Représenter distribution de taille des génomes des souches
barplot(bdata$size)

#2.Relation taille génome / sous-groupe
plot(x=bdata$subgroup,y=bdata$size)

#3.Trouver une corrélation particulière
plot(x=bdata$strain,y=bdata$size)
plot(x=bdata$Location,y=bdata$size)
plot(x=bdata$Host..sex.,y=bdata$size)

plot(x=bdata$A,y=bdata$B)
plot(x=bdata$A,y=bdata$C)
plot(x=bdata$B,y=bdata$C)
plot(x=bdata$B,y=bdata$D)
plot(x=bdata$B,y=bdata$G)


lm1 <- lm(bdata$A ~ bdata$B)
summary(lm1)
#Corrélation A-B ?

#Il faut essayer de trouver des corrélations entre groupes de fragments

plot((bdata$A+bdata$B) , (bdata$D+bdata$E+bdata$F+bdata$G))

#La corrélation à faire est celle entre les fragments BC et celle des fragments DEFG
#L'origine de réplication sépare BC/DEFG
#Si on agrandit BC sans toucher DEFG l'origine de réplication n'est plus en face de la terminaison.
#La réplication fonctionne mieux chez les procaryotes si c'est en face
#==> corrélation positive entre les brins BC et DEFG.