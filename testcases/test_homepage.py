
import pytest

from pages.home_page import LaunchPage
from pages.whats_new_page import whatsnew


@pytest.mark.usefixtures("setup")

class TestViewItem():

    def test_view_men_clothes(self):
        hp=LaunchPage(self.driver,self.wait)
        np=whatsnew(self.driver,self.wait)


        hp.Whatsnewbutton()
        np.click_Hoodies_Sweatshirts_women()



