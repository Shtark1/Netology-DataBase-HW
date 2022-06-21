SELECT1 = '''
SELECT g.name, COUNT(*) FROM performes_genre o 
JOIN genre g ON o.genre_id = g.id GROUP BY o.genre_id, g.name ORDER BY count(*) DESC;
'''

SELECT2 = '''
SELECT COUNT(*) FROM tracks t 
JOIN album a ON t.album_id = a.id WHERE a.release = 2019 or a.release = 2020;
'''

SELECT3 = '''
SELECT a.name, AVG(duration) FROM tracks t 
JOIN album a ON t.album_id = a.id WHERE a.id = t.album_id GROUP BY a.name ORDER BY AVG(duration) DESC;
'''

SELECT4 = '''
SELECT p.name from performes p 
JOIN performes_album pa ON p.id = pa.performes_id JOIN album a ON a.id = pa.album_id WHERE a.release != 2020;
'''

SELECT5 = '''
SELECT c.name, p.name FROM collection c 
JOIN tracks_collection tc ON c.id = tc.collection_id 
JOIN tracks t ON tc.tracks_id = t.id 
JOIN album a ON t.album_id = a.id 
JOIN performes_album pa ON a.id = pa.album_id 
JOIN performes p ON p.id = pa.performes_id 
GROUP BY c.name, p.name, p.id 
HAVING p.id = 2 
'''

SELECT6 = '''
SELECT too.albumName, too.name, too.po FROM 
(SELECT a.name AS albumName, p.name, COUNT(pg.genre_id) AS po FROM performes p 
JOIN performes_genre pg ON p.id = pg.performes_id 
JOIN performes_album pa ON pa.performes_id = p.id 
JOIN album a ON a.id = pa.album_id 
GROUP BY albumName, p.name ORDER BY COUNT(pg.genre_id)) AS too
GROUP BY too.albumName, too.name, too.po 
HAVING too.po > 1; 
'''

SELECT7 = '''
SELECT t.name FROM tracks t 
JOIN (SELECT t.id FROM tracks t EXCEPT SELECT tc.tracks_id FROM tracks_collection tc) AS isp ON isp.id = t.id;
'''

SELECT8 = '''
SELECT t.name FROM tracks t 
WHERE duration = (SELECT  MIN(t.duration) FROM performes p 
JOIN performes_album pa ON p.id = pa.performes_id  
JOIN album a ON pa.album_id = a.id 
JOIN tracks t ON a.id = t.album_id)
'''

SELECT9 = '''
SELECT al.amount, al.name FROM 
(SELECT COUNT(t.album_id) AS amount, a.name FROM album a 
JOIN tracks t ON t.album_id = a.id GROUP BY a.name, a.id) AS al 
WHERE amount = (SELECT MIN(pro.pros) 
FROM (SELECT COUNT(t.album_id) AS pros FROM album a 
JOIN tracks t ON t.album_id = a.id GROUP BY a.name, a.id) AS pro)
'''