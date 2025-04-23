## 📁 Dockerfile : serveur web Python

### 📄 Fichier `server.py` requis (contenu du serveur Python)

### 🔧 Build
```bash
docker build -t python-server -f Dockerfile .
```

### ▶️ Run
```bash
docker run -p 8000:8000 python-server
```

📂 Accès au serveur : [http://localhost:8000](http://localhost:8000)
