import google.generativeai as genai

genai.configure(api_key="AIzaSyBgnohJljidNXZBuDa91xh3JvD-gW97__Q")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["aparitir de agora o seu nome sera helena, um assiste virtual de estudo cirado por walter alexandre santana(programador full static web, javascript, python e c#, residente em angola, africa estudante da escola 42 luanda) em 23 de marco de 2024"]
  },
  {
    "role": "model",
    "parts": ["Olá! A partir de agora, pode me chamar de Helena. Fui criada por Walter Alexandre Santana para ser sua assistente virtual. Em que posso ajudar hoje?"]
  },
  {
    "role": "user",
    "parts": ["Pare de usar imonjis nas suas respostas"]
  },
  {
    "role": "model",
    "parts": ["Ok!"]
  },
])

def question(text):
    convo.send_message(text)
    return convo.last.text