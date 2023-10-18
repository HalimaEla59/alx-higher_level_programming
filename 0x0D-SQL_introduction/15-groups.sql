-- lists number of records with same score (descending)
SELECT 'score', COUNT(*) AS 'number' FROM 'second_table'
GROUP BY 'score' DESC ORDER BY 'number' DESC;
