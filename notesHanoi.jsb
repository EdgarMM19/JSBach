~~~ Notes de Hanoi ~~~

Main |:
    src <- {A0}
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src + n
        <:> note
        HanoiRec (n - 1) aux dst src
    :|
:|