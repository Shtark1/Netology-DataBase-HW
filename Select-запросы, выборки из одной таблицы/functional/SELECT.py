SELECT1 = "SELECT name, release FROM album WHERE release = '2018';"

SELECT2 = """
    SELECT name, duration FROM tracks WHERE 
    duration = (SELECT MAX(duration) FROM tracks);
        """

SELECT3 = "SELECT name, duration FROM tracks WHERE duration > 210;"

SELECT4 = 'SELECT name FROM collection WHERE "release"  <= 2020 AND "release" >= 2018;'

SELECT5 = "SELECT name FROM performes WHERE 1 = (LENGTH(name) - LENGTH(REPLACE(name, ' ', ''))+1)"

SELECT6 = '''SELECT * FROM tracks WHERE "name" LIKE '%My%';'''