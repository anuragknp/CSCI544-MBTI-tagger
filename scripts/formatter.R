Result <- list()
path <- file.path("data")
print(path)
print(list.files(path))
for (i in list.files(path)) {
  Result <- append(Result, file.path(path, i))
}
print(Result)
txt <- lapply(Result, readLines)
nms <- gsub("cleanedAraTokens.txt", "", Result)
tweets <- setNames(txt, nms)
tweets <- sapply(tweets, function(x) paste(x, collapse = " "))
write.csv(tweets, file = "tweets.csv")

