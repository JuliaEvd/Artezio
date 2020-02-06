import website_alive.make_request as mr


def site(s):
    if mr.make(s).status_code == 200:
        return True
    else:
        return False
