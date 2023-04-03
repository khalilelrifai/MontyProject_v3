"This is a web application built with Django that allows users to create and view ads. Users with admin privileges can create ads, while those with regular user privileges can only view the ads that admins have created.We have used the keycloak identity service "
--------------------------


Prerequisites:
    Django
    django-keycloak-pkg
    Docker
    Docker Compose

In your terminal or command prompt, navigate to the directory containing the docker-compose.yml file and run the following command to start the container:

docker-compose up
This will create and start the Keycloak container. You should be able to access the Keycloak web interface at http://localhost:8080/

Once the container is running, you can log in to the Keycloak admin console using the admin username and password you set in the docker-compose.yml file.

From the admin console,  create a new realm with the name myrealm.

Within the myrealm realm,  create a new client with the ID myclient.

---------------------------
{
  "realm": "myrealm",
  "auth-server-url": "http://localhost:8080/",
  "ssl-required": "external",
  "resource": "myclient",
  "verify-token-audience": true,
  "credentials": {
    "secret": "NX4WP9JqZGg2K0xzGakDGEEyZpr2Kp2H"
  },
  "use-resource-role-mappings": true,
  "confidential-port": 0,
  "policy-enforcer": {}
}

---------------
create two user:
one as an administrator with these permissions: can (add,view,edit,update) ad
another with only can view ad