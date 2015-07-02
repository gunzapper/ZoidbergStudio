# Good news everyone

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_first_access_to_site(self):
        # Prof Fansworth wants to access the Dr Zoidberg
        # sites, to see his medical data.
        # He goes to the site.
        self.browser.get('http://localhost:8000')
        # Fansworth notices that the title is
        # right
        self.assertIn("Zoidberg's Studios", self.browser.title)

        # He notice that it is impossible to access
        # without credetial. It's his first time
        # (but Fansworth not ever has a good memories)
        # He looks that, after the title box, there are two links
        # "Sing Up" and "Log In".
        # He chooses to push "Sign up"

        # He inserts his data on form.
        # Zoidberg is very unprepared
        # and the site's application form
        # require only a Nickname and
        # a password.

        # After registration Fansworth goes again to the
        # main page, and insert his credetials

        # Fry does not has credetial
        # and does access the site

        # Fansworth looks a slide on the left
        # and the medical data on the right.

        # Fansworth looks that Zoiberg makes an error
        # inserting data. Fansworth tryes to modifies data.

        # To be sure that the modifications had registered
        # Fansworth colose his browser, access again
        # and look the data.

        # All is fine, happy, Fansworth goes to take a nap
        # on his fling cy, Fansworth goes to take a nap
        # on his fling couch.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
