import allure
import pytest
from allure_commons.types import Severity

from model.pages.profile_settings import SettingsProfilePage

settings_profile_page = SettingsProfilePage()


@allure.title('Никнейм одинаковый в хедере и на странице')
@allure.tag('web')
@allure.link('/profile.php?view=settings')
@allure.feature('Настройки профиля пользователя')
@allure.severity(Severity.CRITICAL)
def test_header_nick_contains_on_page(user):
    settings_profile_page.open()
    settings_profile_page.should_contain_header_nickname()


@allure.title('Страница содержит верные заголовки')
@allure.tag('web')
@allure.link('/profile.php?view=settings')
@allure.feature('Настройки профиля пользователя')
@allure.severity(Severity.CRITICAL)
def test_profile_sectoin_names(user):
    settings_profile_page.open()
    settings_profile_page.should_contain_section_names('Nick',
                                                       'Place of residence')


@allure.title('Кнопка профиля активна в меню настроек')
@allure.tag('web')
@allure.link('/profile.php?view=settings')
@allure.feature('Настройки профиля пользователя')
def test_if_profile_in_settings_dropdown_is_active(user):
    settings_profile_page.open()
    settings_profile_page.should_be_active_in_settigs_dropdown()


@allure.title('Не первая попытка смены ника содержит сообщение об оплате')
@allure.tag('web')
@allure.link('/profile.php?view=settings')
@allure.feature('Настройки профиля пользователя')
def test_change_nickname_second_time(user):
    settings_profile_page.open()
    settings_profile_page.click_change_nick()
    settings_profile_page.should_have_advice_text(
        'You can once change your nick for free. All next changes have to be purchased separately.'
    )


@allure.title('Изменение страны профиля')
@allure.tag('web')
@allure.link('/profile.php?view=settings')
@allure.feature('Настройки профиля пользователя')
@pytest.mark.parametrize('residency', ['Andorra', 'Aruba'])
def test_change_location(user, residency):
    settings_profile_page.open()
    settings_profile_page.change_residency(residency)
    settings_profile_page.open()

    settings_profile_page.should_have_residency(residency)
