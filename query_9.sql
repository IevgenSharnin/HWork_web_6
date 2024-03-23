SELECT s.student_name, c.course_name 
FROM students AS s
LEFT JOIN grades AS g ON g.student_id = s.id
LEFT JOIN courses AS c ON g.course_id = c.id
WHERE s.id = 1
GROUP BY g.student_id, g.course_id
ORDER BY s.student_name;