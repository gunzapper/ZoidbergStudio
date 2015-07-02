# Good news everyone

# Prof Fansworth wants to access the Dr Zoidberg
# sites, to see his medical data.
# He goes to the site.
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

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
