CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  discord_id TEXT NOT NULL,
  total_points INT
);

CREATE TABLE user_activity (
  id SERIAL PRIMARY KEY,
  reason TEXT NOT NULL,
  delta INT,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);