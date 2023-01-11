from unittest.mock import patch

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import RecipeBaseFunctionalTest


@pytest.mark.functional_test
class RecipeHomePageTest(RecipeBaseFunctionalTest):
    @patch('recipes.views.PER_PAGES', new=2)
    def test_recipe_home_page_without_recipes(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(by=By.TAG_NAME, value='body')
        self.assertIn('No recipes found here, create you own', body.text)

    @patch('recipes.views.PER_PAGES', new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch(10)

        title_needed = 'This is what I need'

        recipes[0].title = title_needed
        recipes[0].save()

        self.browser.get(self.live_server_url)

        search_input = self.browser.find_element(
            By.XPATH,
            '//input[@placeholder="Search for a recipe"]'
        )

        search_input.send_keys(title_needed)
        search_input.send_keys(Keys.ENTER)

        self.assertIn(
            title_needed,
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    @patch('recipes.views.PER_PAGES', new=2)
    def test_recipe_homepage_pagination(self):
        self.make_recipe_in_batch(10)

        self.browser.get(self.live_server_url)

        page2 = self.browser.find_element(
            By.XPATH,
            '//a[@aria-label="Go to page 2"]'
        )

        page2.click()

        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe')), 2
        )
