SELECT aver.course_name, MAX(aver.averages) as max_grade, aver.student_name
FROM 
	(SELECT c.course_name, ROUND(AVG(g.grade_value), 2) as averages, s.student_name
	FROM grades AS g
	LEFT JOIN students AS s ON g.student_id = s.id
	LEFT JOIN courses AS c ON g.course_id = c.id
	WHERE g.course_id = 1
	GROUP BY g.course_id, g.student_id
	ORDER BY ROUND(AVG(g.grade_value), 2) DESC)
	AS aver
GROUP BY aver.course_name
ORDER BY aver.averages DESC;