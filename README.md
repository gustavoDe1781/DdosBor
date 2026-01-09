# DDOS BOR!
_⚠️ AVISO LEGAL IMPORTANTE: Este projeto é desenvolvido APENAS para fins educacionais e de teste em ambientes controlados. O uso não autorizado contra sistemas sem permissão explícita é ILEGAL e pode resultar em consequências jurídicas graves. O desenvolvedor não se responsabiliza por qualquer uso indevido desta ferramenta._

---

📋 Descrição

Ferramenta de teste de estresse (DDoS) para análise de segurança em ambientes autorizados.

🚀 Instalação

Pré-requisitos Gerais

```bash
pip install requests urllib3
```

📱 Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/gustavoDe1781/DdosBor.git
cd DdosBor
python ddos.py
```

🪟 Windows

```bash
# Instalar Python (se necessário)
# Baixar de: https://python.org

# Instalar dependências
pip install requests urllib3

# Clonar repositório
git clone https://github.com/gustavoDe1781/DdosBor.git
cd DdosBor

# Executar
python ddos.py
```

🐧 Kali Linux / Distribuições Linux

```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python e pip
sudo apt install python3 python3-pip git -y

# Clonar repositório
git clone https://github.com/gustavoDe1781/DdosBor.git
cd DdosBor

# Instalar dependências
pip3 install requests urllib3

# Tornar executável
chmod +x ddos.py

# Executar (sem sudo normalmente)
python3 ddos.py
# ou
python ddos.py
```

🔧 Solução de Problemas

Se não tiver Python instalado:

```bash
# Linux/Debian
sudo apt install python3

# Termux
pkg install python

# Verificar instalação
python --version
python3 --version
```

Problemas de permissão (Kali Linux):

```bash
# Instalar dependências com sudo se necessário
sudo pip3 install requests urllib3
```

📝 Como Usar

1. Certifique-se de ter permissão explícita para testar o alvo
2. Execute o script:
   ```bash
   python ddos.py
   ```
3. Siga as instruções apresentadas no terminal

⚠️ Responsabilidade Ética

· Use apenas em sistemas que você possui
· Obtenha autorização por escrito antes de testar
· Configure ambientes de laboratório controlados
· Relate vulnerabilidades encontradas de forma responsável
