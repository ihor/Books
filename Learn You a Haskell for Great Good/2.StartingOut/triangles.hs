triangles = [(a, b, c) | a <- [1..10], b <- [a..10], c <- [b..10], a + b > c, b + c > a, c + a > b]