import unittest
from securityheaders import get_headers_of_domain
from securityheaders import get_strict_transport_security

class TestSecurityheadersPy(unittest.TestCase):
    #def test_get_heafers_of_domain(self):
        #self.assertEqual(get_headers_of_domain("https://www.signicat.com"), "Expect-CT")

    def test_strict_transport_security(self):
        self.assertEqual(get_strict_transport_security("https://id.signicat.com"), "max-age=31536000; includeSubDomains")


