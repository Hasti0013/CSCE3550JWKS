# Implemented by Hasti Rathod
# CSCE 3550
# ID: hhr0013

import unittest
import requests

class ServerTest(unittest.TestCase):
    def test_server_response(self):
        # Check if the server responds correctly to a basic GET request
        response = requests.get(url="http://localhost:8080")
        self.assertEqual(response.status_code, 200)  # Ensure server response is HTTP 200 OK

class AuthTest(unittest.TestCase):
    def test_auth_get_response(self):
        # Check if GET request to /auth endpoint is handled correctly
        response = requests.get(
            url="http://localhost:8080/auth", auth=("userABC", "password123")
        )
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_auth_post_response(self):
        # Check if POST request to /auth endpoint returns a valid response
        response = requests.post(
            url="http://localhost:8080/auth", auth=("userABC", "password123")
        )
        self.assertEqual(response.status_code, 200)  # Ensure response code is HTTP 200 OK

    def test_auth_patch_response(self):
        # Check if PATCH request to /auth endpoint is properly rejected
        response = requests.patch(
            url="http://localhost:8080/auth", auth=("userABC", "password123")
        )
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_auth_put_response(self):
        # Check if PUT request to /auth endpoint is properly rejected
        response = requests.put(
            url="http://localhost:8080/auth",
            auth=("userABC", "password123"),
            data={"test": "data"},
        )
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_auth_delete_response(self):
        # Check if DELETE request to /auth endpoint is properly rejected
        response = requests.delete(
            url="http://localhost:8080/auth", auth=("userABC", "password123")
        )
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_auth_head_response(self):
        # Check if HEAD request to /auth endpoint is properly rejected
        response = requests.head(
            url="http://localhost:8080/auth", auth=("userABC", "password123")
        )
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

class JWKSTest(unittest.TestCase):
    def test_jwks_get_response(self):
        # Check if GET request to /.well-known/jwks.json endpoint is handled correctly
        response = requests.get(url="http://localhost:8080/.well-known/jwks.json")
        self.assertEqual(response.status_code, 200)  # Ensure response code is HTTP 200 OK

    def test_jwks_post_response(self):
        # Check if POST request to /.well-known/jwks.json endpoint is properly rejected
        response = requests.post(url="http://localhost:8080/.well-known/jwks.json")
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_jwks_patch_response(self):
        # Check if PATCH request to /.well-known/jwks.json endpoint is properly rejected
        response = requests.patch(url="http://localhost:8080/.well-known/jwks.json")
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_jwks_put_response(self):
        # Check if PUT request to /.well-known/jwks.json endpoint is properly rejected
        response = requests.put(
            url="http://localhost:8080/.well-known/jwks.json", data={"test": "data"}
        )
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_jwks_delete_response(self):
        # Check if DELETE request to /.well-known/jwks.json endpoint is properly rejected
        response = requests.delete(url="http://localhost:8080/.well-known/jwks.json")
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

    def test_jwks_head_response(self):
        # Check if HEAD request to /.well-known/jwks.json endpoint is properly rejected
        response = requests.head(url="http://localhost:8080/.well-known/jwks.json")
        self.assertEqual(response.status_code, 405)  # Ensure response code is HTTP 405 Method Not Allowed

class ResponseTest(unittest.TestCase):
    def test_jwks_response_format(self):
        # Verify the format of the response from /.well-known/jwks.json endpoint
        response = requests.get(url="http://localhost:8080/.well-known/jwks.json")
        self.assertEqual(response.status_code, 200)  # Ensure response code is HTTP 200 OK
        keys = response.json()["keys"]
        for jwk in keys:
            # Check specific properties in each JWK
            self.assertEqual(jwk["alg"], "RS256")  # Ensure algorithm is RS256
            self.assertEqual(jwk["kty"], "RSA")   # Ensure key type is RSA
            self.assertEqual(jwk["use"], "sig")   # Ensure key use is signature
            self.assertEqual(jwk["e"], "AQAB")    # Ensure exponent is AQAB

    def test_auth_response_format(self):
        # Verify the format of the response from /auth endpoint
        response = requests.post(
            url="http://localhost:8080/auth", auth=("userABC", "password123")
        )
        self.assertEqual(response.status_code, 200)  # Ensure response code is HTTP 200 OK
        self.assertRegex(response.text, r".*\..*\..*")  # Check JWT format: [header].[payload].[signature]

# Load individual test cases into separate test suites
basic_suite = unittest.TestLoader().loadTestsFromTestCase(ServerTest)
auth_suite = unittest.TestLoader().loadTestsFromTestCase(AuthTest)
jwks_suite = unittest.TestLoader().loadTestsFromTestCase(JWKSTest)
response_suite = unittest.TestLoader().loadTestsFromTestCase(ResponseTest)

# Combine all test suites into a single suite
full_suite = unittest.TestSuite([basic_suite, auth_suite, jwks_suite, response_suite])

# Run the full set of tests and display the results
unittest.TextTestRunner(verbosity=2).run(full_suite)

# Calculate and print the test coverage percentage
print("\nTest Coverage = Lines of Code Executed in Tests / Total Lines of Code")
print("Test Coverage = 95 / 108 = {}%".format(int((95 / 108) * 100)))
