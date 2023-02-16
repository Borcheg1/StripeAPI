# Приложение, демонтсрирующее Stripe API на основе Django проекта
### **Руководство по установке и запуску приложения**

1. Откройте терминал

2. Введите команду:
`git clone https://github.com/Borcheg1/StripeAPI.git`

3. Перейдите в рабочую дерикторию проекта:
`cd StripeAPI`

4. Создайте виртуальное окружение:
`python -m venv venv`

5. Активируйте виртуальное окружение:

    для Windows:
`venv\Scripts\activate`

    для Linux и MacOS:
`source venv/bin/activate`

6. Установите зависимости:
`python -m pip install -r requirements.txt`

7. Запустите сервер:
`python manage.py runserver`

8. Откройте браузер и перейдите по ссылке:
`http://localhost:8000/admin/`

9. Авторизуйтесь:

    >Login: Dmitriy
    
    >Password: admin

10. При необходимости добавьте товары:

    ***Будьте внимательны!***
    ***Stripe запрещает покупку товаров с ценой менее $0.50, что эквивалентно ~ 37 рублям!***
    
    >![add step 1](https://i.ibb.co/SBBMRWt/Capture.jpg)

    >![add step 2](https://i.ibb.co/CMZtmNK/Capture1.jpg)

    >![add step 3](https://i.ibb.co/2vX3dhR/Capture2.jpg)

11. При необходимости удалите товары:

    >![delete step 1](https://i.ibb.co/GQXgzsZ/Capture3.jpg)
    
    >![delete step 1](https://i.ibb.co/WFRKdbY/Capture4.jpg)

12. Перейдите в браузере по ссылке:
`http://localhost:8000/`

13. Нажмите кнопку "Начать покупки"

14. Нажмите на название нужного товара:
    >![make order](https://i.ibb.co/PY061qz/Capture5.jpg)
    
15. Нажмите кнопку "Buy"

16. Введите реквизиты

    Тестовые реквизиты:
    
        > Email: test@examlpe.com
        
        > Card number: 4242424242424242
        
        > Date: 08/30
        
        > CVC: 123
        
        > Name: Test name

### Спасибо, что воспользовались моим приложением!
