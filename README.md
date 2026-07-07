# 🤖 Gemini API: Projetos & Arquitetura de IA (Portfólio de Estudos)

Este repositório reúne um ecossistema de ferramentas, scripts e microsserviços desenvolvidos em **Python** utilizando a nova **Google GenAI SDK**. O objetivo principal deste ecossistema é demonstrar a aplicação prática de engenharia de software e arquitetura robusta voltada para Inteligência Artificial Generativa.

O portfólio evoluiu de scripts de automação simples para sistemas contínuos e resilientes, aplicando conceitos modernos de segurança e controle determinístico de LLMs (Large Language Models).

---

## 🎯 Projetos em Destaque

### 1. 🛡️ Moderador de Conteúdo Estrito (`moderador_comentarios.py`)
Um sistema de moderação automática para e-commerce que analisa o *input* de utilizadores em tempo real para aprovar ou rejeitar comentários com base em diretrizes de comunidade.
* **Destaque Técnico:** Implementação de saídas estritamente determinísticas e isolamento completo de instruções do sistema.

### 2. 💰 Calculadora Inteligente de Reembolsos (`calculadora_reembolso.py`)
Um motor de auditoria que processa pedidos de reembolso complexos para companhias aéreas, lidando com exceções de negócio (leis de aviação civil, prazos e casos de força maior).
* **Destaque Técnico:** Uso de **Chain of Thought (Cadeia de Pensamento)** para forçar o modelo a deduzir a lógica antes de emitir um veredito, reduzindo drasticamente alucinações.

### 3. 💬 Chatbot Contínuo com Gestão de Estado (`chat_continuo.py`)
Simulação de uma interface de chat persistente via terminal que gerencia o fluxo de conversação do utilizador sem perda de contexto.

---

## 🛠️ Competências e Engenharia de Software Aplicada

Durante o desenvolvimento deste repositório, foram aplicadas as seguintes boas práticas de engenharia de IA:

* **System Instructions vs. User Prompts:** Arquitetura defensiva que separa as regras imutáveis do sistema (`system_instruction`) dos dados dinâmicos enviados pelo utilizador (`contents`). Esta abordagem blinda as aplicações contra ataques de **Prompt Injection**.
* **Controle de Temperatura (`temperature=0.0`):** Configuração cirúrgica da criatividade do modelo. Em projetos de auditoria, moderação e estruturação de dados, a temperatura foi travada a zero para garantir respostas matemáticas, consistentes e previsíveis.
* **Tratamento de Erros e Resiliência (`try/except`):** Código protegido contra falhas de infraestrutura externa (como o erro `503 Service Unavailable`), garantindo que a aplicação falhe de forma elegante sem interromper a execução do utilizador.
* **Gestão Segura de Credenciais:** Integração com o sistema operativo através da biblioteca `os` para leitura de chaves de API via variáveis de ambiente (`os.environ.get`), seguindo os padrões de segurança contra fuga de segredos (*secret scanning*).

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **SDK Oficial:** `google-genai`
* **Modelos de Linguagem:** `gemini-2.5-flash` (Otimizado para baixa latência e alta eficiência de contexto)
* **Ambiente de Desenvolvimento:** Linux via WSL (Windows Subsystem for Linux) e Git para controlo de versões.

---

## 🔧 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Hudsonhiro/API-projects.git](https://github.com/Hudsonhiro/API-projects.git)
   cd API-projects
