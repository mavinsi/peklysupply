import os
import requests

# Criar a pasta "imagens" se não existir
os.makedirs("imagens", exist_ok=True)

# URL base das imagens
base_url = "https://rpsupply.com.br/wp-content/uploads/2024/02/"

# Loop para baixar imagens de 1.png até 43.png
for i in range(1, 44):
    url = f"{base_url}{i}.png"
    caminho_arquivo = os.path.join("imagens", f"{i}.png")

    print(f"Baixando {url}...")

    try:
        resposta = requests.get(url, stream=True, timeout=10)
        resposta.raise_for_status()  # Verifica se ocorreu erro na requisição

        with open(caminho_arquivo, "wb") as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)

        print(f"✅ {i}.png salvo com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao baixar {i}.png: {e}")

print("✅ Download concluído!")
import os
import requests

# Criar a pasta "imagens" se não existir
os.makedirs("imagens", exist_ok=True)

# URL base das imagens
base_url = "https://rpsupply.com.br/wp-content/uploads/2024/02/"

# Loop para baixar imagens de 1.png até 43.png
for i in range(1, 44):
    url = f"{base_url}{i}.png"
    caminho_arquivo = os.path.join("imagens", f"{i}.png")

    print(f"Baixando {url}...")

    try:
        resposta = requests.get(url, stream=True, timeout=10)
        resposta.raise_for_status()  # Verifica se ocorreu erro na requisição

        with open(caminho_arquivo, "wb") as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)

        print(f"✅ {i}.png salvo com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao baixar {i}.png: {e}")

print("✅ Download concluído!")
