quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
	let smallerSorted = quicksort [y | y <- xs, y <= x];
		biggerSorted = quicksort [y | y <- xs, y > x]
	in smallerSorted ++ [x] ++ biggerSorted