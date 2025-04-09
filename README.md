# LLMAppStreamlit - ZTM

## Notes on what we will be using & brief intro about them

- learn to use Streamlit to create a frontend for an LLM-powered Q&A application.
- **`Streamlit is an open-source Python library that simplifies the creation and sharing of custom frontends for machine learning and data science apps with the world.`**
- **LangChain is an OpenSource framework that allows developers working with Al to combine LLMs with external sources of computation and data.**
  - LLMs alone are often limited in their ability to understand the context, interact with the real world, or learn and adapt.
  - LLMs have an impressive general knowledge but are limited to their training data.
  - LangChain allows you to connect an LLM like GPT-4/Gemini to your own sources of data.
  - Using LangChain you can make your LLM Application take actions.
  - LangChain is data-aware and agentic-aware.
  - LangChain Main Concepts
    - LangChain Components
      - LLM Wrappers - allow us to connect to and use large language models like GPT -4.
      - Prompt Templates - allow us to create dynamic prompts which are the input to the LLMs.
      - Indexes - Indexes allow us to extract relevant information for the LLMs.
      - Memory - is the concept of storing and retrieving data in the process of a conversation.
        - Short-term memory generally refers to how to pass data in the context of a single conversation and - long-term memory deals with how to fetch and update information between conversations.
    - Chains - Chains allow us to combine multiple components together to solve a specific task and build an entire LLM application.
    - Agents - Agents facilitate interaction between the LLM and external APIs. They play a crucial role in decision-making, determining which actions the LLM should undertake.This process involves taking an action, observing the result, and then repeating the cycle until completion.
- **Example**: You take a document you want your language model to reference and slice it up into smaller chunks,store those chunks in a vector database as embeddings,which are numeric representations of text.These capabilities open up infinite no.of practical use cases.Now you can ask anything about the document(which may be 100 pages long) & the app will give the correct answer.Langchain implements abstraction like chains and agents so that a developer doesn't happen to know what happens under the hood.
  - Example use-cases: ChatBots, Questions Answering System, Summarization Tools.

### Deep Dive Notes step by step

#### commands & Resources

```bash
echo "# LLMAppStreamlit" >> README.md
```

**Resources :**

`Here are the resources you'll need for this Project:`

[Files for Section 1 (Streamlit Fundamentals)](https://drive.google.com/drive/folders/1BkdFVZ4pE4eAabkGz7SH0HK1cwDww8eJ)

[Files for Section 2 (Building a Frontend for the LLM-powered Q&A App using Streamlit)](https://drive.google.com/drive/folders/1Ein0oHa-eAyLNC-dat73G6OC6SnPX6lJ?usp=sharing)
