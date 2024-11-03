# Guia de Contribuição

Obrigado por considerar contribuir com o projeto AWS Certification Prompts! Este documento fornece as diretrizes e melhores práticas para contribuir com o repositório.

## Índice

1. [Código de Conduta](#código-de-conduta)
2. [Como Contribuir](#como-contribuir)
3. [Estrutura dos Prompts](#estrutura-dos-prompts)
4. [Processo de Validação](#processo-de-validação)
5. [Diretrizes de Estilo](#diretrizes-de-estilo)
6. [Reportando Problemas](#reportando-problemas)

## Código de Conduta

Este projeto segue um Código de Conduta que esperamos que todos os contribuidores sigam. Por favor, leia [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) antes de contribuir.

Principais pontos:
- Seja respeitoso e inclusivo
- Evite conteúdo ofensivo ou discriminatório
- Mantenha o foco profissional
- Aceite feedback construtivo

## Como Contribuir

### 1. Preparando seu Ambiente

```bash
# Fork o repositório
# Clone seu fork
git clone https://github.com/fabianomonteiro/aws-certification-prompts.git
cd aws-certification-prompts

# Crie uma branch para sua contribuição
git checkout -b feature/nova-contribuicao
```

### 2. Tipos de Contribuições

- **Novos Prompts**: Adicionar prompts para certificações ainda não cobertas
- **Melhorias**: Aperfeiçoar prompts existentes
- **Correções**: Corrigir erros ou imprecisões
- **Documentação**: Melhorar ou adicionar documentação
- **Validação**: Testar prompts com diferentes modelos de IA

### 3. Processo de Submissão

1. Certifique-se que sua contribuição segue as diretrizes
2. Teste suas alterações
3. Atualize a documentação relevante
4. Faça commit de suas alterações
5. Submeta um Pull Request

## Estrutura dos Prompts

Cada prompt deve seguir esta estrutura básica:

```markdown
# [Nome da Certificação] Prompt

## Contexto
[Descrição e objetivos]

## Instruções para o Modelo de IA
[Instruções detalhadas]

## Comandos de Controle
[Lista de comandos disponíveis]

## Formato das Respostas
[Estrutura esperada]

## Tópicos Cobertos
[Lista de tópicos]

## Exemplos de Uso
[Demonstrações práticas]
```

## Processo de Validação

### 1. Teste Local
- Teste o prompt com pelo menos um modelo de IA
- Verifique se todas as seções necessárias estão presentes
- Confirme que os comandos funcionam conforme esperado

### 2. Documentação de Testes
Atualize a tabela de status no README principal:

```markdown
| Certificação | ChatGPT | Claude | Gemini | Status |
|-------------|----------|--------|---------|---------|
| Nova Cert   | ✅/⚠️/❓  | ...    | ...     | ...     |
```

### 3. Critérios de Validação
- Precisão das respostas
- Consistência com o exame real
- Clareza das explicações
- Funcionamento dos comandos
- Adequação do nível de dificuldade

## Diretrizes de Estilo

### Markdown
- Use cabeçalhos apropriados (#, ##, ###)
- Mantenha uma linha em branco entre seções
- Use listas quando apropriado
- Inclua exemplos em blocos de código
- Mantenha a formatação consistente

### Conteúdo
- Seja claro e conciso
- Use linguagem profissional
- Evite jargão desnecessário
- Mantenha o foco no objetivo educacional
- Inclua exemplos práticos

## Reportando Problemas

### Issues
Use os templates de issue apropriados para:
- Reportar bugs
- Sugerir melhorias
- Propor novos recursos
- Solicitar esclarecimentos

### Informações Necessárias
- Descrição clara do problema
- Passos para reproduzir (se aplicável)
- Comportamento esperado vs. observado
- Modelo de IA utilizado
- Screenshots ou exemplos (se relevante)

## Dicas Adicionais

1. **Antes de Contribuir**
   - Verifique se já não existe uma issue similar
   - Discuta grandes mudanças em uma issue primeiro
   - Revise a documentação existente

2. **Durante o Desenvolvimento**
   - Mantenha as alterações focadas e específicas
   - Comente seu código quando necessário
   - Siga as convenções existentes

3. **Ao Submeter**
   - Escreva mensagens de commit claras
   - Inclua uma descrição detalhada no PR
   - Responda a feedbacks prontamente

## Agradecimentos

Suas contribuições são valiosas para a comunidade! Agradecemos seu tempo e esforço para melhorar este projeto.

## Dúvidas?

Se você tiver alguma dúvida sobre como contribuir, sinta-se à vontade para:
- Abrir uma issue
- Entrar em contato através do LinkedIn
- Consultar a documentação existente

---

Ao contribuir com este projeto, você concorda em seguir estas diretrizes e o Código de Conduta.