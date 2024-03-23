SELECT gr.group_name, s.student_name 
FROM groups AS gr
LEFT JOIN students AS s ON s.group_id = gr.id
WHERE gr.id = 1
ORDER BY gr.group_name;