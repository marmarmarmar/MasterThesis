library("png")
susel = readPNG("1.png")
wiewiorka = readPNG("2.png")
# Generation of input data

wiewiorka[wiewiorka == 1] = 0

susel = susel[ , , 1] + susel[ , , 2] + susel[ , , 3] + susel[ , , 4]
wiewiorka = wiewiorka[ , , 1] + wiewiorka[ , , 2]

wiewiorka = wiewiorka / 2
susel = susel / 4

inputMatrix = matrix(0, ncol = 400, nrow = 1)

image(susel)
image(wiewiorka)

crosses = 0
circles = 0

for(i in c(1 : 100)) {
    if(rnorm(1) > 0) {
        crosses = crosses + 1
        inputMatrix = rbind(inputMatrix, as.vector(susel))
    } else {
        inputMatrix = rbind(inputMatrix, as.vector(wiewiorka))
        circles = circles + 1
    }
}

library(autoencoder)

myAutoencoder = autoencode(inputMatrix, N.hidden = 2, epsilon = 0.01, lambda = 0.01, beta = 2, rho = 0.001)

visualize.hidden.units(myAutoencoder,20, 20)