SELECT t.teacher_name, c.course_name 
FROM teachers AS t
LEFT JOIN courses AS c ON c.teacher_id = t.id
WHERE t.id = 1
ORDER BY t.teacher_name;