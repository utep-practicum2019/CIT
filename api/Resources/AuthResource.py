from functools import wraps

from flask import render_template, request

allowed_ips = ["127.0.0.1"]


def is_admin_only(f):
    """
    Wrapper for admin methods to prevent them from being accessed by
    any ip not in allowed_ips
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        if request.environ['REMOTE_ADDR'] not in allowed_ips:
            return render_template('thouShallNotPass.html')
        return f(*args, **kwargs)

    return decorated
