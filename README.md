# Sprint_5 - "UI-тестирование"

## Структура проекта

1. **tests**:

    Папка содержащая ui-тесты на следующую функциональность:
   - **test_registration.py** - файл, где содержатся тесты на функциональность "Регистрация пользователя"
      - `test_successful_registration` - регистрация пользователя
      - `test_invalid_email_registration` - регистрация пользователя с email не по маске
      - `test_registration_with_existing_user` - регистрация уже существующего пользователя    
   - **test_login.py** - файл, где содержится тест на функциональность "Login пользователя"
      - `test_successful_login` - авторизация пользователя                  
   - **test_logout.py** - файл, где содержится тест на функциональность "Logout пользователя"
      - `test_successful_registration` - разлогин пользователя
   - **test_create_ad.py** - файл, где содержатся тесты на функциональность "Создание объявления"
      - `test_create_ad_authorized_user` - создание объявления авторизованным пользователем
      - `test_create_ad_unauthorized_user` - создание объявления неавторизованным пользователем

3. **data.py**:  
Содержит методы для генерации почты и пароля

4. **locators.py**:  
Содержит локаторы для элементов

5. **conftest.py**:  
Содержит фикстуру `driver` для инициализации драйвера
