-- lists number of records with same score (descending)
SELECT 'score', COUNT('score') AS 'number' FROM 'second_table'
GROUP BY 'score' DESC;
