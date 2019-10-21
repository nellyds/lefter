import yagmail


def allDoneSwiping(loginName):
    receiver = loginName
    body = "Probably, no matches.  But hey, at least you wrote this low-level application.  Makes it all worth it, right?"

    yag = yagmail.SMTP("en.de.es.developer@gmail.com")
    yag.send(
        to=receiver,
        subject="All done Swiping, get back to work, sport.",
        contents=body,
    )