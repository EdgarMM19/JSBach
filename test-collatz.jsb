Main |:
	<?> a
	l <- {}
	<!> "Tarda" (Collatz a l) "en arribar a 1."
	<!> l
:|

Collatz a l|:
	l << a
	if a = 1 |:
		rück 0
	:|
	if a % 2 = 0 |:
		rück (Collatz a/2 l) +1
	:|
	else |:
		rück (Collatz 3*a+1 l) +1
	:|
:|
