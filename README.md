CSCE3550JWKServer is a Node.js application that serves public keys with unique identifiers (kid) for verifying JSON Web Tokens (JWTs). It supports key expiry for enhanced security and provides an authentication endpoint for issuing JWTs.

Contents
Getting Started
Prerequisites
Installation
Usage
Configuration
Running the Server
Endpoints
/jwks
/auth
Testing
Contributing
License
Getting Started
Prerequisites
To run this project, you need the following prerequisites installed on your system:

Node.js (v14 or higher)
npm (Node Package Manager)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Hasti0013/CSCE3550JWKServer.git
Navigate to the project directory:

bash
Copy code
cd CSCE3550JWKServer
Install project dependencies:

bash
Copy code
npm install
Usage
Configuration
Customize the server configuration and manage RSA key pairs in the server.js file. By default, the server generates a single RSA key pair for demonstration purposes. For production environments, implement a more robust key management strategy.

Running the Server
To start the server, run:

bash
Copy code
npm start
The server listens on port 8080 by default. You can configure the port in the server.js file.

Endpoints
/jwks Endpoint
The /jwks endpoint serves public keys in JWKS (JSON Web Key Set) format. It only serves keys that have not expired.

/auth Endpoint
The /auth endpoint handles authentication and JWT issuance. It returns an unexpired, signed JWT on a POST request. If the "expired" query parameter is present, it issues a JWT signed with the expired key pair and the expired expiry timestamp.

Testing
Basic testing is included using Mocha and Chai. Run the tests with:

bash
Copy code
npm test
Expand the test suite to cover additional scenarios and edge cases.

Contributing
Contributions are welcome! If you find issues or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Thanks!