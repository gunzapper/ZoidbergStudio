# Good news everyone

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_metadata_table(self, row_text):
        table = self.browser.find_element_by_id('id_metadata_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
             any(row.text == row_text for row in rows),
             "New metadata did not appear in table -- its text was:\n%s" %(table.text, )
        )

    def test_first_access_to_site(self):
        # Prof Fansworth wants to access the Dr Zoidberg
        # sites, to see his medical data.
        # He goes to the site.
        self.browser.get(self.live_server_url)
        # Fansworth notices that the title is
        # right
        self.assertIn("Zoidberg's Studios", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Zoidberg's Studios", header_text)

        ##-----------------------------------------------------------------
        ## I develop authorization after
        ## or use the admin back-end

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
        ##---------------------------------------------------------

        # Fansworth looks a slide on the left

        # and the medical data on the right.
        self.check_for_row_in_metadata_table('default metadata here')

        inputbox = self.browser.find_element_by_id('id_change_metadata')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'default metadata here'
        )

        # Fansworth looks that Zoiberg makes an error
        # inserting data. Fansworth tryes to modifies data.
        inputbox.send_keys("Good news every one")
        inputbox.send_keys(Keys.ENTER)
        ## Probably it is better a button
        ## when pushed the sites updates the metadata
        ## And reload the metadata to the box

        # Fansworth look that the table is changed
        self.check_for_row_in_metadata_table('Good news every one')

        # To be sure that the modifications had registered
        # Fansworth colose his browser, access again
        # and look the data.

        # All is fine, happy, Fansworth goes to take a nap
        # on his fling cy, Fansworth goes to take a nap
        # on his fling couch.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
