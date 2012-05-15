replicate' :: (Num i, Ord i) => a -> i -> [a]
replicate' x n
	| n <= 0 = []
	| otherwise = x:replicate' x (n - 1)

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
	| n <= 0 = []
take' _ [] = []
take' n (x:xs) = x:take' (n-1) xs

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]

repeat' :: a -> [a]
repeat' a = a:repeat' a

zip' :: [a] -> [b] -> [(a, b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x, y):zip' xs ys

elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' x (y:ys)
	| x == y = True
	| otherwise = elem' x ys