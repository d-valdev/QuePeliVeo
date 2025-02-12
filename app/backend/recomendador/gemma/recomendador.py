from huggingface_hub import InferenceClient

client = InferenceClient(api_key="ENTER_YOUR_API_KEY")

def formular(prompt, numero):

	print("ENTRO1")
	respuesta =""

	messages = [

		{
			"role": "user",
			"content": f"Solo vas a responder titulos de peliculas en inglés. Nada más que titulos. Cada título entre comillas dobles. En formato CSV. Nada mas que la linea CSV. Solo la linea con titulos en CSV. Asegurate que respondes {numero} titulos. Que cumplan estas características: {prompt} "
		}
	]

	stream = client.chat.completions.create(
		model="google/gemma-2-2b-it", 
		messages=messages, 
		max_tokens=500,
		stream=True
	)


	for chunk in stream:
		respuesta += chunk.choices[0].delta.content
		
	print(respuesta)

	return respuesta
