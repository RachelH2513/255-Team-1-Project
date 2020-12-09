import wine_clustering

def service_func():
    print('*** WELCOME TO FA20 255-01 TEAM 1 WINE LAB ! ***')
    # Define service menu
    menu_dict = {'1':'Wine Recommendation',
                 '2':'Wine Region Analysis',
                 '3':'Wine Clustering'}
    for menu in menu_dict:
        print(menu + ': ' + menu_dict[menu])
    user_service = input('Please enter the service you need (1 ~ ' + str(len(menu_dict)) + '): ')

    # Deal with invalid input
    input_invalid = True
    while input_invalid:

        if user_service not in menu_dict:
                print("Invalid input!")
                user_service = input('Please enter the service you need (1 ~ ' + str(len(menu_dict)) + '): ')
        else:
            input_invalid = False
    
    return user_service


def service(i):
    switcher={
            '1': wine_clustering.wine_recommender,
            '2': 'Under Construction...',
            '3': 'Under Construction...'
            }
    return switcher.get(i,"Unknown Error!")


if __name__ == '__main__':
    # service.py executed as script
    # do something
    service(service_func())