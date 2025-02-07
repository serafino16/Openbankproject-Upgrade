
FROM openjdk:11-jdk


WORKDIR /app


COPY target/open-bank-api.jar /app/open-bank-api.jar


EXPOSE 8080


CMD ["java", "-jar", "open-bank-api.jar"]
