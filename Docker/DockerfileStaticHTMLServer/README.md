## 📁 Dockerfile : serveur HTML statique avec Nginx

### 📄 Assurez-vous d’avoir un fichier `index.html` dans le même dossier.

### 🔧 Build
```bash
docker build -t nginx-static -f Dockerfile .
```

### ▶️ Run
```bash
docker run -d -p 8080:80 nginx-static
```

📂 Accès à la page : [http://localhost:8080](http://localhost:8080)