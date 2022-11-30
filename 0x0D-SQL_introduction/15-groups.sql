-- lists the `score` & number of occurances with each score with 'number'
-- displaying this data sorted by number in descending order
--
-- score   number
-- 10  2
-- 8   1

SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;

