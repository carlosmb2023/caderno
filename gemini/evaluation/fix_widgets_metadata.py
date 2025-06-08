import os
import nbformat

def fix_widgets_metadata(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
    changed = False
    metadata = nb.get('metadata', {})
    widgets = metadata.get('widgets', None)
    if widgets is not None:
        # Se não tem a chave 'state', adiciona um dicionário vazio
        if 'state' not in widgets:
            widgets['state'] = {}
            print(f"[Dr. Decifra] Corrigindo 'metadata.widgets' em: {nb_path}")
            changed = True
    if changed:
        with open(nb_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
    return changed

if __name__ == "__main__":
    # Corrige todos os .ipynb em gemini/evaluation/
    folder = os.path.dirname(__file__)
    for fname in os.listdir(folder):
        if fname.endswith('.ipynb'):
            fix_widgets_metadata(os.path.join(folder, fname))
    print("Dr. Decifra aqui! Descomplicando a IA com ciência, bom humor e os códigos certos!")
