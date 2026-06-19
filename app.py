from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'cle_secrete_simple'

def get_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  
        database='gestion_produits'
    )

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produits (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            prix DECIMAL(10,2) NOT NULL,
            quantite INT NOT NULL,
            categorie VARCHAR(50)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

init_db()

@app.route('/')
def liste():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM produits ORDER BY id')
    produits = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('liste.html', produits=produits)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nom = request.form['nom']
        prix = float(request.form['prix'])
        quantite = int(request.form['quantite'])
        categorie = request.form.get('categorie', '')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produits (nom, prix, quantite, categorie) VALUES (%s, %s, %s, %s)',
                      (nom, prix, quantite, categorie))
        conn.commit()
        cursor.close()
        conn.close()
        flash('✅ Produit ajouté avec succès', 'success')
        return redirect(url_for('liste'))
    
    return render_template('ajouter.html')

@app.route('/modifier/<int:id_produit>', methods=['GET', 'POST'])
def modifier(id_produit):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        nom = request.form['nom']
        prix = float(request.form['prix'])
        quantite = int(request.form['quantite'])
        categorie = request.form.get('categorie', '')
        
        cursor.execute('UPDATE produits SET nom=%s, prix=%s, quantite=%s, categorie=%s WHERE id=%s',
                      (nom, prix, quantite, categorie, id_produit))
        conn.commit()
        cursor.close()
        conn.close()
        flash('✅ Produit modifié avec succès', 'success')
        return redirect(url_for('liste'))
    
    cursor.execute('SELECT * FROM produits WHERE id=%s', (id_produit,))
    produit = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('modifier.html', produit=produit)

@app.route('/supprimer/<int:id_produit>', methods=['POST'])
def supprimer(id_produit):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produits WHERE id=%s', (id_produit,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('🗑️ Produit supprimé avec succès', 'success')
    return redirect(url_for('liste'))

if __name__ == '__main__':
    app.run(debug=True)