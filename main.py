title_film = 'Крестный отец: Трилогия 1901-1980'
eng_title = 'The Godfather Trilogy: 1901-1980'
img_film = 'https://static.hdrezka.ac/i/2021/10/9/ff30995b7978bwx72s54v.jpg'
description_film = "Фильм представляет собой сагу о взлёте и падении преступного клана Корлеоне, охватывающем три поколения семейства Вито, эмигрировавшего из Италии в Соединённые Штаты Америки после убийства отца, его старшего брата и матери. Благодаря твёрдому характеру вчерашний иммигрант достаточно быстро возглавил крупную группировку итальянских преступников в Нью-Йорке. История рассказывается в хронологическом порядке, объединяя три ранее выпущенные картины, с добавлением в общей сложности шестидесяти минут вырезанных из предыдущих фильмов сцен."

user = {
    "name": "Azim",
    "password": 1234
}


login_name = input('Имя пользователя: ')
login_password = int(input('Пароль: '))


if login_name == user['name'] and login_password == user['password']: 
    print('Вы вошли в систему') 
else:
    print('Ошибка')    