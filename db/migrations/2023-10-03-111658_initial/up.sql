-- Create the adoption_status ENUM type
CREATE TYPE adoption_status AS ENUM ('ready', 'special_condition', 'reserved', 'waiting', 'adopted', 'deleted');

-- Create the gender ENUM type
CREATE TYPE gender AS ENUM ('male', 'female');

-- Create the size ENUM type
CREATE TYPE size AS ENUM ('small', 'medium', 'large', 'giant');

-- Create the role ENUM type
CREATE TYPE user_role AS ENUM ('admin', 'shelter', 'user');

-- Create the Pet table
CREATE TABLE "Pet" (
  pet_id serial PRIMARY KEY,
  name VARCHAR(50),
  specie VARCHAR(50),
  gender gender,
  characteristics VARCHAR(255),
  health VARCHAR(50),
  description VARCHAR(500),
  size size,
  weight FLOAT,
  birth_date TIMESTAMP,
  image_url_list JSONB,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Create the User table
CREATE TABLE "User" (
  user_id CHAR(25) PRIMARY KEY,
  username VARCHAR(100),
  password VARCHAR(300),
  email VARCHAR(300),
  role user_role,
  address VARCHAR(255),
  city VARCHAR(50),
  phone VARCHAR(12),
  image_url VARCHAR(500),
  settings JSONB,
  created_at TIMESTAMP default now(),
  updated_at TIMESTAMP default now()
);

-- Create the Shelter table
CREATE TABLE "Shelter" (
  shelter_id CHAR(25) PRIMARY KEY,
  name VARCHAR(100),
  address VARCHAR(255),
  city VARCHAR(50),
  phone VARCHAR(12),
  email VARCHAR(300),
  description VARCHAR(500),
  website VARCHAR(300),
  logo_image_url VARCHAR(500),
  gallery_image_url VARCHAR(500),
  created_at TIMESTAMP default now(),
  updated_at TIMESTAMP default now()
);

-- Create the Adoption table
CREATE TABLE "Adoption" (
  id serial PRIMARY KEY,
  pet_id INTEGER,
  user_id CHAR(25),
  shelter_id CHAR(25),
  adopted_by_id INTEGER,
  status adoption_status,
  extra_location VARCHAR(255),
  entry_date TIMESTAMP,
  description VARCHAR(255),
  created_at TIMESTAMP default now(),
  updated_at TIMESTAMP default now()
);

-- Add foreign key constraints
ALTER TABLE "Adoption" ADD CONSTRAINT pet_fk FOREIGN KEY (pet_id) REFERENCES "Pet" (pet_id);
ALTER TABLE "Adoption" ADD CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "User" (user_id);
ALTER TABLE "Adoption" ADD CONSTRAINT shelter_fk FOREIGN KEY (shelter_id) REFERENCES "Shelter" (shelter_id);