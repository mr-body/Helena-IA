from flask import Flask, Blueprint, request, jsonify
from Class.Genai import GenerativeAI
import os

question_bp = Blueprint('question', __name__)


app = Flask(__name__)

generative_ia = GenerativeAI("AIzaSyD38o8MZEPYTOekcvlUGB3FimnG7_99hgs") 

@question_bp.route('/text', methods=['POST'])
def generate_response_chat():
    data = request.get_json()
    user_input = data['text']

    # Get the last message in the conversation history
    response = generative_ia.question(user_input)
    property(user_input)

    return jsonify({"response": response})

@question_bp.route('/codeFile', methods=['POST'])
def generate_response_file_code():
    text = request.form.get('text')
    file = request.files['file'] if 'file' in request.files else None
    
    if not file:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400

    if file.filename == '':
        return jsonify({'message': 'Nome do arquivo vazio'}), 400

    filename = file.filename
    print(filename)

    file.save(os.path.join(f"{app.static_folder}/upload/", filename))

    try:
        response = generative_ia.questionFileCode(text, os.path.join(f"{app.static_folder}/upload/{filename}"))
    except Exception as e:
        caminho = f"static/upload/{filename}"
        print(caminho)
        response = generative_ia.questionFileCode(text, caminho)

    return response

@question_bp.route('/pdfFile', methods=['POST'])
def generate_response_file_pdf():
    # Obter os dados do formulário enviado pelo frontend
    text = request.form.get('text')
    file = request.files['file'] if 'file' in request.files else None
    
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nome do arquivo vazio'}), 400

    text = request.form.get('text')

    filename = file.filename

    
    print(filename)
    file.save(os.path.join(f"{app.static_folder}/upload/", filename))

    try:
        # Get the last message in the conversation history
        response = generative_ia.questionFilePDF(text, os.path.join(f"{app.static_folder}/upload/{filename}"))
    except Exception as e:
        # Get the last message in the conversation history
        caminho = f"static/upload/{filename}"
        print(caminho)
        response = generative_ia.questionFilePDF(text, caminho)
    
    property(text)

    return response


@question_bp.route('/office/<type>', methods=['POST'])
def office_word(type):
    # Obter os dados do formulário enviado pelo frontend
    text = request.form.get('text')
    file = request.files['file'] if 'file' in request.files else None
    
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nome do arquivo vazio'}), 400

    text = request.form.get('text')

    filename = file.filename

    
    print(filename)
    file.save(os.path.join(f"{app.static_folder}/upload/", filename))

    try:
        # Get the last message in the conversation history
        response = generative_ia.questionFile(text, type, os.path.join(f"{app.static_folder}/upload/{filename}"))
    except Exception as e:
        # Get the last message in the conversation history
        caminho = f"static/upload/{filename}"
        print(caminho)
        response = generative_ia.questionFile(text, type, caminho)
    
    property(text)

    return response
