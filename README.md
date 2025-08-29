# CardioIA - Sistema Inteligente de Cardiologia

## 🏥 Visão Geral do Projeto

O **CardioIA** é um projeto de sistema inteligente voltado para a área de cardiologia, desenvolvido como parte da **Fase 1 – Batimentos de Dados**. O objetivo é construir um ecossistema de dados que alimentará módulos inteligentes de Inteligência Artificial aplicados à saúde cardiovascular.

Este projeto simula um ambiente hospitalar onde diferentes tipos de dados cardiológicos são coletados, organizados e preparados para análises avançadas de IA, sempre considerando os princípios de **Governança de Dados** e mitigação de viés em sistemas inteligentes.

## 🎯 Objetivos do Projeto

Desenvolver uma base sólida de dados cardiológicos em três modalidades:

1. **📊 Dados Numéricos (IoT)**: Variáveis clínicas de pacientes cardíacos
2. **📝 Dados Textuais (NLP)**: Textos médicos e literatura sobre saúde cardiovascular  
3. **🖼️ Dados Visuais (VC)**: Imagens de exames cardiológicos

Esses dados serão utilizados nas fases seguintes para:
- Treinar modelos de machine learning
- Desenvolver algoritmos de diagnóstico assistido
- Realizar análises comparativas e preditivas
- Gerar soluções inovadoras para cardiologia

## 📋 Estrutura do Projeto

```
CardioIA/
├── README.md
├── datasets/
│   ├── numeric/
│   │   ├── heart_disease_processed.csv
│   │   └── dataset_doencas_cardiacas.xlsx
│   └── visual/
│       └── [A ser desenvolvido pelos integrantes]
└── assets/
    └── textual/
        └── [Documentação adicional]
```

---

## 📊 Parte 1 - Dados Numéricos (IoT)

### ✅ **Status: CONCLUÍDO**

### 📁 **Arquivos de Dados**

#### **🔗 Link para Dados Completos (Google Drive):**
**[📊 Dataset CardioIA - Dados Numéricos](https://drive.google.com/drive/folders/1MVGRajXHamQ81FYPaeWpcSY2UmrDjWy7?usp=drive_link)**

*Acesso público aos arquivos completos do projeto, incluindo datasets, planilhas, relatórios e visualizações.*
- **Dataset Principal**: [heart_disease_processed.csv](datasets/numeric/heart_disease_processed.csv)
- **Planilha Excel**: [dataset_doencas_cardiacas.xlsx](datasets/numeric/dataset_doencas_cardiacas.xlsx)
- **Relatório Completo**: [relatorio_dataset_cardiaco.md](docs/relatorio_dataset_cardiaco.md)

### 🏥 **Origem dos Dados**

Os dados são **100% reais** e provêm do renomado **UCI Machine Learning Repository**, especificamente do **Cleveland Heart Disease Database**:

- **Fonte**: Cleveland Clinic Foundation, Cleveland, Ohio, EUA
- **Período**: 1988
- **Tipo**: Dados clínicos reais de pacientes
- **Validação**: Mais de 64 citações acadêmicas e 847.000 visualizações
- **Licença**: Creative Commons Attribution 4.0 International
- **DOI**: 10.24432/C52P4X

### ⚠️ **Considerações Importantes sobre a Idade dos Dados**

**Limitação Temporal (1988):**
- **Contexto Médico**: A cardiologia evoluiu significativamente desde 1988
- **Novos Tratamentos**: Estatinas, stents, procedimentos minimamente invasivos
- **Tecnologia Diagnóstica**: Equipamentos mais precisos e novos biomarcadores
- **Demografia**: Mudanças nos padrões populacionais e fatores de risco

**Por que ainda é Relevante:**
- **Fisiologia Humana**: Os fundamentos cardiovasculares permanecem os mesmos
- **Variáveis Core**: Idade, sexo, pressão arterial, colesterol continuam sendo fatores de risco primários
- **Padrões Básicos**: Relações entre sintomas e diagnóstico mantêm validade
- **Benchmark Acadêmico**: Amplamente usado para comparação de algoritmos

**Estratégias de Mitigação:**
1. **Validação Cruzada**: Testar modelos em datasets mais recentes quando disponíveis
2. **Transfer Learning**: Usar como base para fine-tuning com dados modernos
3. **Análise Comparativa**: Comparar com estudos epidemiológicos atuais
4. **Disclaimer Clínico**: Sempre indicar limitações temporais em aplicações práticas

### 📈 **Características do Dataset**

- **Total de Pacientes**: 297 registros
- **Variáveis**: 14 características clínicas
- **Qualidade**: Apenas 2% de valores ausentes
- **Balanceamento**: 46% com doença cardíaca, 54% sem doença
- **Faixa Etária**: 29-77 anos (média: 54.5 anos)
- **Distribuição por Sexo**: 67.7% masculino, 32.3% feminino

### 🔬 **Variáveis Clínicas e Relevância para IA**

#### **Variáveis Demográficas**
| Variável | Tipo | Relevância para IA |
|----------|------|-------------------|
| **idade** | Numérica | Forte preditor não-linear de risco cardiovascular |
| **sexo** | Categórica | Alto poder discriminativo (homens têm maior risco prematuro) |

#### **Variáveis de Sintomas**
| Variável | Tipo | Relevância para IA |
|----------|------|-------------------|
| **tipo_dor_peito** | Categórica | Feature ordinal com alta correlação diagnóstica |
| **angina_exercicio** | Binária | Indicador direto de isquemia miocárdica |

#### **Variáveis Fisiológicas**
| Variável | Tipo | Relevância para IA |
|----------|------|-------------------|
| **pressao_arterial_repouso** | Numérica | Relação não-linear com risco cardiovascular |
| **colesterol** | Numérica | Biomarcador quantitativo essencial |
| **freq_cardiaca_max** | Numérica | Indicador de capacidade cardiovascular |
| **glicemia_jejum** | Binária | Fator de risco metabólico |

#### **Variáveis de Exames Especializados**
| Variável | Tipo | Relevância para IA |
|----------|------|-------------------|
| **ecg_repouso** | Categórica | Detecta anormalidades elétricas cardíacas |
| **depressao_st** | Numérica | Altamente específica para isquemia |
| **inclinacao_st** | Ordinal | Complementa depressão ST com info morfológica |
| **vasos_principais** | Ordinal | Quantifica extensão da doença |
| **talassemia** | Categórica | Teste de perfusão miocárdica especializado |

#### **Variável Target**
| Variável | Tipo | Relevância para IA |
|----------|------|-------------------|
| **doenca_cardiaca** | Binária | Target para classificação supervisionada |

### 🤖 **Aplicações em IA**

#### **Algoritmos Recomendados:**
- **Random Forest**: Ideal para features mistas (categóricas + numéricas)
- **Gradient Boosting**: Excelente para padrões não-lineares complexos
- **SVM**: Eficaz para classificação binária com features normalizadas
- **Neural Networks**: Captura interações complexas entre variáveis
- **Logistic Regression**: Interpretável para validação clínica

#### **Casos de Uso:**
1. **Diagnóstico Assistido**: Predição de risco de doença cardíaca
2. **Triagem Inteligente**: Priorização de pacientes por risco
3. **Medicina Preventiva**: Identificação de fatores de risco modificáveis
4. **Análise Epidemiológica**: Padrões populacionais de doenças cardíacas

### 📊 **Qualidade e Limitações dos Dados**

#### **Pontos Fortes:**
- ✅ **Dados Reais**: Coletados em ambiente clínico real
- ✅ **Padrão-Ouro**: Diagnóstico baseado em angiografia
- ✅ **Completude**: Apenas 2% de valores ausentes
- ✅ **Balanceamento**: 46% positivos, 54% negativos
- ✅ **Diversidade**: Ampla faixa etária e ambos os sexos
- ✅ **Validação Acadêmica**: Amplamente utilizado na literatura científica

#### **Limitações Importantes:**
- ⚠️ **Idade dos Dados**: Coletados em 1988 (37 anos atrás)
- ⚠️ **Evolução Médica**: Medicina cardiovascular evoluiu significativamente
- ⚠️ **População Específica**: Principalmente caucasiana (Cleveland, EUA)
- ⚠️ **Tamanho Limitado**: 297 registros (adequado para proof-of-concept)
- ⚠️ **Contexto Tecnológico**: Equipamentos e protocolos diagnósticos desatualizados

#### **Impacto das Limitações Temporais:**
1. **Tratamentos**: Estatinas, stents e terapias modernas não existiam
2. **Diagnóstico**: Tecnologia de imagem e biomarcadores mais limitados
3. **Demografia**: Padrões populacionais de risco podem ter mudado
4. **Estilo de Vida**: Fatores como sedentarismo e dieta evoluíram

#### **Recomendações para Uso:**
- 🎯 **Fins Educacionais**: Excelente para aprender conceitos de ML em saúde
- 🎯 **Prototipagem**: Ideal para desenvolver e testar algoritmos
- 🎯 **Benchmark**: Comparação com outros métodos de ML
- ⚠️ **Aplicação Clínica**: Requer validação com dados contemporâneos

#### **Alternativas de Datasets Mais Recentes:**
Para projetos que exigem dados mais atuais, considere:
- **Framingham Heart Study**: Dados longitudinais mais recentes
- **MIMIC-III/IV**: Dados hospitalares modernos (requer autorização)
- **UK Biobank**: Grande coorte populacional contemporânea
- **Kaggle Heart Disease**: Compilações de datasets mais recentes
- **Dados Sintéticos**: Geração de dados baseada em distribuições modernas

---

## 📝 Parte 2 - Dados Textuais (NLP)

### 📚 **Pesquisa de Dados NLP Cardíacos**

A pesquisa realizada sobre dados NLP cardíacos está disponível em 3 formatos:

- [PDF](research/Pesquisa_de_Dados_NLP_Cardiacos.pdf)
- [Markdown](research/Pesquisa_de_Dados_NLP_Cardiacos.md)
- [Google Docs](https://docs.google.com/document/d/1VWUvAUArbplo_Hc-aQJ_L6XYFMTIYwAIe_UNLfuX28Y)

### 📁 **Arquivos de Dados Textuais**

#### 📚 **Textos Coletados do Projeto Gutenberg:**

**1. St. Bernard's: The Romance of a Medical Student**
- **Arquivo**: [St_Bernard_s_TheRomance_of_a_Medical_Student_by_Edward_Berdoe.txt](assets/textual/St_Bernard_s_TheRomance_of_a_Medical_Student_by_Edward_Berdoe.txt)
- **Autor**: Edward Berdoe (sob pseudônimo Æsculapius Scalpel)
- **Ano**: 1888 (4ª edição)
- **Idioma**: Inglês
- **Tamanho**: 542KB (9.627 linhas)
- **Gênero**: Romance médico histórico
- **Relevância**: Narrativa sobre a vida de estudantes de medicina, oferecendo perspectiva histórica e humana sobre a prática médica

**2. O Oraculo do Passado, do Presente e do Futuro (Parte 3)**
- **Arquivo**: [O_Oraculo_do_Passado_do_presente_e_do_Futuro](assets/textual/O_Oraculo_do_Passado_do_presente_e_do_Futuro)
- **Autor**: Bento Serrano
- **Ano**: 1883
- **Idioma**: Português
- **Tamanho**: 104KB (2.736 linhas)
- **Gênero**: Tratado médico-astrológico
- **Relevância**: Contém "segredos úteis para a cura radical de muitas moléstias conhecidas e desconhecidas", incluindo tratamentos tradicionais

### 🏥 **Origem e Características dos Textos**

Os textos foram coletados de fontes de domínio público conforme especificado no enunciado, seguindo as diretrizes do Projeto Gutenberg:

#### 📊 **Características dos Arquivos:**
- **Formato**: Arquivos .txt (texto simples)
- **Licença**: Domínio público (Creative Commons)
- **Qualidade**: Digitalizados e processados pelo Projeto Gutenberg
- **Acessibilidade**: Livre para uso educacional e de pesquisa

#### 📋 **Fontes Utilizadas:**
- **Projeto Gutenberg**: Biblioteca digital de obras em domínio público
- **URLs de Origem**:
  - [St. Bernard's](https://www.gutenberg.org/ebooks/46431)
  - [O Oraculo](https://www.gutenberg.org/ebooks/30462)

#### 📋 **Conteúdo dos Textos:**

**St. Bernard's: The Romance of a Medical Student**
- Narrativa ficcional sobre a vida de estudantes de medicina no século XIX
- Descreve práticas médicas, anatomia, e a evolução da medicina
- Oferece contexto histórico sobre a formação médica
- Contém terminologia médica e descrições de procedimentos

**O Oraculo do Passado, do Presente e do Futuro**
- Tratado médico-astrológico português do século XIX
- Contém "segredos" e tratamentos tradicionais para diversas moléstias
- Inclui receitas e procedimentos médicos da época
- Documenta práticas médicas históricas e crenças populares

### 🤖 Aplicações em Processamento de Linguagem Natural (NLP)

#### 🔍 **Como os Textos Podem Ser Analisados por Algoritmos de NLP:**

Os textos coletados podem ser processados por diferentes técnicas de NLP para extrair informações valiosas para o projeto CardioIA:

##### 1. **Reconhecimento de Entidades Nomeadas (NER) - Extração de Sintomas e Sinais:**

```python
# Exemplo de extração de sintomas cardíacos dos textos
cardiac_symptoms = [
    "dor torácica", "dispneia", "palpitações", 
    "síncope", "edema", "fadiga", "sudorese",
    "tontura", "ansiedade", "nervosismo"
]

# Aplicação: Identificar automaticamente sintomas em prontuários
def extract_symptoms(text):
    symptoms = []
    for symptom in cardiac_symptoms:
        if symptom.lower() in text.lower():
            symptoms.append(symptom)
    return symptoms
```

**Relevância**: Permite triagem automática de pacientes baseada em sintomas descritos, agilizando o processo de atendimento e priorização de casos.

##### 2. **Identificação de Fatores de Risco:**

- **Hipertensão arterial**: Detecção de valores pressóricos e termos relacionados
- **Diabetes mellitus**: Identificação de critérios diagnósticos e complicações
- **Dislipidemia**: Níveis de colesterol e triglicerídeos mencionados
- **Tabagismo**: Hábitos de fumo e programas de cessação
- **Obesidade**: IMC e circunferência abdominal

**Relevância**: Facilita a identificação automática de pacientes de alto risco cardiovascular, permitindo intervenções preventivas.

##### 3. **Classificação de Doenças Cardiovasculares:**

- **Doença arterial coronariana**: Termos como "estenose", "angina", "infarto"
- **Insuficiência cardíaca**: "edema", "dispneia", "fadiga"
- **Valvulopatias**: "estenose mitral", "insuficiência aórtica"
- **Arritmias cardíacas**: "fibrilação atrial", "taquicardia"
- **Acidente vascular cerebral**: "AVC", "isquemia cerebral"

**Relevância**: Permite categorização automática de prontuários e direcionamento para especialistas apropriados.

##### 4. **Análise de Sentimentos em Textos Médicos:**

- **Urgência**: Identificação de situações emergenciais ("dor intensa", "falta de ar súbita")
- **Gravidade**: Classificação da severidade das condições ("estável", "crítico")
- **Prognóstico**: Análise de expectativas de evolução ("favorável", "reservado")

**Relevância**: Ajuda na priorização de atendimentos e identificação de casos que requerem intervenção imediata.

##### 5. **Extração de Relacionamentos Médicos:**

- **Sintoma → Doença**: Mapeamento de manifestações clínicas com diagnósticos
- **Fator de Risco → Complicação**: Relações causais entre condições
- **Tratamento → Eficácia**: Resultados terapêuticos e respostas ao tratamento

**Relevância**: Construção de bases de conhecimento médico para suporte à decisão clínica.

#### 🎯 **Importância das Análises de NLP para o Projeto CardioIA:**

As análises de NLP são fundamentais para o sucesso do projeto CardioIA pelos seguintes motivos:

##### **1. Transformação de Dados Não Estruturados em Informação Acionável:**
- **Problema**: 80% dos dados médicos estão em formato textual não estruturado
- **Solução**: NLP converte prontuários, relatórios e literatura em dados estruturados
- **Impacto**: Permite análise quantitativa de informações qualitativas

##### **2. Automação de Processos Clínicos:**
- **Triagem Inteligente**: Identificação automática de sintomas e priorização de casos
- **Diagnóstico Assistido**: Sugestões baseadas em padrões textuais
- **Monitoramento Contínuo**: Análise de evolução clínica através de textos

##### **3. Redução de Erros Médicos:**
- **Padronização**: Eliminação de variações na terminologia médica
- **Validação**: Verificação automática de consistência em prontuários
- **Alertas**: Identificação de informações contraditórias ou ausentes

##### **4. Personalização do Cuidado:**
- **Perfil do Paciente**: Análise de histórico médico textual
- **Preferências**: Identificação de padrões de comunicação e compreensão
- **Aderência**: Monitoramento de relatos sobre medicação e tratamento

##### **5. Pesquisa e Desenvolvimento:**
- **Mineração de Literatura**: Análise de artigos científicos para descobertas
- **Farmacovigilância**: Detecção de efeitos adversos em relatórios
- **Epidemiologia**: Identificação de padrões populacionais em textos médicos

##### **6. Governança de Dados e Ética:**
- **Transparência**: Processamento claro e auditável de dados textuais
- **Privacidade**: Anonimização automática de informações pessoais
- **Viés**: Detecção e mitigação de preconceitos em textos médicos

#### 🧠 Algoritmos de NLP Recomendados:

1. Named Entity Recognition (NER):

- **SpaCy**: Para identificação de entidades médicas
- **BERT Médico**: Modelo especializado em textos de saúde
- **BioBERT**: Para reconhecimento de termos biomédicos

2. Classificação de Texto:

- **TF-IDF + SVM**: Para categorização de documentos
- **Word2Vec**: Para representação vetorial de termos médicos
- **BERT**: Para classificação contextual avançada

3. Extração de Informações:

- **Regex Patterns**: Para valores numéricos (pressão, colesterol)
- **Rule-based Systems**: Para sintomas e diagnósticos
- **Information Extraction**: Para relacionamentos médicos

4. Análise Semântica:

- **Topic Modeling**: Identificação de tópicos médicos
- **Sentiment Analysis**: Análise de urgência e gravidade
- **Text Summarization**: Resumo de prontuários médicos

### 🎯 Casos de Uso Específicos para CardioIA

#### 1. Assistente de Diagnóstico Inteligente:

```python
# Exemplo de pipeline de análise
def analyze_symptoms(text):
    symptoms = extract_symptoms(text)
    risk_factors = identify_risk_factors(text)
    probability = calculate_cardiovascular_risk(symptoms, risk_factors)
    return generate_recommendations(probability)
```

#### 2. Classificação Automática de Prontuários:

- **Categorização**: Por tipo de doença cardiovascular
- **Priorização**: Por urgência e gravidade
- **Roteamento**: Para especialistas apropriados

#### 3. Extração de Dados para Pesquisa:

- **Epidemiologia**: Padrões populacionais de doenças
- **Farmacovigilância**: Efeitos adversos de medicamentos
- **Qualidade Assistencial**: Indicadores de atendimento

#### 4. Sistema de Alertas Inteligentes:

- **Detecção de Emergências**: Sintomas de alto risco
- **Monitoramento**: Evolução de pacientes
- **Prevenção**: Identificação de fatores de risco

### 📈 Métricas de Qualidade dos Dados

#### ✅ Pontos Fortes:

- **Especialização**: Conteúdo específico de cardiologia
- **Atualização**: Baseado em literatura médica recente
- **Estruturação**: Organização clara por tópicos
- **Completude**: Cobertura abrangente da especialidade
- **Linguagem**: Português brasileiro médico

#### ⚠️ Limitações:

- **Volume**: 3 textos (mínimo exigido atendido, mas pode ser expandido)
- **Variedade**: Foco específico em cardiologia
- **Interatividade**: Textos estáticos (não interativos)
- **Validação**: Necessita revisão por especialistas para aplicação clínica

### 🔬 Próximos Passos para Expansão

#### 1. Ampliação do Corpus:

- **Artigos Científicos**: Integração com PubMed/SciELO
- **Prontuários Médicos**: Dados clínicos reais (anônimos)
- **Guias Clínicos**: Protocolos de tratamento
- **Casos Clínicos**: Relatos de casos complexos

#### 2. Processamento Avançado:

- **Análise Temporal**: Evolução de sintomas
- **Correlação Multimodal**: Integração com dados numéricos
- **Personalização**: Adaptação por perfil do paciente
- **Aprendizado Contínuo**: Atualização de modelos

#### 3. Validação Clínica:

- **Revisão por Especialistas**: Cardiologistas experientes
- **Testes de Usabilidade**: Interface médica
- **Estudos de Precisão**: Comparação com diagnóstico humano
- **Certificação**: Aprovação regulatória quando aplicável

---

## 🖼️ Parte 3 - Dados Visuais (VC)

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
  - **normal**: 50 imagens de exames sem anomalias visíveis.
  - **anormal**: 50 imagens de exames com diagnóstico de estenose.

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

### **Princípios Aplicados:**
- **Transparência**: Origem e processamento dos dados claramente documentados
- **Qualidade**: Validação e limpeza rigorosa dos dados
- **Privacidade**: Dados anonimizados e sem informações pessoais
- **Viés**: Análise de representatividade demográfica e clínica
- **Reprodutibilidade**: Scripts e metodologia completamente documentados

### **Considerações Éticas:**
- Dados coletados respeitando diretrizes médicas
- Uso exclusivo para fins educacionais e de pesquisa
- Conformidade com regulamentações de dados de saúde

---

## 🚀 Próximas Etapas

### **Futuras (Fases 2-7):**
Para mais informações sobre as próximas fases do projeto CardioIA, consulte o arquivo [project/OVERVIEW.md](project/OVERVIEW.md).

### **Recomendações para Expansão:**

- **Ampliar Corpus Textual**: Adicionar artigos científicos do SciELO
- **Dados Mais Recentes**: Considerar datasets cardiológicos contemporâneos
- **Validação Clínica**: Revisão por especialistas em cardiologia
- **Integração Multimodal**: Combinação de dados numéricos, textuais e visuais

---

## 👥 Equipe

- Gustavo Castro (RM560831)
- Luis Emidio (RM559976)
- Matheus Conciani (RM559473) 

---

## 📚 Referências

1. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). Heart Disease [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
2. Detrano, R. et al. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology.
3. UCI Machine Learning Repository. Heart Disease Dataset. Disponível em: https://archive.ics.uci.edu/dataset/45/heart+disease

---

**Projeto desenvolvido para FIAP - Fase 1: Batimentos de Dados**  

[LICENSE.md](LICENSE.md)
