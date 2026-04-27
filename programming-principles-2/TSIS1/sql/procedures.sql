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

--@searchByPattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p text)
RETURNS TABLE(contact_name VARCHAR, contact_email VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT DISTINCT c.name, c.email, ph.phone
    FROM contacts c
    LEFT JOIN phones ph ON c.id = ph.contact_id
    WHERE c.name  ILIKE '%%' || p || '%%'
       OR c.email  ILIKE '%%' || p || '%%'
       OR ph.phone ILIKE '%%' || p || '%%';
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_contacts_by_pattern(%s);

--@upsertContact
CREATE OR REPLACE PROCEDURE upsert_contact_with_phone(
    p_group_name TEXT,
    p_contact_name TEXT,
    p_email TEXT,
    p_birthday DATE,
    p_phone TEXT,
    p_phone_type TEXT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_group_id INTEGER;
    v_contact_id INTEGER;
BEGIN
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name) RETURNING id INTO v_group_id;
    END IF;

    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;

    IF v_contact_id IS NOT NULL THEN
        UPDATE contacts 
        SET email = p_email, 
            birthday = p_birthday, 
            group_id = v_group_id 
        WHERE id = v_contact_id;
        
        DELETE FROM phones WHERE contact_id = v_contact_id;
    ELSE
        INSERT INTO contacts (name, email, birthday, group_id)
        VALUES (p_contact_name, p_email, p_birthday, v_group_id)
        RETURNING id INTO v_contact_id;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_phone_type);
END;
$$;

CALL upsert_contact_with_phone(%(groupName)s, %(contactName)s, %(email)s, %(birthday)s, %(phone)s, %(phoneType)s);