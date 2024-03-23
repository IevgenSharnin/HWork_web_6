SELECT ROUND(AVG(g.grade_value), 2) as average_grade, s.student_name
FROM grades AS g
LEFT JOIN students AS s ON g.student_id = s.id
GROUP BY g.student_id
ORDER BY ROUND(AVG(g.grade_value), 2) DESC
LIMIT 5;
