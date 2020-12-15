import wine_clustering
import Clustering_wine_dataset
import sys

def service_func():
    print('\n*** WELCOME TO FA20 255-01 TEAM 1 WINE LAB ! ***\n')
    # Define service menu
    menu_dict = {'1':'Wine Recommendation',
                 '2':'Wine Region Analysis',
                 '3':'Wine Clustering',
                 '4':'No thanks.'}
    for menu in menu_dict:
        print(menu + ': ' + menu_dict[menu])
        
    user_service = input('\nPlease enter the service you need (1 ~ ' + str(len(menu_dict)) + '): ')

    # Handle invalid input
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
            '3': Clustering_wine_dataset.clustering,
            '4': exit()
            }
    return switcher.get(i,"The specified key does not exist!")()

def exit():
    print('Thanks for using our services. Happy Holiday!')
    sys.exit()

if __name__ == '__main__':
    # service.py executed as script
    # do something
    service(service_func())