~~~ Notes de Hanoi ~~~

Main |:
    src <- {C D E F G}
    <!> src
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        <:> note
        HanoiRec (n - 1) aux dst src
    :|
:|