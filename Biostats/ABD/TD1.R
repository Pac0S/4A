library(ade4)

rm(list=ls())
data("iris")

#CROISEMENT DE DEUX VARIABLES QUALITATIVES

cramer <- function(x,y) {
  res <- chisq.test(x,y, correct=FALSE)
  chi2 <- as.numeric(res$statistic)
  n <- length(x)
  p <- length(levels(x)) 
  q <- length(levels(y))
  m <- min(p-1,q-1)
  V <- sqrt( chi2 / (n*m) )
  return(V)
}

#CROISEMENT D'UNE VARIABLE QUALITATIVE ET D'UNE VARIABLE QUANTITATIVE

vartot <- function(x) {res <- sum((x-mean(x))^2) ; return(res)}

varinter <- function(x,gpe) {
  moyennes <- tapply(x,gpe,mean)
  effectifs <- tapply(x,gpe,length)
  res <- (sum(effectifs*(moyennes-mean(x))^2))
  return(res)
}

eta2 <- function(x,gpe) {res <- varinter(x,gpe)/vartot(x) ; return(res)}


graphnf <- function(x,gpe) {
  stripchart(x~gpe)
  points(tapply(x,gpe,mean),1:length(levels(gpe)),col="red",pch=19,cex=1.5)
  abline(v=mean(x),lty=2)
  moyennes <- tapply(x,gpe,mean)
  traitnf <- function(n) segments(moyennes[n],n,mean(x),n,col="blue",lwd=2)
  sapply(1:length(levels(gpe)),traitnf)
}


graphnf(iris[,1],iris$Species)