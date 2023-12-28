import os

from selene import browser, have, command


def test_sign_up_all_fields_success():
    browser.open('/automation-practice-form')
    # Fill in personal data
    browser.element('#firstName').type('FirstName')
    browser.element('#lastName').type('LastName')
    browser.element('#userEmail').type('email@email.email')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567890')

    # Fill in date birth 1990-01-01
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('[value="1990"]').click()
    browser.element('.react-datepicker__month-select').element('[value="0"]').click()
    browser.element('.react-datepicker__day--001').click()

    # Fill in subject maths
    browser.element('#subjectsInput').click().type('a').press_enter()

    # Fill in hobby
    browser.element('[for="hobbies-checkbox-2"]').click()

    # Add picture
    browser.element('.form-file-label').perform(command.js.scroll_into_view)
    browser.element('#uploadPicture').send_keys(os.getcwd() + "/resources/windy_hill.jpg")

    # Fill in current address with multiple lines
    browser.element('#currentAddress').type('45 Current Address')

    # Select state and city
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('#currentAddress').press_tab()
    browser.element('#state').click()
    browser.element('#state').element('#react-select-3-option-0').click()

    browser.element('#city').click()
    browser.element('#stateCity-wrapper').element('#react-select-4-option-0').click()

    # Submit form
    browser.element('#submit').press_enter()

    # Check data
    browser.element('.table-responsive').all('td:nth-child(2)')[0].should(have.text('FirstName LastName'))
    browser.element('.table-responsive').all('td:nth-child(2)')[1].should(have.text('email@email.email'))
    browser.element('.table-responsive').all('td:nth-child(2)')[2].should(have.text('Female'))
    browser.element('.table-responsive').all('td:nth-child(2)')[3].should(have.text('1234567890'))
    browser.element('.table-responsive').all('td:nth-child(2)')[4].should(have.text('1 January,1990'))
    browser.element('.table-responsive').all('td:nth-child(2)')[5].should(have.text('Maths'))
    browser.element('.table-responsive').all('td:nth-child(2)')[6].should(have.text('Reading'))
    browser.element('.table-responsive').all('td:nth-child(2)')[7].should(have.text('windy_hill.jpg'))
    browser.element('.table-responsive').all('td:nth-child(2)')[8].should(have.text('45 Current Address'))
    browser.element('.table-responsive').all('td:nth-child(2)')[9].should(have.text('NCR Delhi'))

