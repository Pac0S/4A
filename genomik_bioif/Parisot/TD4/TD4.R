rm(list=ls())

#Retourne la valeur du logarithme de la fonction du maximum de vraisemblance
logvraineg <- function(param, obs) {
  p <- param[1]
  m1 <- param[2]
  sd1 <- param[3]
  m2 <- param[4]
  sd2 <- param[5]
  -sum(log(p * dnorm(obs, m1, sd1) + (1 - p) * dnorm(obs, m2, sd2)))
}

#Simule un mélange de deux lois normales
simulmixnor <- function(n, p, m1, sd1, m2, sd2) {
  n1 <- rbinom(1, n, p)
  x1 <- rnorm(n1, m1, sd1)
  x2 <- rnorm(n - n1, m2, sd2)
  c(x1, x2)
}


data <- read.table("bactgensize.txt", h=T, sep = '\t', quote = "\"")
names(data)


x <- data$sizeKb/1000
hist(x, col = grey(0.8), proba = TRUE, main = paste("Distribution de la tailles de\n",
                                                    length(x), "genomes bacteriens"), 
     xlab = "Taille du genome en Mb",
     ylab = "Densite")
xseq <- seq(from = min(x), to = max(x), length = 50)
lines(xseq, dnorm(xseq, mean(x), sd(x)), lwd = 2)

qqnorm(x)
qqline(x)


resnlm <- nlm(f = logvraineg, p = c(0.5, 2, 1, 4.5, 1), obs = x)
resnlm$estimate

xseq <- seq(min(x), max(x), le = 100)
est <- resnlm$estimate
y1 <- est[1] * dnorm(xseq, est[2], est[3])
y2 <- (1 - est[1]) * dnorm(xseq, est[4], est[5])
hist(x, proba = TRUE, ylim = c(0, max(y1 + y2)), col = grey(0.8),
     main = paste("Distribution de la tailles de\n", length(x), "genomes bacteriens"),
     xlab = "Taille du genome en Mb", ylab = "Densite")
lines(xseq, y1 + y2)
lines(xseq, y1, col = "red", lwd = 2)
lines(xseq, y2, col = "blue", lwd = 2)

theo <- simulmixnor(10000, est[1], est[2], est[3], est[4], est[5])
qqplot(theo, x, main = "Graphe quantiles-quantiles contre\nmelange de deux lois normales",
       xlab = "Quantiles theoriques", ylab = "Quantiles observes")
lines(c(0, 10), c(0, 10))

data[order(x), c(1, 2, 4)][1:15, ]
