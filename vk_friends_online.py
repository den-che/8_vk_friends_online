import vk


APP_ID = '6339777'  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input("Введите логин пользователя: ")
    return login


def get_user_password():
    password = input("Введите пароль: ")
    return password


def get_online_friends(login, password):
    auth_session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    access_token = auth_session.get_access_token()
    print(access_token)
    session = vk.Session(access_token=access_token)

    api = vk.API(session)
    #api.friends.getOnline()
    
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    pass

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
