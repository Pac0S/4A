rm(list=ls())

gd <- read.table('goldtable.txt', header = T, sep = '\t', dec = '.', quote = "", comment.char = "")


procaryot <- subset(gd, subset = is.element(SUPERKINGDOM, c('Bacteria', 'Archae')))
complete <- subset(gd, subset = is.element(PROJECT.STATUS, c('complete', 'Complete and Published')))
RNA <- subset(gd, select = c(PLASMID.COUNT, CHROMOSOME.COUNT))

cptpro <- gd[(gd$PROJECT.STATUS=='complete' | gd$PROJECT.STATUS=='Complete and Published')  & (gd$SUPERKINGDOM=='Bacteria'| gd$SUPERKINGDOM=='Archaea'),]
cptprorna <- subset(cptpro, select = c(SUPERKINGDOM,PLASMID.COUNT, CHROMOSOME.COUNT))

par(mfrow = c(1,1))

plot(cptprorna$SUPERKINGDOM, cptprorna$PLASMID.COUNT)
plot(cptprorna$SUPERKINGDOM, cptprorna$CHROMOSOME.COUNT)

count_pls <- table(cptprorna$PLASMID.COUNT)
barplot(count_pls)

count_chr <- table(cptprorna$CHROMOSOME.COUNT)
count <- table(cptprorna$CHROMOSOME.COUNT,cptprorna$PLASMID.COUNT)
barplot(count_chr)

dim(cptprorna)
plot(count, col = rainbow(11))
barplot(t(count), col = rainbow(dim(count[2])))
dim(count[2])
