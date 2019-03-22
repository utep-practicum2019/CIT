import unittest
from .Session import Session
#from ConnectionManager import ConnectionManager


class SessionTestDriver(unittest.TestCase):

    session = []

    """
    Valid session that should pass all validity checks.
    """
    session.append(Session("username", "192.168.0.1", "00:34", "-", "connected", "ppp"))

    """
    
    """
    session.append(Session("aaaa", "192.168.0.1", "00:34", "-", "connected", "ppp"))
    session.append(Session(True, "192.168.0.1", "00:34", "-", "connected", "ppp"))
    session.append(Session(1234, "192.168.0.1", "00:34", "-", "connected", "ppp"))

    """
    
    """
    session.append(Session("username", 19216801, "00:34", "-", "connected", "ppp"))
    session.append(Session("username", "592.568.990.451", "00:34", "-", "connected", "ppp"))
    session.append(Session("username", "a.b.c.d", "00:34", "-", "connected", "ppp"))

    """
    
    """
    session.append(Session("username", "192.168.0.1", "99:99", "-", "connected", "ppp"))
    session.append(Session("username", "192.168.0.1", "-89:34", "-", "connected", "ppp"))
    session.append(Session("username", "192.168.0.1", "aa:bb", "-", "connected", "ppp"))

    """
    
    """
    session.append(Session("username", "192.168.0.1", "00:34", 1, "connected", "ppp"))
    session.append(Session("username", "192.168.0.1", "00:34", "55555", "connected", "ppp"))
    session.append(Session("username", "192.168.0.1", "00:34", False, "connected", "ppp"))

    """
    
    """
    session.append(Session("username", "192.168.0.1", "00:34", "-", 1, "ppp"))
    session.append(Session("username", "192.168.0.1", "00:34", "-", "conn", "ppp"))
    session.append(Session("username", "192.168.0.1", "00:34", "-", True, "ppp"))

    def test_session_validity_check(self):
        self.assertEqual(self.session[0].validity_check(), [])

    def test_svc_username(self):
        self.assertEqual(self.session[1].validity_check(), ['Invalid username'])
        self.assertEqual(self.session[2].validity_check(), ['Invalid username'])
        self.assertEqual(self.session[3].validity_check(), ['Invalid username'])

    def test_svc_public_ip(self):
        self.assertEqual(self.session[4].validity_check(), ['Invalid IP address'])
        self.assertEqual(self.session[5].validity_check(), ['Invalid IP address'])
        self.assertEqual(self.session[6].validity_check(), ['Invalid IP address'])

    def test_svc_start_time(self):
        self.assertEqual(self.session[7].validity_check(), ['Invalid start time'])
        self.assertEqual(self.session[8].validity_check(), ['Invalid start time'])
        self.assertEqual(self.session[9].validity_check(), ['Invalid start time'])

    def test_svc_end_time(self):
        self.assertEqual(self.session[10].validity_check(), ['Invalid end time'])
        self.assertEqual(self.session[11].validity_check(), ['Invalid end time'])
        self.assertEqual(self.session[12].validity_check(), ['Invalid end time'])

    def test_svc_status(self):
        self.assertEqual(self.session[13].validity_check(), ['Invalid status'])
        self.assertEqual(self.session[14].validity_check(), ['Invalid status'])
        self.assertEqual(self.session[15].validity_check(), ['Invalid status'])


if __name__ == '__main__':
    unittest.main()