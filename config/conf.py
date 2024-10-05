import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
ALLURE_IMG_DIR = os.path.join(BASE_DIR, 'image_allure')

'''
if __name__ == '__main__':
    print(BASE_DIR)
    print(LOG_DIR)
    print(ALLURE_IMG_DIR)
'''