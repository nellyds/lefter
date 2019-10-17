import yagmail


def allDoneSwiping():
    receiver = "en.de.es.developer@gmail.com"
    body = "Probably, no matches.  But hey, at least you wrote this low-level application.  Makes it all worth it, right?"

    yag = yagmail.SMTP("en.de.es.developer@gmail.com")
    yag.send(
        to=receiver,
        subject="All done Bumbling, get back to work, sport.",
        contents=body,
    )