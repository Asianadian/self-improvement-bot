CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  discord_id TEXT UNIQUE NOT NULL,
  total_points INT
);

CREATE TABLE user_activity (
  id SERIAL PRIMARY KEY,
  reason TEXT NOT NULL,
  delta INT,
  discord_id TEXT,
  FOREIGN KEY (discord_id) REFERENCES users(discord_id)
);

