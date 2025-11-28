-- Optionally drop the database and recreate it
-- Ensure this only happens if you have a way to safely connect to the database
-- WARNING: This will remove the entire database and all its data!

-- Drop the database if it exists
DROP DATABASE IF EXISTS digital_signature_service;

-- Create the database again
CREATE DATABASE digital_signature_service;

-- Connect to the newly created database (this part depends on how you're executing the script)
\c digital_signature_service;

-- Optionally, drop the tables if they already exist
DROP TABLE IF EXISTS signatures;
DROP TABLE IF EXISTS documents;

-- Create the "documents" table
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,                     -- Auto-incrementing primary key
    document_id VARCHAR UNIQUE NOT NULL,       -- Unique document ID
    content TEXT,                              -- Content of the document
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp with default as current time
);

-- Create an index on the "document_id" column for faster lookups
CREATE INDEX idx_documents_document_id ON documents (document_id);

-- Create the "signatures" table
CREATE TABLE signatures (
    id SERIAL PRIMARY KEY,                     -- Auto-incrementing primary key
    signature_id VARCHAR UNIQUE NOT NULL,      -- Unique signature ID
    document_id VARCHAR NOT NULL,              -- Document ID (foreign key)
    signed_at TIMESTAMP NOT NULL,              -- Timestamp when document was signed
    signature_value TEXT NOT NULL,             -- Signature value (e.g., base64 encoded)
    
    -- Foreign key constraint referencing "documents" table
    CONSTRAINT fk_document FOREIGN KEY (document_id) REFERENCES documents (document_id)
);

-- Create an index on the "document_id" column for faster lookups
CREATE INDEX idx_signatures_document_id ON signatures (document_id);
