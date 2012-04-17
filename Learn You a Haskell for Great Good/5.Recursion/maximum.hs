maximum' :: (Ord a) => [a] -> a
maximum' [] = error "Can't get maximum of empty list"
maximum' [x] = x
maximum' (x:xs)
	| x > maxTail = x
	| otherwise = maxTail
	where maxTail = maximum' xs