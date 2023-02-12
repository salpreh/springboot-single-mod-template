# {{cookiecutter.artifact_id}}

# Getting Started
Base template for SpringBoot project with a PosgresDB and REST API.

## Requirements
`docker` and `docker-compose` to start development postgres DB. Java Development Kit (`jdk`) installed.
Having Maven `mvn` installed is recomended but not required. You could use maven wrapper scripts with:
```sh
./mvnw
```
_NOTE_: Make sure `mvnw` has execution permission.

## Dev environment
Project has a `docker-compose` to start a postgres database container for development. Use docker compose to start development database container with:
```sh
docker compose up -d
```

Complie the project with maven (or maven wrapper if not installed locally)
```sh
# If maven wrapper: ./mvnw clean pacakge
mvn clean package
```

To run the project you can execute `bin/run.sh` script:
```sh
bin/run.sh
```
Or use your IDE to run the main class located in `{{cookiecutter.project_name}}/src/main/java/{{cookiecutter.__package_path}}/Application.java`

## Containerize the application
There is a `Dockerfile` in the root of the project that mounts and runs the compiled application jar. You can use the script `bin/build-docker.sh` to build the docker image or issue the command manually.

## Spring documentation
### Reference Documentation

For further reference, please consider the following sections:

* [Official Apache Maven documentation](https://maven.apache.org/guides/index.html)
* [Spring Boot Maven Plugin Reference Guide](https://docs.spring.io/spring-boot/docs/2.7.1/maven-plugin/reference/html/)
* [Create an OCI image](https://docs.spring.io/spring-boot/docs/2.7.1/maven-plugin/reference/html/#build-image)
* [Spring Data JPA](https://docs.spring.io/spring-boot/docs/2.7.1/reference/htmlsingle/#data.sql.jpa-and-spring-data)
* [Spring Web](https://docs.spring.io/spring-boot/docs/2.7.1/reference/htmlsingle/#web)
* [Spring Configuration Processor](https://docs.spring.io/spring-boot/docs/2.7.1/reference/htmlsingle/#appendix.configuration-metadata.annotation-processor)

### Guides

The following guides illustrate how to use some features concretely:

* [Accessing Data with JPA](https://spring.io/guides/gs/accessing-data-jpa/)
* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
* [Building REST services with Spring](https://spring.io/guides/tutorials/rest/)
