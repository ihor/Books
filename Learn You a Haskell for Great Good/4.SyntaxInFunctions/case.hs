describeList :: [a] -> String
describeList xs = "The list is " ++ case xs of
	[] -> "empty."
	[x] -> "a singleton list."
	xs -> "a longer list."