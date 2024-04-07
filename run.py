from app import app, db

# Membuat struktur tabel database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
