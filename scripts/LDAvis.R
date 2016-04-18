library(readr)
library(tm)
library(SnowballC)
library(Matrix)
library(lda)
library(LDAvis)
library(servr)

# read data
train = read.csv("tweets_16way_final.csv", header=TRUE);
txt = train[,c(2)]
labels = train[,1]
 
# tokenize on space and output as a list:
txt <- as.character(txt)
doc.list <- strsplit(txt, " ")

# compute the table of terms:
term.table <- table(unlist(doc.list))
term.table <- sort(term.table, decreasing = TRUE)

vocab <- names(term.table)

# now put the documents into the format required by the lda package:
get.terms <- function(x) {
    index <- match(x, vocab)
    index <- index[!is.na(index)]
    rbind(as.integer(index - 1), as.integer(rep(1, length(index))))
}

documents <- lapply(doc.list, get.terms)


# Compute some statistics related to the data set:
D <- length(documents)
W <- length(vocab)  
doc.length <- sapply(documents, function(x) sum(x[2, ])) 
N <- sum(doc.length)  
term.frequency <- as.integer(term.table)

# MCMC and model tuning parameters:
K <- 16
G <- 50
alpha <- 0.02
eta <- 0.02

# Fit the model:
set.seed(357)
t1 <- Sys.time()

#fit <- lda.collapsed.gibbs.sampler(documents = documents, K = K, vocab = vocab, 
#                                   num.iterations = G, alpha = alpha, 
#                                   eta = eta, initial = NULL, burnin = 0,
#                                   compute.log.likelihood = TRUE)

params <- sample(c(-1, 1), K, replace=TRUE)

fit <- slda.em(documents=documents,
                  K=K,
                  vocab=vocab,
                  num.e.iterations=G,
                  num.m.iterations=G,
                  alpha=alpha, eta=eta,
                  labels,
                  params,
                  variance=0.25,
                  lambda=1.0,
                  logistic=FALSE,
                  method="sLDA")

t2 <- Sys.time()
t2 - t1  

### Visualizing the fitted model with LDAvis
theta <- t(apply(fit$document_sums + alpha, 2, function(x) x/sum(x)))
phi <- t(apply(t(fit$topics) + eta, 2, function(x) x/sum(x)))

results <- list(phi = phi,
                theta = theta,
                doc.length = doc.length,
                vocab = vocab,
                term.frequency = term.frequency)

top.topic.words(fit$topics, 30, by.score=TRUE)

test = read.csv("tweets_16way_test_final.csv", header=TRUE);
test_txt = test[,c(2)]

# tokenize on space and output as a list:
test_txt <- as.character(test_txt)
test_doc.list <- strsplit(test_txt, " ")

# compute the table of terms:
test_term.table <- table(unlist(test_doc.list))
test_term.table <- sort(test_term.table, decreasing = TRUE)

test_vocab <- names(test_term.table)

# now put the documents into the format required by the lda package:
test_get.terms <- function(x) {
  index <- match(x, test_vocab)
  index <- index[!is.na(index)]
  rbind(as.integer(index - 1), as.integer(rep(1, length(index))))
}

test_documents <- lapply(doc.list, get.terms)

predictions <- slda.predict(test_documents,
                            fit$topics, 
                            fit$model,
                            alpha = alpha,
                            eta=eta)

# create the JSON object to feed the visualization:
json <- createJSON(phi = results$phi, 
                   theta = results$theta, 
                   doc.length = results$doc.length, 
                   vocab = results$vocab, 
                   term.frequency = results$term.frequency)

serVis(json, out.dir = './', open.browser = FALSE)
system("mv index.html results.html")
