import website_alive.check_response as check


def adres():
    s = input()
    if check.site(s):
        print('Available')


adres()
