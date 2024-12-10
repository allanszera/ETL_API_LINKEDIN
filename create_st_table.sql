CREATE DATABASE STAGING_AREA;

USE STAGING_AREA;

CREATE TABLE dbo.Vagas_linkedin (
    id               VARCHAR(255),
    title            VARCHAR(255),
    url              VARCHAR(500),
    referenceId      VARCHAR(255),
    posterId         VARCHAR(255),
    location         VARCHAR(255),
    type             VARCHAR(100),
    postDate         VARCHAR(100),
    postAt           VARCHAR(100),
    postedTimestamp  BIGINT,
    company_name     VARCHAR(255),
    company_logo     VARCHAR(500),
    company_url      VARCHAR(500),
    PRIMARY KEY (id)
);
