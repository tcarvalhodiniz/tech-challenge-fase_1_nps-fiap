# Tech Challenge - Fase 1: Case NPS
> **Pós-Graduação em AI Scientist - FIAP**

## Visão Geral
Este projeto faz parte do Tech Challenge da Fase 1 e tem como objetivo transformar dados operacionais em insights estratégicos. O foco principal é entender os impactos ea d satisfação do cliente (NPS) e propor soluções baseadas em dados para melhorar a experiência do consumidor.

## Entendimento do Negócio
Hoje, o NPS é coletado apenas **após o encerramento da jornada de compra**. Quando a 
pesquisa chega, a experiência ruim já aconteceu — e a empresa fica reativa.

## Principais Achados

A análise exploratória de 2.500 pedidos revelou:

- **NPS consolidado: -80** (84% detratores, apenas 4,4% promotores)
- **Atraso na entrega** é o fator mais crítico (correlação -0,60 com NPS)
- O **tempo total de entrega** praticamente não influencia o NPS — o que importa é o 
  cumprimento da promessa
- **Reclamações e contatos com SAC** amplificam a insatisfação, mesmo quando 
  resolvidos
- O **perfil do cliente** (idade, região, tempo de relacionamento) **não explica** as 
  variações no NPS — o problema é estrutural na operação


## Base de Dados

Arquivo: `data/raw/desafio_nps_fase_1.csv`  
**2.500 pedidos** com 19 variáveis cobrindo:

- Dados do cliente (idade, região, tempo de relacionamento)
- Dados do pedido (valor, itens, parcelamento, desconto)
- Dados logísticos (tempo de entrega, atraso, tentativas, frete)
- Dados de atendimento (contatos, tempo de resolução, reclamações)
- Indicadores internos (CSAT, recompra em 30 dias, NPS)

---

## 🛠️ Estrutura do Projeto

tech-challenge/
├── data/
│   ├── raw/                                  # Dados originais (CSV)
│   └── processed/                            # Dados processados (não foi necessário fazer tratamento)
├── notebooks/
│   ├── 01_Analises_Case.ipynb                # Entendimento do negócio e target
├── reports/
│   ├── Diagnostico_NPS_Apresentacao.pptx     # Apresentação executiva
│   └── video_link.md                         # Apresentação executiva
├── src/
│   ├── data_cleaning.py                      # Funções de limpeza
│   └── visualization.py                      # Funções de visualização
├── .gitignore
├── README.md
└── requirements.txt


## Como Executar o Projeto

## Como Reproduzir

### 1. Clone o repositório
```bash
git clone https://github.com/tcarvalhodiniz/tech-challenge.git
cd tech-challenge
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o notebook
1. `01_Analises_Case.ipynb` — entendimento do problema e definição da target

---

## 📐 Metodologia

O projeto segue o framework **CRISP-DM** (Cross-Industry Standard Process for Data Mining):

1. **Business Understanding** — definição do problema, target e impactos no negócio
2. **Data Understanding** — exploração inicial e checagem de qualidade
3. **Data Preparation** — limpeza e categorização (Detrator/Neutro/Promotor)
4. **Modeling** — análise de correlação e identificação de drivers
5. **Evaluation** — Insights e recomendações
6. **Deployment** — apresentação executiva 

---

## 🎬 Material Complementar

- **Apresentação executiva:** [`reports/Diagnostico_NPS_Apresentacao.pptx`](reports/Diagnostico_NPS_Apresentacao.pptx)
- **Vídeo executivo (5 min):** [Link do Loom](https://www.loom.com/share/d27b72a108864c549029aef2f5a3a2bf)

---

## ⚠️ Limitações da Análise

- A base **não contém datas** — não permite análise temporal ou sazonalidade
- **Correlação não é causalidade** — o atraso pode estar correlacionado a causas 
  ocultas (transportadora, categoria de produto)
- **Falta dado qualitativo** — não temos o texto das reclamações, apenas a contagem
- **Viés de resposta** — quem responde NPS tende a estar nos extremos (muito 
  satisfeito ou muito insatisfeito)

---

## 👤 Autor

**Thiago Corrêa Carvalho Diniz** — RM [371212]  
Pós-Graduação AI Data Science — FIAP