-- lists number of records with same score (descending)
SELECT 'score', COUNT(*) AS 'number'
FROM 'second_table'
GROUP BY 'score'
ORDER BY 'number' DESC;
