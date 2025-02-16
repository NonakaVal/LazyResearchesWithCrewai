# Automação de Pesquisa com CrewAI

Este projeto utiliza **CrewAI** e **GPT** para automatizar fluxos de trabalho, como pesquisas, criação de planos de estudo e coleta de notícias de jogos. A estrutura é modular e flexível, permitindo a personalização conforme a necessidade do usuário.

Estou publicando alguns outputS em :  [https://lazyresearches.blogspot.com/]

## **Requisitos**

### Bibliotecas Necessárias
Certifique-se de instalar as seguintes dependências:

- `dotenv`
- `os`
- `crewai`
- `crewai_tools`
- `langchain_openai`

Para instalar, execute:

```bash
pip install python-dotenv crewai langchain_openai tabulate
```

### Configuração de API
Crie um arquivo `.env` e insira as chaves de API necessárias:

```env
OPENAI_API_KEY="sua_chave_openai"
SERPER_API_KEY="sua_chave_serper"
```

## **Como Usar**

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/NonakaVal/LazyResearchesWithCrewai.git
   cd LazyResearchesWithCrewai
   ```

2. **Configuração**
   Certifique-se de que o arquivo `.env` contém suas chaves de API.

3. **Execute o Script**
   ```bash
   python main.py
   ```

4. **Escolha a Equipe**
   O script oferece três opções:
   - **Search Crew**: Para pesquisas gerais.
   - **Study Plan Crew**: Para criar planos de estudo.
   - **Game News Crew**: Para coleta de notícias de jogos.
   - **ProdcutContentCrew** : Pesquisar ideias de conteúdos e informações sobre um produto específico

5. **Forneça Detalhes**
   Insira o contexto, a pergunta de pesquisa ou o tópico relacionado. O sistema irá processar os dados e gerar um resumo no diretório escolhido.

## **Recursos**

- **Agentes Baseados em IA**: Executam tarefas específicas para cada equipe.
- **Resultados Estruturados**: Relatórios salvos localmente com insights detalhados.

## **Contribuições**

Contribuições são bem-vindas! Envie **issues** ou **pull requests** para melhorias.

## **Licença**

Este projeto está sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
