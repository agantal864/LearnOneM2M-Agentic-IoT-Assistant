Source: https://acmecse.net/setup/Certificates/

# Certificates

The ACME CSE supports the secure protocol version of HTTP, MQTT, and WebSockets. This means that you can use the CSE with HTTPS, MQTT over TLS, and WSS.

To enable, for example, https you have to set various settings under the security configuration [http.security](../Configuration-http/#security), and provide a certificate and a key file. The other protocols are configured in a similar way.

See also

[HTTP Security Settings](../Configuration-http/#security)  
[MQTT Security Settings](../Configuration-mqtt/#security)  
[WebSocket Security Settings](../Configuration-ws/#security)

## Self-Signed Certificates

One way to create those files is the [openssl](https://www.openssl.org) tool that may already be installed on your OS. The following example shows how to create a self-signed certificate:

Create a self-signed certificate

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -nodes -days 1000
```

This will create the self-signed certificate and private key without password protection (*-nodes*), and stores them in the files *cert.pem* and *key.pem* respectively. *openssl* will prompt you with questions for *Country Name* etc, but you can just hit *Enter* and accept the defaults. The *-days* parameter affects the certificate's expiration date.

Please also consult the *openssl* manual for further instructions.

After you generated these files you can move them to a separate directory (for example you may create a new directory named *cert* under ACME's [runtime base directory](../Running/#different-base-directory)) and set the *caCertificateFile* and *caPrivateKeyFile* configuration parameters in the *acme.ini* configuration file under the appropriate security section(s) accordingly.

## HTTP Authentication

The ACME CSE supports the following HTTP authentication methods.

Warning

Note that the credentials are partly stored as plain text (ie. user names) and in hashed form (ie. passwords and tokens) in the respective credential files. Make sure to protect these files accordingly.

### Basic Authentication

The ACME CSE supports basic authentication. To enable it, you have to set the [[http.security].enableBasicAuth](../Configuration-http/#security) configuration parameter in the *acme.ini* configuration file to *True* .

In addition, you have to set the [[http.security].basicAuthFile](../Configuration-http/#security) configuration parameter to the path of a file that contains the user credentials. The file must be in the format *username:password*, and comments are allowed.  
The *password* is **not** as plain text but as a hashed password. You can use the [hashcreds](../../development/tools/HashCredentials/) tool to create a hashed password.

**Example:**

```
# This is a comment
user1:hashedPassword1
user2:hashedPassword2
```

To access the CSE, you have to provide the credentials in the HTTP request header in the form of `Authorization: Basic <credentials>`, where <credentials> is the Base64 encoding of a username and (unhashed) password joined by a single colon.

### Bearer Token Authentication

The ACME CSE also supports a simple form of bearer token authentication. To enable it, you have to set the [[http.security].enableTokenAuth](../Configuration-http/#security) configuration parameter in the *acme.ini* configuration file to *True* .

In addition, you have to set the [[http.security].tokenAuthFile](../Configuration-http/#security) configuration parameter to the path of a file that contains the bearer token. The file must contain lines with each token on a separate line. Comments (lines starting with #) are allowed.  
The token is **not** stored as plain text but as a hashed token. You can use the [hashcreds](../../development/tools/HashCredentials/) tool to create a hashed token.

**Example:**

```
# This is a comment
hashedToken1
hashedToken2
```

In this case to access the CSE, you have to provide the (unhashed) bearer token in the HTTP request header in the form of `Authorization: Bearer <token>`.

## WebSocket Authentication

The ACME CSE supports the same authentication methods for the WebSocket binding as for the HTTP binding. To enable basic or token authentication for the WebSocket binding, you have to set the [[websocket.security].enableBasicAuth](../Configuration-ws/#security) or [[websocket.security].enableTokenAuth](../Configuration-ws/#security) configuration parameter in the *acme.ini* configuration file to *True* .

The configuration parameters are the same as for the HTTP binding. See [HTTP Authentication](#http-authentication) for further details on how to configure the authentication files.