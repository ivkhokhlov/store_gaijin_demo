import allure
from selene.support.shared import browser
from selene import have, query


class SettingsProfilePage:

    def __init__(self):
        pass

    @allure.step('Открыть страницу настроек профиля')
    def open(self):
        browser.open('/profile.php?view=settings')

    @allure.step('Нажать на иконку смены ника')
    def click_change_nick(self):
        browser.element('.profile-settings__icon-edit').click()

    @allure.step('Сменить местоположение')
    def change_residency(self, residency):
        browser.element('.profile-settings__edit-link').click()
        browser.element('.input-select').send_keys(residency)
        browser.element('.profile-settings__section--content-button').click()

    @allure.step('Проверка текста сообщения')
    def should_have_advice_text(self, text_on_page):
        browser.element('.shop__advice').should(have.text(text_on_page))

    @allure.step('Проверка местоположения')
    def should_have_residency(self, residency):
        browser.element('.profile-settings__section--content > div').should(have.text(residency))

    @allure.step('Проверка соответствия ника в заголовке и в шапке')
    def should_contain_header_nickname(self):
        header_nick = browser.element('.GCM-Menu-Item__profile').get(query.text)
        browser.element('.profile-settings__wrapper').should(have.text(header_nick))

    @allure.step('Проверка заголовков полей настроек')
    def should_contain_section_names(self, *titles):
        for title in titles:
            browser.element('.profile-settings__wrapper').should(have.text(title))

    @allure.step('Проверка активности профиля в меню настроек')
    def should_be_active_in_settigs_dropdown(self):
        active_item_text = browser.element('.profile-menu-dropdown__link_active').get(query.text_content)
        assert 'Profile' in active_item_text
