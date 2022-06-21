INSERT = """
    INSERT INTO album (name, release) VALUES 
    ('i am i was', '2018'), ('Заправка Кид 2', '2021'), ('NO BANG! HOLD ON!', '2022'), ('Find the Beat', '2020'),
    ('Неразбериха', '2013'), ('Ломбард', '2015'), ('Birds In The Trap Sing McKnight', '2018'), ('Donda', '2021');
    
    INSERT INTO collection (name, release) VALUES 
    ('Для сна', '2020'), ('Тусовка', '2020'), ('Грустные', '2015'), ('Для Учёбы', '2021'),
    ('Для Тренировок', '2000'), ('Меломан', '2013'), ('Рок', '2018'), ('Трэпчик', '2022');
    
    INSERT INTO genre (name) VALUES
    ('Рэп'), ('Трэп'), ('Рок'), ('Шансон'), ('Сальса');
    
    INSERT INTO performes (name) VALUES
    ('21 savage'), ('Mayot'), ('Bushido Zho'), ('BlueFace'), ('Noize MC'), 
    ('Кровосток'), ('Travis Scott'), ('KanyeWest');
    
    INSERT INTO performes_album (performes_id, album_id) VALUES
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), 
    ('7', '7'), ('8', '8');
    
    INSERT INTO performes_genre (performes_id, genre_id) VALUES
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '1'), 
    ('7', '3'), ('8', '2');
    
    INSERT INTO tracks (name, duration, album_id) VALUES
    ('My a lot', '220', '1'), ('asmr', '180', '1'), ('Абонент', '80', '2'), ('Калека', '129', '2'),
    ('Batman', '108', '3'), ('Komar', '110', '3'), ('My Vibes', '187', '4'), ('Dirty', '120', '4'),
    ('Ненавижу', '220', '5'), ('Нам не понять', '130', '5'), ('Ногти', '249', '6'), ('Летом', '190', '6'),
    ('outside', '178', '7'), ('lose', '201', '7'), ('Donda', '101', '8'), ('Moon', '129', '8'),
    ('ЭТо трека который не входит в сборник', '178', '2');
    

    INSERT INTO tracks_collection (tracks_id, collection_id) VALUES
    ('1', '1'), ('2', '1'), ('3', '2'), ('4', '2'),
    ('5', '3'), ('6', '3'), ('7', '4'), ('8', '4'),
    ('9', '5'), ('10', '5'), ('11', '6'), ('12', '6'),
    ('13', '7'), ('14', '7'), ('15', '8'), ('16', '8');

"""