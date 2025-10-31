# Utiliser l'image Python officielle comme base
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Mise à jour des packages (pas de dépendances système nécessaires pour Flask)

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'application
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Exposer le port 5000
EXPOSE 5000

# Définir les variables d'environnement pour Flask
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Créer un utilisateur non-root pour la sécurité
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Commande pour lancer l'application
CMD ["python", "app.py"]

