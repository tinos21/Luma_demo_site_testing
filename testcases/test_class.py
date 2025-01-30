import time

import pytest
from pages.home_page import LaunchPage
from pages.whats_new_page import whatsnew
from pages.women_page import womenpage

import pytest

@pytest.mark.usefixtures("setup")


class Test:





    def test_home_page(self):
        hp = LaunchPage(self.driver, self.wait)
        wm = womenpage(self.driver, self.wait)

        hp.Womendropdown()
        time.sleep(4)
        wm.click_shopBytop_50()
        time.sleep(10)
        hp.Whatsnewbutton()



    @pytest.mark.parametrize("whatsnewpage",[
        "test_TC02_click_Hoodies_Sweatshirts_women_verify_navigation",
        "test_TC03_click_Jackets_women_verify_navigation",
        "test_TC04_click_Tees_women_verify_navigation",
        "test_TC05_click_Bras_Tanks_women_verify_navigation",
        "test_TC06_click_Pants_women_verify_navigation",
        "test_TC07_click_Shorts_women_verify_navigation"

    ])

    def test_view_men_clothes(self, whatsnewpage):
        np = whatsnew(self.driver, self.wait)
        getattr(np, whatsnewpage)()




