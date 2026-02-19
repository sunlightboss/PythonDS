-- Active: 1769433636626@@127.0.0.1@5432@sultan
CREATE DATABASE sultan;
CREATE TABLE students (
    first_name   VARCHAR(50) NOT NULL,
    last_name    VARCHAR(50) NOT NULL,
    birth_date   DATE        NOT NULL,
    has_budget   BOOLEAN     DEFAULT FALSE,
    phone        BIGINT      UNIQUE,
    course       VARCHAR(100),
    is_active    BOOLEAN     DEFAULT NULL
);

INSERT INTO students (first_name, last_name, birth_date, has_budget, phone, course) VALUES
('Айбек',    'Сатыбалдиев', '2008-05-12', TRUE,  996555123456, 'Backend'),
('Гулнура',  'Маматова',    '2005-11-03', FALSE, 996777987654, 'Frontend'),
('Эрлан',    'Жумабеков',   '2007-02-28', TRUE,  996701456789, 'Data Science'),
('Сабина',   'Кыдыралиева', '2009-09-15', FALSE, 996559112233, 'Mobile Dev'),
('Нурсултан','Алиев',       '2004-07-20', TRUE,  996706334455, 'DevOps'),
('Айжан',    'Токтогулова', '2006-12-01', FALSE, 996550998877, 'QA');

UPDATE students
SET is_active = FALSE
WHERE birth_date > CURRENT_DATE - INTERVAL '18 years';

