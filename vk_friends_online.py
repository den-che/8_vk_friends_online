import vk
import getpass


APP_ID = '6339777'  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input("Введите логин пользователя: ")
    return login


def get_user_password():
    #password = input("Введите пароль: ")
    password = getpass.getpass()
    return password


def get_online_friends(login, password):
        auth_session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope={'friends', 'users'},
        
        )

        api = vk.API(auth_session)
        friends_list = api.friends.getOnline()
        print(friends_list)
        for id in friends_list:
            print(id)
            friend = api.users.get(user_ids=id, fields = "screen_name")
            print(friend)

def output_friends_to_console(friends_online):
    pass

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
