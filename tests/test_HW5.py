from selene import browser, have, be
import os


def test_number():
    browser.open('/automation-practice-form')
    browser.driver.execute_script(
        "document.querySelector('.body-height').style.transform='scale(.40)'")

    # Заполнение полей FirstName и LastName
    browser.element('#firstName').should(be.blank).type('Boris')
    browser.element('#lastName').should(be.blank).type('Shark')

    # Заполнение поля Email
    browser.element('#userEmail').type('examplemail@mail.com')

    # Выбор радио-кнопки для поля Gender
    browser.element('[for="gender-radio-1"]').click()

    # Заполнение поля Mobile
    browser.element('#userNumber').should(be.blank).type('2911011214')
    browser.element('#userNumber').should(have.value('2911011214'))

    # Заполнение поля Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__header__dropdown.react-datepicker__header__dropdown--select').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="2"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1998"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--024').click()

    # Заполнение поля Subjects
    browser.element('#subjectsInput').type('Ma').press_tab()
    browser.element('#subjectsInput').type('Ph')
    browser.element('#react-select-2-option-0').click()

    # Выбор чек-боксов для поля Hobbies
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    # Выбор файла для поля Picture
    browser.element('.form-file').click().element('#uploadPicture').send_keys(
        os.path.abspath('photo.jpeg'))

    # Заполнение поля Current Address
    browser.element('#currentAddress').should(be.blank).type('Republic of Belarus, Minsk')

    # Выбор значений в выпадающих списках State и City
    browser.element('#state').click().element('#react-select-3-option-3').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    # Submit
    browser.element('#submit').click()

    # Проверки
    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts('Boris Shark', 'examplemail@mail.com', 'Male', '2911011214', '24 March,1998', 'Maths, Physics',
                         'Sports, Reading', 'photo.jpeg', 'Republic of Belarus, Minsk', 'Rajasthan Jaipur'))