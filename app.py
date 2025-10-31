from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'fatigometre-secret-key-2025'

# Mapping des niveaux de fatigue vers les produits
FATIGUE_PRODUCTS = {
    'enfant': {
        'name': 'Fatigue chez l\'enfant',
        'image': 'kidspng.png'
    },
    'legere': {
        'name': 'Fatigue légère',
        'image': 'mag.png'
    },
    'moderee': {
        'name': 'Fatigue modérée',
        'image': 'plus.png'
    },
    'intense': {
        'name': 'Fatigue intense',
        'image': 'pro.png'
    },
    'severe': {
        'name': 'Fatigue sévère',
        'image': 'boost.png'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fatigue-level', methods=['POST'])
def get_fatigue_level():
    """Endpoint pour récupérer le produit selon le niveau de fatigue"""
    data = request.json
    level = data.get('level')
    
    if level in FATIGUE_PRODUCTS:
        return jsonify({
            'success': True,
            'product': FATIGUE_PRODUCTS[level]
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Niveau de fatigue invalide'
        }), 400

if __name__ == '__main__':
    # En production, utiliser un serveur WSGI comme Gunicorn
    # Pour le développement Docker, on garde le serveur Flask
    app.run(host='0.0.0.0', port=5000)

