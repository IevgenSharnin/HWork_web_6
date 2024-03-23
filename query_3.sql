SELECT gr.group_name, c.course_name, ROUND(AVG(g.grade_value), 2) as average_grade
FROM grades AS g
LEFT JOIN students AS s ON g.student_id = s.id
LEFT JOIN groups AS gr ON s.group_id = gr.id
LEFT JOIN courses AS c ON g.course_id = c.id
WHERE g.course_id = 1
GROUP BY s.group_id, g.course_id
ORDER BY gr.group_name;