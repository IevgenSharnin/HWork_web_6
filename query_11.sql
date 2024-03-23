SELECT with_teacher.teacher_name, with_teacher.student_name, ROUND(AVG(with_teacher.grade_value), 2) as average_grade
FROM 
	(SELECT s.student_name, g.grade_value, t.teacher_name 
	FROM grades AS g
	LEFT JOIN students AS s ON g.student_id = s.id
	LEFT JOIN courses AS c ON g.course_id = c.id
	LEFT JOIN teachers AS t ON c.teacher_id = t.id
	WHERE s.id = 1 AND t.id = 1)
	AS with_teacher
GROUP BY with_teacher.teacher_name, with_teacher.student_name
ORDER BY with_teacher.teacher_name, with_teacher.student_name;