SELECT t.teacher_name, c.course_name, ROUND(AVG(g.grade_value), 2) as average_grade
FROM grades AS g
LEFT JOIN courses AS c ON g.course_id = c.id
LEFT JOIN teachers AS t ON c.teacher_id = t.id
WHERE t.id = 1
GROUP BY t.teacher_name, c.course_name
ORDER BY t.teacher_name, c.course_name;