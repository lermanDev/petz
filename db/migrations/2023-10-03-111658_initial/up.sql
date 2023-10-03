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
  name VARCHAR,
  specie VARCHAR,
  gender gender,
  characteristics VARCHAR,
  health VARCHAR,
  description VARCHAR,
  size size,
  weight FLOAT,
  birth_date TIMESTAMP,
  image_url_list JSONB,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);

-- Create the User table
CREATE TABLE "User" (
  user_id VARCHAR PRIMARY KEY,
  username VARCHAR,
  password VARCHAR,
  email VARCHAR,
  role user_role,
  address VARCHAR,
  city VARCHAR,
  phone VARCHAR,
  image_url VARCHAR,
  settings JSONB,
  created_at TIMESTAMP default now(),
  updated_at TIMESTAMP default now()
);

-- Create the Shelter table
CREATE TABLE "Shelter" (
  shelter_id VARCHAR PRIMARY KEY,
  name VARCHAR,
  address VARCHAR,
  city VARCHAR,
  phone VARCHAR,
  email VARCHAR,
  description VARCHAR,
  website VARCHAR,
  logo_image_url VARCHAR,
  gallery_image_url VARCHAR,
  created_at TIMESTAMP default now(),
  updated_at TIMESTAMP default now()
);

-- Create the Adoption table
CREATE TABLE "Adoption" (
  id serial PRIMARY KEY,
  pet_id INTEGER,
  user_id VARCHAR,
  shelter_id VARCHAR,
  adopted_by_id INTEGER,
  status adoption_status,
  extra_location VARCHAR,
  entry_date TIMESTAMP,
  description VARCHAR,
  created_at TIMESTAMP default now(),
  updated_at TIMESTAMP default now()
);

-- Add foreign key constraints
ALTER TABLE "Adoption" ADD CONSTRAINT pet_fk FOREIGN KEY (pet_id) REFERENCES "Pet" (pet_id);
ALTER TABLE "Adoption" ADD CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES "User" (user_id);
ALTER TABLE "Adoption" ADD CONSTRAINT shelter_fk FOREIGN KEY (shelter_id) REFERENCES "Shelter" (shelter_id);