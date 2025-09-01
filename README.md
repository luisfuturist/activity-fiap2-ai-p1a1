# CardioIA - Sistema Inteligente de Cardiologia <!-- omit in toc -->

> Este projeto faz parte do curso de **Inteligência Artificial** da [FIAP](https://github.com/fiap) - Online 2024. Este repositório é a atividade "**Ano 2 - Fase 1** - Batimentos de Dados".

## Índice <!-- omit in toc -->

- [Visão Geral do Projeto](#visão-geral-do-projeto)
- [Objetivos do Projeto](#-objetivos-do-projeto)
  - [**Objetivo Geral:**](#objetivo-geral)
  - [**Objetivos Específicos:**](#objetivos-específicos)
  - [**Resultados Esperados:**](#resultados-esperados)
- [Parte 1 - Dados Numéricos (IoT)](#-parte-1---dados-numéricos-iot)
  - [Arquivos de Dados](#-arquivos-de-dados)
  - [Origem dos Dados](#-origem-dos-dados)
  - [Variáveis Relevantes](#-variáveis-relevantes)
- [Parte 2 - Dados Textuais (NLP)](#-parte-2---dados-textuais-nlp)
  - [**Arquivos de Dados**](#-arquivos-de-dados-1)
    - [**Arquivos Coletados:**](#-arquivos-coletados)
  - [**Origem dos Dados**](#-origem-dos-dados-1)
  - [**Como os textos podem ser analisados por NLP**](#-como-os-textos-podem-ser-analisados-por-nlp)
  - [**Justificativa: Por que essas análises são relevantes para IA em Saúde?**](#-justificativa-por-que-essas-análises-são-relevantes-para-ia-em-saúde)
- [Parte 3 - Dados Visuais (VC)](#-parte-3---dados-visuais-vc)
  - [**Arquivos de Dados**](#-arquivos-de-dados-2)
    - [**Link para Dados Completos (Google Drive):**](#-link-para-dados-completos-google-drive)
  - [**Origem dos Dados**](#-origem-dos-dados-2)
  - [**Características do Dataset**](#-características-do-dataset)
  - [**Aplicações em Visão Computacional (VC)**](#-aplicações-em-visão-computacional-vc)
    - [**Casos de Uso para o CardioIA:**](#casos-de-uso-para-o-cardioia)
    - [**Importância para o Projeto:**](#importância-para-o-projeto)
- [Equipe](#equipe)
  - [Membros](#membros)
  - [Professores](#professores)


## Visão Geral do Projeto

O **CardioIA** é um projeto acadêmico inovador do curso de Inteligência Artificial da FIAP, desenvolvido como parte da **Fase 1 – Batimentos de Dados**. Este projeto simula o ecossistema de uma cardiologia moderna, integrando diferentes modalidades de dados para criar uma base sólida que alimentará futuros módulos inteligentes de IA aplicados à saúde cardiovascular.

Como cientistas de dados hospitalares, nossa missão nesta fase é levantar, organizar e compreender dados cardiológicos que serão fundamentais para o desenvolvimento de algoritmos de machine learning, visão computacional e processamento de linguagem natural. O projeto é construído com foco na **Governança de Dados** e na mitigação de viés em sistemas inteligentes, preparando o terreno para as próximas fases que incluirão modelos de ML, agentes inteligentes e soluções de diagnóstico assistido.

## Objetivos do Projeto

### **Objetivo Geral:**
Construir uma base sólida de dados cardiológicos em três modalidades essenciais para projetos de IA em saúde, demonstrando competência na coleta, organização e preparação de dados clínicos.

### **Objetivos Específicos:**

1. **Dados Numéricos (IoT)**: 
   - Coletar e organizar dataset clínico com variáveis cardiológicas relevantes
   - Demonstrar compreensão da origem e qualidade dos dados médicos
   - Identificar variáveis clinicamente significativas para algoritmos de IA

2. **Dados Textuais (NLP)**: 
   - Reunir literatura médica e textos científicos sobre saúde cardiovascular
   - Explicar como técnicas de NLP podem extrair conhecimento desses textos
   - Justificar a relevância da análise textual para projetos de IA em saúde

3. **Dados Visuais (VC)**: 
   - Coletar imagens de exames cardiológicos para análise computacional
   - Demonstrar compreensão das aplicações de visão computacional em cardiologia
   - Preparar base visual para treinamento de modelos de classificação médica

### **Resultados Esperados:**
Esses dados serão utilizados nas fases seguintes para:
- Treinar modelos de machine learning para diagnóstico assistido
- Desenvolver algoritmos de visão computacional para análise de exames
- Implementar sistemas de processamento de linguagem natural para prontuários
- Criar soluções inovadoras de triagem e monitoramento cardiológico
- Estabelecer base para ecossistema de cardiologia inteligente

---

## Parte 1 - Dados Numéricos (IoT)

### Arquivos de Dados
[Dataset XLSX](datasets/numeric/heart_disease_processed.xlsx)

**Link público para acesso completo ao dataset:**  
[Google Drive - Dados Numéricos](https://drive.google.com/drive/folders/1MVGRajXHamQ81FYPaeWpcSY2UmrDjWy7?usp=sharing)

### Origem dos Dados
Os dados foram obtidos do **UCI Machine Learning Repository**, especificamente do **Cleveland Heart Disease Database** (1988).  
- Tipo: Dados clínicos reais de pacientes  
- Fonte: Cleveland Clinic Foundation, EUA  
- Licença: Creative Commons Attribution 4.0 International  

### Variáveis Relevantes
Algumas variáveis fundamentais para análise clínica e em IA:  
- **Idade** – fator de risco primário para doenças cardiovasculares  
- **Sexo** – importante na diferenciação de risco precoce em homens  
- **Pressão arterial em repouso** – indicador direto de saúde cardiovascular  
- **Colesterol sérico** – biomarcador crítico para risco cardíaco  
- **Frequência cardíaca máxima** – avalia capacidade funcional do coração  
- **Doença cardíaca (target)** – variável de classificação binária  

Essas variáveis são essenciais para construir modelos de predição e triagem inteligente em cardiologia.

## Parte 2 - Dados Textuais (NLP)

### **Arquivos de Dados**

#### **Arquivos Coletados:**

1. **FhdvV9qsmPbL4KFfMqwtNBv_extracted.txt** (13KB, 258 linhas)
   - **Título**: "Coronavírus e o Coração | Um Relato de Caso sobre a Evolução da COVID-19 Associado à Evolução Cardiológica"
   - **Fonte**: Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol)
   - **Conteúdo**: Relato de caso de paciente diabético com COVID-19 que evoluiu com complicações cardíacas
   - **Relevância**: Demonstra a interação entre doenças infecciosas e cardiovasculares

2. **K9Ns38vDyW3qXDkJSQj56Jk_extracted.txt** (25KB, 418 linhas)
   - **Título**: "Relato de Caso de Doença Coronariana e Vascular Não Aterosclerótica: Em Busca de uma Entidade Clínica Rara"
   - **Fonte**: Arquivos Brasileiros de Cardiologia (Arq Bras Cardiol)
   - **Conteúdo**: Caso de doença relacionada à imunoglobulina G4 (IgG4-RD) com manifestação cardiovascular rara
   - **Relevância**: Apresenta diagnóstico complexo de condição sistêmica rara com envolvimento cardíaco

> [!NOTE]
> O download dos textos foi realizado utilizando o script [nlp_data_download.py](scripts/nlp_data_download.py). Para mais informações sobre o download dos textos, [leia aqui](lib/pdfurl2text/README.md).

### **Origem dos Dados**

Os textos foram coletados de fontes científicas de alta qualidade:

- **SciELO (Scientific Electronic Library Online)**: Biblioteca digital de acesso aberto
- **Arquivos Brasileiros de Cardiologia**: Revista científica da Sociedade Brasileira de Cardiologia
- **Licença**: Acesso aberto para fins educacionais e de pesquisa
- **Qualidade**: Artigos revisados por pares e publicados em revista indexada

### **Como os textos podem ser analisados por NLP**

Os textos coletados podem ser analisados por técnicas de Processamento de Linguagem Natural (NLP) de diversas formas, tornando possível extrair informações valiosas automaticamente. Veja alguns exemplos práticos:

- **Identificação de sintomas e diagnósticos:** O algoritmo pode "ler" o texto e encontrar menções a sintomas (como dor no peito, febre, falta de ar) e diagnósticos médicos, destacando essas informações de forma estruturada.
- **Classificação do conteúdo:** É possível separar os textos por temas, como tipo de doença, gravidade do caso ou especialidade médica, facilitando a organização e busca por casos semelhantes.
- **Análise de sentimentos e tom clínico:** O NLP pode avaliar se o relato descreve um caso grave, urgente ou estável, ajudando a priorizar atendimentos ou identificar situações críticas rapidamente.
- **Extração de dados para tabelas:** Informações como idade, sexo, exames realizados e resultados podem ser extraídas automaticamente dos textos e organizadas em tabelas para análise posterior.
- **Resumo automático:** Algoritmos podem gerar resumos dos textos, facilitando a leitura rápida por profissionais de saúde.

Essas análises permitem transformar textos médicos longos e complexos em dados estruturados, prontos para serem usados em sistemas de apoio à decisão, pesquisas ou automação de processos clínicos.

### **Justificativa: Por que essas análises são relevantes para IA em Saúde?**

A aplicação de técnicas de NLP (Processamento de Linguagem Natural) em textos médicos é fundamental para projetos de Inteligência Artificial na área da saúde, pois:

- **Automatiza a triagem de casos:** Algoritmos podem identificar rapidamente relatos críticos ou urgentes, priorizando o atendimento de pacientes de maior risco.
- **Apoia o diagnóstico clínico:** A extração automática de sintomas, sinais e diagnósticos auxilia médicos na tomada de decisão, reduzindo erros e acelerando o processo.
- **Organiza e estrutura prontuários:** A classificação e extração de informações transforma textos não estruturados em dados organizados, facilitando buscas e análises posteriores.
- **Identifica padrões clínicos e epidemiológicos:** O agrupamento e análise de grandes volumes de textos permite detectar tendências, fatores de risco e novas associações clínicas.
- **Acelera pesquisas e descobertas:** O processamento automatizado de literatura médica e relatos de casos amplia a capacidade de revisão e atualização científica.
- **Melhora a qualidade dos dados:** A padronização e extração de informações relevantes contribuem para bases de dados mais completas e confiáveis.

Em resumo, essas análises potencializam a eficiência, a precisão e a inovação em projetos de IA aplicados à saúde, promovendo melhores resultados clínicos e avanços científicos.

## Parte 3 - Dados Visuais (VC)

### **Arquivos de Dados**

#### **Link para Dados Completos (Google Drive):**
**[Dataset CardioIA - Dados Visuais (Angiografias)](https://drive.google.com/drive/folders/1jVCcJEcLKzIFXeW35t9XjeqihJ4S-i-i?usp=drive_link)**

*Acesso público às imagens de angiografia coronária (XCA) utilizadas nesta fase do projeto.*

### **Origem dos Dados**

As imagens provêm de uma seleção do dataset **Annotated X-Ray Angiography (ARCADE)**, disponível publicamente na plataforma Kaggle, e foram organizadas para este projeto.

- **Fonte Original**: [Kaggle - Annotated X-Ray Angiography Dataset](https://www.kaggle.com/datasets/nikitamanaenkov/annotated-x-ray-angiography-dataset)
- **Tipo**: Imagens reais de angiografia coronária por raios-X (XCA).
- **Licença**: Domínio Público (CC0: Public Domain).

### **Características do Dataset**

- **Total de Imagens**: 100 imagens.
- **Resolução**: 512x512 pixels.
- **Estrutura**: O conjunto de dados foi organizado em duas categorias para tarefas de classificação:
  - **normal**: 50 imagens de exames sem anomalias visíveis.
  - **anormal**: 50 imagens de exames com diagnóstico de estenose.

### **Aplicações em Visão Computacional (VC)**

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

## Equipe

### Membros

- Gustavo Castro (RM560831)
- Luis Emidio (RM559976)
- Matheus Conciani (RM559473) 

### Professores

- **Tutor**: [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona/)  
- **Coordenador**: [André Godoi](https://www.linkedin.com/in/profandregodoi/)  

---

[LICENSE.md](LICENSE.md)
