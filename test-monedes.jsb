Main |:
	<!> "Nombre de tipus de monedes"
	<?> n
	coins <- {}
	i <- 0
	<!> "Entra les" n "monedes"
	while i < n |:
		<?> a
		coins << a
		i <- i+1
	:|
	<!> "Quantitat a pagar"
	<?> p
	i <- 0
	memo <- {}
	while i <= p |:
		memo << 0
		i <- i+1
	:|
	memo[1] <- 1
	i <- 0
	while i < n |:
		j <- 0
		m <- coins[i+1]
		while j + m <= p |:
			memo[j+1+m] <- Max memo[j+1] memo[j+1+m]
			j <- j+1
		:|
		i <- i+1
	:|
	if memo[p+1] |:
		<!> "Pots pagar!"
	:| 
	else |:
		<!> "No pots pagar :("
	:|
:|

Max a b |:
	if a > b |:
		rück a
	:|
	rück b
:|