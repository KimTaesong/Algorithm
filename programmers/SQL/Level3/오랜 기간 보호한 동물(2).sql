SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
LEFT OUTER JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME IS NOT NULL
ORDER BY A.DATETIME - B.DATETIME DESC
LIMIT 2