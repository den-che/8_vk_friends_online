import vk
import getpass


APP_ID = '6339777'  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input("Введите логин пользователя: ")
    return login


def get_user_password():
    password = getpass.getpass(prompt="Пароль: ")
    return password


def get_online_friends(login, password):
        friends_dict = {}

        auth_session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope={'friends', 'users'}
        )

        api = vk.API(auth_session)
        friends_list = api.friends.getOnline()
        friends_dict = api.users.get(user_ids=friends_list, fields = "first_name, last_name")
        return friends_dict
        

def output_friends_to_console(friends_online):
    print("Все друзья которые онлайн")
    print("__________________________\n")
    for friend in friends_online:
        print ('{} {}\n'.format(friend['first_name'],friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
