SELECT 'CREATE DATABASE online_exam' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'online_exam')\gexec

SELECT 'CREATE DATABASE online_exam_test' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'online_exam_test')\gexec
