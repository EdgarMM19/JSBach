Main |:
	<?> a
	<!> "Tarda" Collatz a "en arribar a 1."
:|

Collatz a |:
	if a = 1 |:
		rück 0
	:|
	if a % 2 = 0 |:
		rück (Collatz a/2) +1
	:|
	else |:
		rück (Collatz 3*a+1) +1
	:|
:|
