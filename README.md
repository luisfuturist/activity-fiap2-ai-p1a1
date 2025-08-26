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
│   ├── textual/
│   │   └── [A ser desenvolvido pelos integrantes]
│   └── visual/
│       └── [A ser desenvolvido pelos integrantes]
├── docs/
│   ├── relatorio_dataset_cardiaco.md
│   └── [Documentação adicional]
├── assets/
│   ├── heart_disease_overview.png
│   ├── correlation_matrix.png
│   └── [Recursos visuais]
└── scripts/
    ├── heart_disease_analysis.py
    ├── process_heart_data.py
    └── create_excel_dataset.py
```

---

## 📊 Parte 1 - Dados Numéricos (IoT)

### ✅ **Status: CONCLUÍDO**

### 📁 **Arquivos de Dados**
- **Dataset Principal**: [https://docs.google.com/spreadsheets/d/1ORs0W-SfhUboAbOAMELbmYAZ_VGF-Dd_lw4O-zPUKNg/edit?usp=drive_link)
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

### ⏳ **Status: A SER DESENVOLVIDO**

*Esta seção será preenchida pelos integrantes responsáveis pela coleta e análise de textos médicos.*

**Objetivos:**
- Coletar textos de fontes como SciELO, BVS, artigos do SUS
- Preparar dados para análise de sentimentos, extração de sintomas
- Desenvolver classificação de tópicos médicos

---

## 🖼️ Parte 3 - Dados Visuais (VC)

### ⏳ **Status: A SER DESENVOLVIDO**

*Esta seção será preenchida pelos integrantes responsáveis pela coleta e análise de imagens médicas.*

**Objetivos:**
- Reunir imagens de ECGs, angiogramas, raio-X torácico
- Preparar dados para detecção de padrões e anomalias
- Desenvolver algoritmos de reconhecimento de imagens médicas

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

1. **Integração de Dados**: Combinar as três modalidades de dados
2. **Desenvolvimento de Modelos**: Criar algoritmos de IA especializados
3. **Validação Clínica**: Testar modelos com especialistas
4. **Interface de Usuário**: Desenvolver sistema para uso hospitalar
5. **Implantação**: Deploy em ambiente de produção simulado

---

## 👥 Equipe

- **Parte 1 (Dados Numéricos)**: [Nome do Responsável]
- **Parte 2 (Dados Textuais)**: [A ser preenchido]
- **Parte 3 (Dados Visuais)**: [A ser preenchido]

---

## 📚 Referências

1. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). Heart Disease [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
2. Detrano, R. et al. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology.
3. UCI Machine Learning Repository. Heart Disease Dataset. Disponível em: https://archive.ics.uci.edu/dataset/45/heart+disease

---

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso da FIAP. Os dados utilizados seguem suas respectivas licenças originais.

---

**Projeto desenvolvido para FIAP - Fase 1: Batimentos de Dados**  
**Ano**: 2025  
**Versão**: 1.0

