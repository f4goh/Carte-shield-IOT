#
# An example for sending a long email
# with SSL connection
#
# NOTE:
# If the email is too long to fit in an variable,
# you may use write() to send a chunk of the email 
# each time.
#

import umail
smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
smtp.login('nsi.touchard@gmail.com', 'b020b023b025')
smtp.to('f4goh@orange.fr')
smtp.write("From: Bob <nsi.touchard@gmail.com>\n")
smtp.write("To: Alice <f4goh@orange.fr>\n")
smtp.write("Subject: Poem\n\n")
smtp.write("Roses are red.\n")
smtp.write("Violets are blue.\n")
smtp.write("...\n")
smtp.send()
smtp.quit()
