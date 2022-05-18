Main |:
	l <- { 1 2+3 5}
	<!> l
	a <- 2
	Canvi l a
	<!> l a
:|

Canvi l a|:
	8< l[1]
	a <- a+1
:|
