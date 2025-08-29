# CardioIA - Sistema Inteligente de Cardiologia

## 🏥 Visão Geral do Projeto
O **CardioIA** é um projeto acadêmico da **Fase 1 – Batimentos de Dados** do curso de Inteligência Artificial da FIAP.  
O objetivo desta fase é construir uma base inicial de dados cardiológicos (numéricos, textuais e visuais) que servirá como fundamento para os módulos inteligentes que serão desenvolvidos nas próximas etapas do projeto.

---

## 🎯 Objetivo da Atividade
Coletar, organizar e justificar três tipos de dados fundamentais para projetos de IA aplicados à saúde:

1. **📊 Dados Numéricos (IoT)**  
2. **📝 Dados Textuais (NLP)**  
3. **🖼️ Dados Visuais (Visão Computacional)**  

Essas informações serão utilizadas em fases futuras para treinar modelos de Machine Learning, realizar análises comparativas e apoiar soluções inovadoras em cardiologia.

---

## 📋 Estrutura do Repositório

```
CardioIA/
├── README.md
├── datasets/
│   ├── numeric/
│   ├── textual/
│   └── visual/
├── docs/
└── assets/
```

---

## 📊 Parte 1 – Dados Numéricos (IoT)

### 📁 Arquivos de Dados
👉 [Dataset XLSX](datasets/numeric/heart_disease_processed.xlsx)

**Link público para acesso completo ao dataset:**  
👉 [Google Drive - Dados Numéricos](https://drive.google.com/drive/folders/1MVGRajXHamQ81FYPaeWpcSY2UmrDjWy7?usp=sharing)

### 📌 Origem dos Dados
Os dados foram obtidos do **UCI Machine Learning Repository**, especificamente do **Cleveland Heart Disease Database** (1988).  
- Tipo: Dados clínicos reais de pacientes  
- Fonte: Cleveland Clinic Foundation, EUA  
- Licença: Creative Commons Attribution 4.0 International  

### 🔬 Variáveis Relevantes
Algumas variáveis fundamentais para análise clínica e em IA:  
- **Idade** – fator de risco primário para doenças cardiovasculares  
- **Sexo** – importante na diferenciação de risco precoce em homens  
- **Pressão arterial em repouso** – indicador direto de saúde cardiovascular  
- **Colesterol sérico** – biomarcador crítico para risco cardíaco  
- **Frequência cardíaca máxima** – avalia capacidade funcional do coração  
- **Doença cardíaca (target)** – variável de classificação binária  

Essas variáveis são essenciais para construir modelos de predição e triagem inteligente em cardiologia.

---

## 📝 Parte 2 – Dados Textuais (NLP)

### 📁 Arquivos de Textos
- [Texto 1](datasets/textual/texto1.txt)  
- [Texto 2](datasets/textual/texto2.txt)  

**Link público para acesso completo aos textos:**  
👉 [Google Drive / OneDrive - Dados Textuais](INSERIR_LINK_AQUI)

### 📌 Aplicações em NLP
Os textos podem ser usados em:  
- **Análise de sentimentos**: percepção de pacientes em tratamentos  
- **Extração de sintomas**: identificação de termos clínicos relevantes  
- **Classificação de tópicos**: organização de informações médicas  

Essas análises apoiam diagnósticos e auxiliam políticas de saúde pública.

---

## 🖼️ Parte 3 – Dados Visuais (Visão Computacional)

### ✅ **Status: CONCLUÍDO**

### 📁 **Arquivos de Dados**

#### **🔗 Link para Dados Completos (Google Drive):**
**[🖼️ Dataset CardioIA - Dados Visuais (Angiografias)](https://drive.google.com/drive/folders/1jVCcJEcLKzIFXeW35t9XjeqihJ4S-i-i?usp=drive_link)**

*Acesso público às imagens de angiografia coronária (XCA) utilizadas nesta fase do projeto.*

### 🏥 **Origem dos Dados**

As imagens provêm de uma seleção do dataset **Annotated X-Ray Angiography (ARCADE)**, disponível publicamente na plataforma Kaggle, e foram organizadas para este projeto.

- **Fonte Original**: [Kaggle - Annotated X-Ray Angiography Dataset](https://www.kaggle.com/datasets/nikitamanaenkov/annotated-x-ray-angiography-dataset)
- **Tipo**: Imagens reais de angiografia coronária por raios-X (XCA).
- **Licença**: Domínio Público (CC0: Public Domain).

### 📈 **Características do Dataset**

- **Total de Imagens**: 100 imagens.
- **Resolução**: 512x512 pixels.
- **Estrutura**: O conjunto de dados foi organizado em duas categorias para tarefas de classificação:
    1. **normal**: 50 imagens de exames sem anomalias visíveis.
    2. **anormal**: 50 imagens de exames com diagnóstico de estenose.

### 🤖 **Aplicações em Visão Computacional (VC)**

Este dataset é ideal para treinar e avaliar um algoritmo de Visão Computacional para a classificação e diagnóstico automatizado em cardiologia.

#### **Casos de Uso para o CardioIA:**

1.  **Classificação de Exames (Normal vs. Anormal)**:
    - **Objetivo**: Desenvolver um modelo de **Rede Neural Convolucional (CNN)** para classificar as imagens de angiografia em duas categorias: 'normal' ou 'anormal' (presença de estenose).
    - **Impacto**: Criar um sistema de triagem automático que pode rapidamente identificar exames que necessitam de atenção de um especialista, otimizando o fluxo de trabalho e acelerando o diagnóstico.

2.  **Localização de Anomalias (Exploração Futura)**:
    - **Objetivo**: Utilizar técnicas como Mapas de Ativação de Classe (CAM) para visualizar quais áreas da imagem levaram o modelo a classificar um exame como 'anormal', oferecendo interpretabilidade ao diagnóstico da IA.

#### **Importância para o Projeto:**
A análise de imagens é um pilar da cardiologia moderna. Integrar um módulo de Visão Computacional ao **CardioIA** que possa diferenciar exames normais de anormais transforma a plataforma em uma solução de diagnóstico mais completa, combinando dados clínicos (numéricos), registros (textuais) e evidências visuais (imagens) para fornecer um suporte à decisão muito mais robusto e preciso para a equipe médica.

---

## 🔒 Governança de Dados e Ética
- **Transparência**: origem e documentação dos dados  
- **Privacidade**: dados anonimizados e sem identificação pessoal  
- **Viés**: atenção à representatividade clínica e demográfica  
- **Uso**: finalidade exclusivamente acadêmica e educacional  

---

## 👥 Equipe
- Parte 1 – Dados Numéricos: Gustavo Castro (RM560831) 
- Parte 2 – Dados Textuais: Luis Emidio (RM559976)  
- Parte 3 – Dados Visuais: [Nome do Responsável]  

---

## 📚 Referências
1. UCI Machine Learning Repository – Heart Disease Dataset: https://archive.ics.uci.edu/dataset/45/heart+disease  
2. Detrano, R. et al. (1989). *International application of a new probability algorithm for the diagnosis of coronary artery disease*. American Journal of Cardiology.  

---

## ✨ Mensagem Final
Esta fase inicial representa a construção das bases para um ecossistema de cardiologia inteligente.  
Mais do que coletar dados, buscamos garantir relevância clínica e impacto positivo na aplicação de IA para a saúde.
