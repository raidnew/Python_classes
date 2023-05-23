https://editor.ponyorm.com/user/raidnew/homework_type21/designer

SELECT *
FROM `Child`
WHERE id_group = 1

SELECT t.name
FROM Teacher as t
LEFT JOIN `group` as g ON g.id_class_teacher = t.id
WHERE g.id = 1

SELECT *
FROM `Schedule` as sch
LEFT JOIN `Subject` as sub ON sch.id_subject = sub.id
LEFT JOIN `Teacher` as t ON t.id = sub.id_teacher
WHERE t.name = "Techaer1"

SELECT *
FROM `Mark` as m
LEFT JOIN `Child` as c ON c.id = m.id_child
WHERE c.name = "People1"


SELECT *
FROM `Child` as c
LEFT JOIN `Mark` as m ON m.id_child = c.id
GROUP BY c.id
HAVING SUM(m.mark_value <= 3) <= 0

