--@createContact
WITH new_group AS (
    INSERT INTO groups (name) 
    VALUES (%(groupName)s) 
    ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name
    RETURNING id
),
new_contact AS (
    INSERT INTO contacts (name, email, birthday, group_id)
    SELECT %(contactName)s, %(email)s, %(birthday)s, id 
    FROM new_group
    RETURNING id
)
INSERT INTO phones (contact_id, phone, type)
SELECT id, %(phone)s, %(phoneType)s 
FROM new_contact;

--@exportJson
SELECT 
	c.name, 
	c.email, 
	c.birthday::TEXT,
	g.name AS group_name,
	(
		SELECT json_agg(json_build_object('phone', p.phone, 'type', p.type))
		FROM phones p
		WHERE p.contact_id = c.id
	) AS phones
FROM contacts c
LEFT JOIN groups g ON c.group_id = g.id;

--@updateContact
UPDATE contacts SET name = %s WHERE id = %s;

--@deleteContactByName
DELETE FROM contacts WHERE id = %s;

--@deleteContactByPhone
DELETE FROM contacts USING phones WHERE phones.contact_id = contacts.id AND phones.id = %s;

--@searchByPhone
SELECT c.name, p.phone, p.type
FROM contacts c
INNER JOIN phones p ON c.id = p.contact_id
WHERE p.phone LIKE %s;

--@searchByName
SELECT c.name, p.phone, p.type
FROM contacts c
INNER JOIN phones p ON c.id = p.contact_id
WHERE c.name ILIKE %s;
