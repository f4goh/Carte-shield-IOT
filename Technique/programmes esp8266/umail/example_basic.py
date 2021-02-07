#
# An bare minimium example for sending a email
# without SSL connection
#

import umail
smtp = umail.SMTP('smtp.gmail.com', 587, username='xxxxx@gmail.com', password='xxxxxx')
smtp.to('xxxx@orange.fr')
smtp.send("This is an example.")
smtp.quit()

