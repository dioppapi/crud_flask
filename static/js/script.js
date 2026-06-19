function confirmerSuppression(id) {
    if (confirm('⚠️ Voulez-vous vraiment supprimer ce produit ? Cette action est irréversible.')) {
        document.getElementById('form-supprimer-' + id).submit();
    }
}