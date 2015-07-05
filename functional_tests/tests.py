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
        # Prof Fanrsworth wants to access the Dr Zoidberg
        # sites, to see his medical data.
        # He goes to the site.
        self.browser.get(self.live_server_url)
        # Farnsworth notices that the title is
        # right
        self.assertIn("Zoidberg's Studios", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Zoidberg's Studios", header_text)

        ##-----------------------------------------------------------------
        ## I develop authorization after
        ## or use the admin back-end

        # He notice that it is impossible to access
        # without credetial. It's his first time
        # (but Farnsworth not ever has a good memories)
        # He looks that, after the title box, there are two links
        # "Sing Up" and "Log In".
        # He chooses to push "Sign up"

        # He inserts his data on form.
        # Zoidberg is very unprepared
        # and the site's application form
        # require only a Nickname and
        # a password.

        # After registration Farnsworth goes again to the
        # main page, and insert his credetials

        # Fry does not has credetial
        # and does access the site
        ##---------------------------------------------------------

        # Farnsworth looks a slide on the left

        # and the medical data on the right.
        self.check_for_row_in_metadata_table('default metadata here')

        inputbox = self.browser.find_element_by_id('id_change_metadata')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'default metadata here'
        )

        # Farnsworth looks that Zoiberg makes an error
        # inserting data. Farnsworth tryes to modifies data.
        inputbox.send_keys("Good news every one")
        inputbox.send_keys(Keys.ENTER)
        farnsworth_url = self.browser.current_url
        self.assertRegex(farnsworth_url, '/dicom_visio/.+')
        ## Probably it is better a button
        ## when pushed the sites updates the metadata
        ## And reload the metadata to the box

        # Farnsworth look that the table is changed
        self.check_for_row_in_metadata_table('Good news every one')

        # A new user, prof Wernstrom, come along the site.

        ## We use a new browser session to make sure that no information
        ## of Farnsworth's is coming thourgh form cokies etc...
        self.browser.quit()
        self.browser =  webdriver.Firefox()

        # Wernstrom modifies his dicom metadata
        inputbox = self.browser.find_element_by_id('id_change_metadata')
        inputbox.send_keys('I am the best')
        inputbox.send_keys(Keys.ENTER)

        # Wernstrom gets his own unique URL
        wernstorm_url = self.browser.current_url
        self.assertRegex(wernstorm_url, '/dicom_visio/.+')
        self.assertNotEqual(wernstorm_url, farnsworth_url)

        # Again, there is no trace of Farnsworth's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Good news every one', page_text)
        self.assertIn('I am the best', page_text)

        # To be sure that the modifications had registered
        # Farnsworth colose his browser, access again
        # and look the data.

        # All is fine, happy, Farnsworth goes to take a nap
        # on his fling cy, Farnsworth goes to take a nap
        # on his fling couch.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
