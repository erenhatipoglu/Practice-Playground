array <- sample(500,500, replace = F)

array

# See how much time it takes
start <- Sys.time()

for (i in 1:(length(array) - 1)) {
  for (a in 1:(length(array) - i)) {
    if (array[a] > array[a + 1]) {
      temp <- array[a]
      array[a] <- array[a + 1]
      array[a + 1] <- temp
    }
  }
}

end <- Sys.time()

howmuch <- end-start

cat(paste("It took", howmuch, "seconds to bubble sort this array.\n"))
print(array)
