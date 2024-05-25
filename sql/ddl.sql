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

CREATE OR REPLACE FUNCTION update_user_points()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE users
    SET total_points = total_points + NEW.delta
    WHERE discord_id = NEW.discord_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_user_points_after_insert
AFTER INSERT ON user_activity
FOR EACH ROW
EXECUTE FUNCTION update_user_points();

