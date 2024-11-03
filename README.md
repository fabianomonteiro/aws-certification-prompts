# AWS Certification Prompts

Bem-vindo ao **AWS Certification Prompts**, uma coleção de prompts de simulado para certificações AWS. Este repositório visa ajudar candidatos a se prepararem para exames AWS, oferecendo experiências interativas e realistas que refletem o estilo e a complexidade dos exames oficiais.

## Visão Geral

Este repositório contém prompts para criar chatbots que simulam perguntas de certificação AWS, incluindo o AWS Cloud Practitioner, SysOps Administrator Associate, Solutions Architect Professional, entre outros. Cada prompt oferece perguntas práticas, feedback em tempo real e recursos adicionais para reforçar o aprendizado.

### Funcionalidades dos Prompts

- **Interatividade:** Prompts que guiam o usuário em simulados personalizados, com feedback imediato e explicações.
- **Reforço de Aprendizado:** Flashcards e explicações detalhadas para questões, fortalecendo a compreensão.
- **Distribuição de Questões:** Divisão de perguntas conforme as porcentagens do exame oficial.
- **Atualização Contínua:** Prompts atualizados para acompanhar mudanças nos serviços da AWS.

## Status de Validação dos Prompts

| Certificação                          | Nível        | [ChatGPT](https://openai.com/chatgpt) | [Claude](https://claude.ai) | [Gemini](https://gemini.google.com) | Status |
|---------------------------------------|--------------|---------------------------------------|-----------------------------------------|---------------------------------------------|---------|
| AWS Certified Cloud Practitioner       | Foundational | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Certified AI Practitioner          | Foundational | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Certified SysOps Administrator     | Associate    | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Certified Solutions Architect      | Associate    | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Certified Developer                | Associate    | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Certified Machine Learning Engineer| Associate    | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Certified Data Engineer            | Associate    | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Solutions Architect Professional   | Professional | ✅                                     | ✅                                     | ❌                                         | Ativo   |
| AWS DevOps Engineer Professional       | Professional | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Machine Learning Specialty         | Specialty    | ✅                                     | ❓                                     | ❌                                         | Ativo   |
| AWS Security Specialty                 | Specialty    | ❓                                     | ❓                                     | ❓                                         | Em Desenvolvimento |
| AWS Advanced Networking Specialty      | Specialty    | ❓                                     | ❓                                     | ❓                                         | Em Desenvolvimento |
| AWS Database Specialty                 | Specialty    | ❓                                     | ❓                                     | ❓                                         | Em Desenvolvimento |
| AWS Data Analytics Specialty           | Specialty    | ❓                                     | ❓                                     | ❓                                         | Em Desenvolvimento |
| AWS SAP on AWS Specialty               | Specialty    | ❓                                     | ❓                                     | ❓                                         | Em Desenvolvimento |

**Legenda:**
- ✅ Testado e funcionando corretamente
- ⚠️ Testado, mas apresenta inconsistências
- ❌ Testado e não funcional
- ❓ Ainda não testado

## Estrutura do Repositório

```
aws-certification-prompts/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── 01-foundational/
│   ├── ai-practitioner/
│   │   └── prompt.md
│   └── cloud-practitioner/
│       └── prompt.md
├── 02-associate/
│   ├── data-engineer/
│   │   └── prompt.md
│   ├── developer/
│   │   └── prompt.md
│   ├── machine-learning-engineer/
│   │   └── prompt.md
│   ├── solutions-architect/
│   │   └── prompt.md
│   └── sysops-admin/
│       └── prompt.md
├── 03-professional/
│   ├── devops-engineer/
│   │   ├── README.md
│   │   └── prompt.md
│   └── solutions-architect/
│       ├── README.md
│       └── prompt.md
└── 04-specialty/
    ├── machine-learning/
    │   └── prompt.md
    ├── networking/
    └── security/
```

## Como Usar

1. **Escolha uma Certificação:** Navegue até o diretório específico para a certificação desejada.
2. **Copie e Cole o Prompt:** Insira o prompt no modelo de IA desejado e personalize conforme necessário.
3. **Simulado Personalizado:** Responda às perguntas e receba feedback instantâneo e explicações detalhadas.
4. **Revisão com Flashcards:** Opcionalmente, revise conceitos importantes usando flashcards baseados nas perguntas respondidas.

## Contribuindo

Para contribuir, faça o seguinte:

1. **Crie um Fork** do repositório.
2. **Crie uma Branch de Feature:** `git checkout -b feature/nova-certificacao`
3. **Commit das Alterações:** `git commit -m 'Adiciona prompts para nova certificação'`
4. **Envie para a Branch:** `git push origin feature/nova-certificacao`
5. **Abra um Pull Request.**

### Diretrizes para Contribuição

- Organize os prompts por certificação e nível.
- Atualize a tabela de status de validação e documente requisitos específicos.
- Inclua exemplos de uso e feedback esperado.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).