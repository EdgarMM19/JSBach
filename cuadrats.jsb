Main |:
    <!> "n:"
    <?> n
    v <- {}
    i <- 1
    while i <= n |:
        v << i
        i <- i+1
    :|
    i <- 1
    while i <= n |:
        <!> v[i] * v[i]
        i <- i+1
    :|
    while #v /= 0 |:
        <!> v[#v]
        8< v[#v]
    :|
    <!> 3 / 0
:|