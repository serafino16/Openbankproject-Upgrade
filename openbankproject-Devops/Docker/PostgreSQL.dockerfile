
FROM postgres:13


ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=adminpassword
ENV POSTGRES_DB=open_bank_db


EXPOSE 5432
