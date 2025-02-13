from huggingface_hub import InferenceClient

client = InferenceClient(api_key="ENTER_YOUR_API_KEY")

def formular(prompt, numero):

	respuesta =""

	messages = [

		{
			"role": "user",
			"content": f"Aquí introducirías el {prompt} y el {numero}. Pero te dejo pensar cual crees que puse! jeje. "
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
		

	return respuesta
