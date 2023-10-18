-- lists records of second_table Don’t list rows without a name val
SELECT score, name FROM second_table WHERE name <> ''
GROUP BY score DESC, name DESC;
