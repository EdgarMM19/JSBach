~~~ programa que llegeix dos enters i n'escriu el seu maxim comu divisor ~~~

Main |:
    <!> "Escriu dos nombres"
    <?> a
    <?> b

    <!> "El seu MCD es" (Euclides a b)

    c <- (Euclides a b)*3
    <!> "Tres cops el seu MCD es" c
    <!> "El maxim es" (Max a b)

    <!> "La multiplicacio dels seus factorials es" (Factorial a) * (Factorial b)
:|

Euclides a b |:
    if a < 0 |:
        a <- -a
    :|
    if b < 0 |:
        b <- -b
    :|
    while a /= b |:
        if a > b |:
            a <- a - b
        :| else |:
            b <- b - a
        :|
    :|
    rück (a+b)
:|

Max a b |:
    if a > b |:
        rück a
    :|
    rück b
:|

Factorial n |:
  if n = 0 |:
    rück 1
  :|

  rück (n * (Factorial (n-1) ))
:|