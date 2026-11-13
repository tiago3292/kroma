from gradio_client import Client

# Conecta ao Space oficial gratuito do FLUX.1-schnell
client = Client("black-forest-labs/FLUX.1-schnell")

result = client.predict(
    prompt="A smiley face giving a thumbs up",
    seed=0,
    randomize_seed=True,
    width=500,
    height=500,
    num_inference_steps=4,
    api_name="/infer"
)

# O retorno é uma tupla onde o primeiro item é o caminho local da imagem baixada
caminho_imagem = result[0]
print(f"Imagem salva em: {caminho_imagem}")