from flask import Flask, render_template
import json

app = Flask(__name__)

# Carregar dados do JSON
with open('user-data.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", data=data)

'''
TESTE FUTURO

@app.route("/download_vcard")
def download_vcard():
    # Obter informações do perfil
    perfil = data["perfil"] # Obtém o objeto "perfil" e suas propriedades chave-valor
    nome = perfil["nome"]
    sobrenome = perfil["sobrenome"]
    contato = perfil["contato"]

    # Criar conteúdo do vCard
    vcard_content = f"""BEGIN:VCARD
VERSION: 3.0
FN: {nome} {sobrenome}
TEL;TYPE=CELL: {contato}
END:VCARD
"""

    # Salvar o vCard em um arquivo temporário
    vcard_filename = "contato.vcf"
    with open(vcard_filename, "w") as vcard_file:
        vcard_file.write(vcard_content)

    # Enviar o arquivo vCard para download
    return send_file(vcard_filename, as_attachment=True)
'''

if __name__ == "__main__":
    app.run(debug=True)
