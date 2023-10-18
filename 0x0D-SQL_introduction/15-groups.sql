-- lists the number of records with same score in second_table (descending)
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score DESC;
