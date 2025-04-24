CREATE TABLE IF NOT EXISTS messages (
  id SERIAL PRIMARY KEY,
  text TEXT NOT NULL
);

INSERT INTO messages (text) VALUES
('Hello 👋'),
('Bienvenue dans Docker 🐳'),
('Tu gères ! 🚀');
