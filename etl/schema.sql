-- Schema for Climate/Air Quality Forecasting System

-- Create raw_data table
-- Used for storing raw API responses for auditing and reprocessing
CREATE TABLE IF NOT EXISTS raw_data (
    id SERIAL PRIMARY KEY,
    source VARCHAR(255) NOT NULL, -- e.g., 'OpenAQ', 'OpenWeatherMap'
    measurement_timestamp TIMESTAMP WITH TIME ZONE,
    raw_payload JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create staging_data table
-- Used for parsed, cleaned, and normalized data ready for analysis and ML models
CREATE TABLE IF NOT EXISTS staging_data (
    id SERIAL PRIMARY KEY,
    location_name VARCHAR(255) NOT NULL,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    measurement_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    temperature DECIMAL(5,2), -- in Celsius
    humidity DECIMAL(5,2),    -- percentage
    pm2_5 DECIMAL(8,2),       -- PM2.5 concentration (µg/m³)
    pm10 DECIMAL(8,2),        -- PM10 concentration (µg/m³)
    aqi INTEGER,              -- Air Quality Index
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for frequent querying
CREATE INDEX idx_raw_data_source ON raw_data(source);
CREATE INDEX idx_raw_data_timestamp ON raw_data(measurement_timestamp);

CREATE INDEX idx_staging_data_location ON staging_data(location_name);
CREATE INDEX idx_staging_data_timestamp ON staging_data(measurement_timestamp);
