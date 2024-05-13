from selene import browser, have, be
import os


def test_number():
    browser.open('/')
    browser.driver.execute_script(
        "document.querySelector('.body-height').style.transform='scale(.20)'")

    # Заполнение полей FirstName и LastName
    browser.element('#firstName').should(be.blank).type('Boris')
    browser.element('#firstName').should(have.value('Boris'))
    browser.element('#lastName').should(be.blank).type('Shark')
    browser.element('#lastName').should(have.value('Shark'))

    # Заполнение поля Email
    browser.element('#userEmail').should(be.blank).type('examplemail@mail.com')
    browser.element('#userEmail').should(have.value('examplemail@mail.com'))

    # Выбор радио-кнопки для поля Gender
    browser.element('#genterWrapper').all('label[for^=gender-radio]').element_by(have.text('Male')).click()

    # Заполнение поля Mobile
    browser.element('#userNumber').should(be.blank).type('2911011214')
    browser.element('#userNumber').should(have.value('2911011214'))

    # Заполнение поля Date of Birth
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__header__dropdown react-datepicker__header__dropdown--select"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="2"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1998"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--024"]').click()

    # Заполнение поля Subjects
    browser.element('#subjectsInput').type('Ma').press_tab()
    browser.element('#subjectsInput').type('Ph')
    browser.element('#react-select-2-option-0').click()

    # Выбор чек-боксов для поля Hobbies
    browser.element('#hobbiesWrapper').all('label[for^=hobbies-checkbox]').element_by(have.text('Reading')).click()
    browser.element('#hobbiesWrapper').all('label[for^=hobbies-checkbox]').element_by(have.text('Sports')).click()

    # Выбор файла для поля Picture
    browser.element('[class="form-file"]').click().element('#uploadPicture').send_keys(
        os.path.abspath('/Users/mborja/PycharmProjects/HW5/tests/photo.jpeg'))

    # Заполнение поля Current Address
    browser.element('#currentAddress').should(be.blank).type('Republic of Belarus, Minsk')
    browser.element('#currentAddress').should(have.value('Republic of Belarus, Minsk'))

    # Выбор значений в выпадающих списках State и City
    browser.element('#state').click().element('#react-select-3-option-3').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    browser.element('#city').click()

    # Submit
    browser.element('#submit').click()

    # Проверки
    browser.element('[class="modal-content"]').element('table').all('tr').all('td').even.should(
        have.exact_texts('Boris Shark', 'examplemail@mail.com', 'Male', '2911011214', '24 March,1998', 'Maths, Physics',
                         'Reading, Sports', 'photo.jpeg', 'Republic of Belarus, Minsk', 'Rajasthan Jaipur'))
