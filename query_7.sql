SELECT c.course_name, gr.group_name, s.student_name, g.grade_value
FROM grades AS g
LEFT JOIN students AS s ON g.student_id = s.id
LEFT JOIN groups AS gr ON s.group_id = gr.id
LEFT JOIN courses AS c ON g.course_id = c.id
WHERE gr.id = 1 AND g.course_id = 1
ORDER BY c.course_name;