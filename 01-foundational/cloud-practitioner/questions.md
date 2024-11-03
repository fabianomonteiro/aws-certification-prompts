1. **Como a AWS cobra pelo uso do AWS Lambda depois que o nível gratuito é ultrapassado?** (Selecione **DUAS**.)

   - **A** Pelo tempo que leva para que a função do Lambda seja executada  
     _Correto._ As cobranças do Lambda dependem do tempo necessário para executar o código.  
     [Saiba mais sobre os preços do Lambda.](https://aws.amazon.com/lambda/pricing/)  
     [Saiba mais sobre o Lambda.](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

   - **B** Pelo número de versões de uma função específica do Lambda  
     _Incorreto._ O número de versões de uma função específica do Lambda não contribui para o custo. Você é cobrado pelo número de solicitações de suas funções do Lambda e pelo tempo que leva para que seu código seja executado.

   - **C** Pelo número de solicitações feitas para uma determinada função do Lambda  
     _Correto._ As cobranças do Lambda dependem do número de solicitações para suas funções do Lambda.  
     [Saiba mais sobre os preços do Lambda.](https://aws.amazon.com/lambda/pricing/)  
     [Saiba mais sobre o Lambda.](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

   - **D** Pela linguagem de programação usada para a função do Lambda  
     _Incorreto._ A linguagem de programação usada para criar a função do Lambda não contribui para o custo. Você é cobrado pelo número de solicitações de suas funções do Lambda e pelo tempo que leva para que seu código seja executado.

   - **E** Pelo número total de funções do Lambda em uma conta da AWS  
     _Incorreto._ Não há cobrança baseada no número de funções em uma conta da AWS. Você é cobrado pelo número de solicitações de suas funções do Lambda e pelo tempo que leva para que seu código seja executado.

   **Resposta correta:** A, C

---

2. **Uma empresa quer criar um aplicativo de aprendizagem para estudantes. O aplicativo de aprendizagem deve dar aos alunos a opção de escolher um botão para que o texto seja lido em voz alta para eles.**

   - **A** Amazon Transcribe  
     _Incorreto._ O Amazon Transcribe é um serviço que usa machine learning para converter dados de áudio em texto. O Amazon Transcribe não é um serviço de conversão de texto em fala.  
     [Saiba mais sobre o Amazon Transcribe.](https://docs.aws.amazon.com/transcribe/latest/dg/what-is.html)

   - **B** Amazon Polly  
     _Correto._ O Amazon Polly é um serviço de machine learning que converte texto em fala. Esse serviço oferece a capacidade de ler texto em voz alta.  
     [Saiba mais sobre o Amazon Polly.](https://docs.aws.amazon.com/polly/latest/dg/what-is.html)

   - **C** Amazon Translate  
     _Incorreto._ O Amazon Translate é um serviço de tradução de idiomas com machine learning. O Amazon Translate não é um serviço de conversão de texto em fala.  
     [Saiba mais sobre o Amazon Translate.](https://docs.aws.amazon.com/translate/latest/dg/what-is.html)

   - **D** Amazon Textract  
     _Incorreto._ O Amazon Textract é um serviço de machine learning que pode extrair texto de documentos digitalizados. O Amazon Textract não é um serviço de conversão de texto em fala.  
     [Saiba mais sobre o Amazon Textract.](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)

   **Resposta correta:** B

---

3. **Qual serviço da AWS permite que os clientes comprem capacidade não utilizada do Amazon EC2 a uma taxa com desconto frequente?**

- **A** Instâncias reservadas  
  _Incorreto._ As instâncias reservadas reservam alguma capacidade para seu uso a qualquer momento. Às vezes, as instâncias reservadas podem gerar um desconto. No entanto, essa não é uma capacidade não utilizada.  
  [Saiba mais sobre instâncias reservadas.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html)

- **B** Instâncias sob demanda  
  _Incorreto._ As instâncias sob demanda são a opção de compra padrão e estão imediatamente disponíveis. As instâncias sob demanda não são descontadas.  
  [Saiba mais sobre instâncias sob demanda.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html)

- **C** Instâncias dedicadas  
  _Incorreto._ As instâncias dedicadas são executadas em VPCs em hardware dedicado a esse cliente individual e são frequentemente usadas quando há restrições de licenciamento ou conformidade. Instâncias dedicadas não são descontadas.  
  [Saiba mais sobre instâncias dedicadas.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html)

- **D** Spot Instances  
  _Correto._ Com as Spot Instances, você pode acessar a capacidade não utilizada do EC2. As Spot Instances podem ser descontadas.  
  [Saiba mais sobre as Spot Instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)

**Resposta correta:** D

---

4. **Uma empresa tem um servidor on-premises baseado em Linux com um banco de dados Oracle executado nele. A empresa quer migrar o servidor de banco de dados para ser executado em uma instância do Amazon EC2 na AWS.**

**Qual serviço a empresa deve usar para concluir a migração?**

- **A** AWS Database Migration Service (AWS DMS)  
  _Incorreto._ O AWS DMS pode ser usado para migrar dados de um banco de dados on-premises para um banco de dados na AWS. No entanto, o AWS DMS não migra o servidor real para uma instância do EC2.  
  [Saiba mais sobre o AWS DMS.](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)

- **B** AWS Migration Hub  
  _Incorreto._ O Migration Hub é um serviço que ajuda a planejar e rastrear migrações de aplicativos. O Migration Hub não realiza migrações do sistema.  
  [Saiba mais sobre o Migration Hub.](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)

- **C** AWS Application Migration Service (AWS MGN)  
  _Correto._ O AWS MGN é uma solução “lift-and-shift” automatizada. Essa solução pode migrar servidores físicos e quaisquer bancos de dados ou aplicativos executados neles para instâncias do EC2 na AWS.  
  [Saiba mais sobre o AWS MGN.](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)

- **D** AWS Application Discovery Service  
  _Incorreto._ O Application Discovery Service coleta informações sobre o uso e a configuração de servidores on-premises para ajudar a planejar uma migração para a AWS. Na verdade, o Application Discovery Service não realiza migrações.  
  [Saiba mais sobre o Application Discovery Service.](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html)

**Resposta correta:** C

---

5. **Quais componentes de credencial são necessários para obter acesso programático a uma conta da AWS?** (Selecione **DUAS**.)

- **A** Uma ID de chave de acesso  
  _Correto._ O acesso programático requer uma ID de chave de acesso e uma chave de acesso secreta que pode ser atribuída a um usuário da AWS.  
  [Saiba mais sobre as práticas recomendadas de chaves de acesso.](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html)

- **B** Uma chave primária  
  _Incorreto._ Uma chave primária é um recurso usado no gerenciamento de banco de dados. Ele não concede acesso à conta da AWS.  
  [Saiba mais sobre as credenciais de segurança da AWS.](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)

- **C** Uma chave de acesso secreta  
  _Correto._ O acesso programático requer uma ID de chave de acesso e uma chave de acesso secreta que pode ser atribuída a um usuário da AWS.  
  [Saiba mais sobre as práticas recomendadas de chaves de acesso.](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html)

- **D** Uma ID de usuário  
  _Incorreto._ Uma ID de usuário é utilizada para credenciais de segurança do IAM, mas não para acesso programático.  
  [Saiba mais sobre os usuários do IAM.](https://docs.aws.amazon.com/accounts/latest/reference/root-user-vs-iam.html)

- **E** Uma chave secundária  
  _Incorreto._ Uma chave secundária é um recurso usado no gerenciamento de banco de dados. Ele não concede acesso à conta da AWS.  
  [Saiba mais sobre as credenciais de segurança da AWS.](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html)

**Resposta correta:** A, C

---

6. **Quais tarefas são de responsabilidade do cliente de acordo com o modelo de responsabilidade compartilhada da AWS?** (Selecione **DUAS**.)

- **A** Corrigir o sistema operacional que as funções do AWS Lambda usam.  
  _Incorreto._ A AWS fornece o Lambda como um serviço. O cliente não precisa corrigir o sistema operacional.  
  [Saiba mais sobre o modelo de responsabilidade compartilhada.](https://aws.amazon.com/compliance/shared-responsibility-model/)

- **B** Instalar patches nas instâncias de banco de dados do Amazon RDS.  
  _Incorreto._ A AWS fornece o Amazon RDS como um serviço. A AWS gerencia patches para o mecanismo do Amazon RDS. O cliente pode escolher uma janela de tempo para instalar os patches.  
  [Saiba mais sobre o gerenciamento de patches para o Amazon RDS.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html)

- **C** Controlar o acesso físico ao data center que contém a VPC do cliente.  
  _Incorreto._ A AWS não permite o acesso aos data centers. Um cliente pode fazer um tour virtual por um data center para entender as medidas e controles de segurança. Os clientes não podem visitar os data centers pessoalmente.  
  [Saiba mais sobre os data centers da AWS.](https://aws.amazon.com/compliance/data-center/data-centers/)

- **D** Configurar os usuários do IAM de acordo com o princípio de menor privilégio.  
  _Correto._ A AWS fornece o AWS Identity and Access Management (IAM) como um serviço. O cliente define os usuários do IAM e as políticas de acesso que se aplicam a esses usuários.  
  [Saiba mais sobre o modelo de responsabilidade compartilhada.](https://aws.amazon.com/compliance/shared-responsibility-model/)

- **E** Configurar um bucket do Amazon S3 para permitir o acesso público.  
  _Correto._ O cliente determina as permissões de acesso aos buckets do S3 que o cliente possui.  
  [Saiba mais sobre o modelo de responsabilidade compartilhada.](https://aws.amazon.com/compliance/shared-responsibility-model/)

**Resposta correta:** D, E

---

7. **Qual serviço da AWS identifica grupos de segurança que permitem acesso irrestrito aos recursos da AWS de um usuário?**

- **A** AWS Trusted Advisor  
  _Correto._ O Trusted Advisor verifica em grupos de segurança regras que permitam acesso irrestrito a um recurso. O acesso irrestrito aumenta as oportunidades para atividades maliciosas, como hacking, ataques de negação de serviço, perda de dados.  
  [Saiba mais sobre as verificações do Trusted Advisor.](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html)

- **B** AWS Config  
  _Incorreto._ O AWS Config monitora e registra continuamente as alterações em seus recursos da AWS, mas não identifica os grupos de segurança que permitem acesso irrestrito.  
  [Saiba mais sobre o AWS Config.](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

- **C** Amazon CloudWatch  
  _Incorreto._ O CloudWatch é um serviço de monitoramento que coleta e rastreia métricas para recursos da AWS. Ele não identifica os grupos de segurança que permitem acesso irrestrito.  
  [Saiba mais sobre o CloudWatch.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

- **D** AWS CloudTrail  
  _Incorreto._ O CloudTrail fornece um registro de auditoria de chamadas de API. Ele não identifica os grupos de segurança que permitem acesso irrestrito.  
  [Saiba mais sobre o CloudTrail.](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

**Resposta correta:** A

---

8. **Uma empresa necessita de um banco de dados relacional na AWS que registre os pedidos de novos clientes em um site.**

**Qual serviço ou recurso da AWS atenderá a esse requisito?**

- **A** AWS Global Accelerator  
  _Incorreto._ O Global Accelerator é um serviço de rede que melhora o desempenho do tráfego de rede de seus usuários em até 60%. O Global Accelerator usa a infraestrutura de rede global da AWS. O Global Accelerator não é um banco de dados relacional.  
  [Saiba mais sobre o Global Accelerator.](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

- **B** Amazon DynamoDB  
  _Incorreto._ O DynamoDB é um serviço de banco de dados NoSQL totalmente gerenciado. Ele tem desempenho rápido e previsível, com dimensionamento integrado. No entanto, o DynamoDB não é um banco de dados relacional.  
  [Saiba mais sobre o DynamoDB.](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

- **C** Amazon Aurora  
  _Correto._ O Aurora é um banco de dados relacional compatível com MySQL e PostgreSQL, e foi criado para a nuvem. O Aurora combina o desempenho e a disponibilidade de bancos de dados comerciais tradicionais com a simplicidade e a economia de bancos de dados de código aberto.  
  [Saiba mais sobre o Aurora.](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

- **D** Amazon Elastic Block Store (Amazon EBS)  
  _Incorreto._ O Amazon EBS é um serviço de armazenamento em blocos fácil de usar e de alto desempenho. Você pode usar o Amazon EBS com o Amazon EC2 para cargas de trabalho intensivas em produtividade e transações em qualquer escala. Você pode executar um banco de dados em instâncias do Amazon EC2 e usar o Amazon EBS para o armazenamento desse banco de dados. No entanto, o Amazon EBS por si só não é um banco de dados relacional.  
  [Saiba mais sobre o Amazon EBS.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)

**Resposta correta:** C

---

9. **Uma empresa está hospedando um site estático em um único bucket do Amazon S3.**

**Qual serviço da AWS alcançará menor latência e altas velocidades de transferência?**

- **A** AWS Elastic Beanstalk  
  _Incorreto._ O Elastic Beanstalk é um serviço para implantar e dimensionar serviços e aplicativos Web desenvolvidos com linguagens de programação comuns em infraestrutura implantada automaticamente com gerenciamento de capacidade, balanceamento de carga, auto scaling e monitoramento. O Elastic Beanstalk facilita o provisionamento e a conformidade de um aplicativo. O Elastic Beanstalk não reduz a latência do site.  
  [Saiba mais sobre o Elastic Beanstalk.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

- **B** Amazon DynamoDB Accelerator (DAX)  
  _Incorreto._ O DAX é usado para reduzir o tempo de resposta de uma tabela do DynamoDB de um dígito em milissegundos para microssegundos. As tabelas do DynamoDB não podem hospedar sites estáticos.  
  [Saiba mais sobre o DAX.](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)

- **C** Amazon Route 53  
  _Incorreto._ O Route 53 é um serviço da Web de DNS altamente disponível e dimensionável. As três principais funções do Route 53 são registrar nomes de domínio, rotear o tráfego da internet para os recursos do domínio e conferir a integridade desses recursos. O Route 53 pode direcionar o tráfego para buckets do S3. Mas como a pergunta descreve apenas um bucket do S3, o Route 53 teria somente uma rota potencial e não poderia reduzir a latência.  
  [Saiba mais sobre o Route 53.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)  
  [Saiba mais sobre como rotear para buckets do S3 com o Route 53.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/RoutingToS3Bucket.html)

- **D** Amazon CloudFront  
  _Correto._ O CloudFront é um serviço da Web que acelera a distribuição do conteúdo estático e dinâmico da Web, como arquivos .html, .css, .js e de imagem aos usuários. O conteúdo é armazenado em cache nos locais de borda. O conteúdo acessado repetidamente pode ser servido a partir dos locais de borda, em vez do bucket de origem do S3.  
  [Saiba mais sobre o CloudFront.](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html#IntroductionUseCasesStaticWebsite)

**Resposta correta:** D

---

10. **Qual é o plano MÍNIMO do AWS Support que fornece suporte técnico por meio de chamadas telefônicas?**

- **A** Enterprise  
  _Incorreto._ O plano Enterprise Support fornece suporte por telefone, mas não é o plano mínimo.

- **B** Business  
  _Correto._ Você pode ligar ou conversar com o suporte técnico usando o plano Business Support ou Enterprise Support. O plano Business Support é o plano mínimo que fornece esse recurso.  
  [Saiba mais sobre os planos do AWS Support.](https://aws.amazon.com/pt/premiumsupport/plans/)

- **C** Desenvolvedor  
  _Incorreto._ O plano Developer Support permite somente a criação de tickets de suporte por e-mail e não fornece suporte por telefone.

- **D** Basic  
  _Incorreto._ O plano Basic Support fornece suporte ao cliente para problemas não técnicos, como aumentos nas cotas de serviço. No entanto, ele não fornece suporte técnico.

**Resposta correta:** B

---

11. **Um usuário implanta uma instância de banco de dados do Amazon RDS em várias zonas de disponibilidade.**

**Essa estratégia envolve qual pilar do AWS Well-Architected Framework?**

- **A** Eficiência de desempenho  
  _Incorreto._ O pilar de eficiência de desempenho inclui a capacidade de usar recursos computacionais com eficiência para atender aos requisitos do sistema e manter essa eficiência à medida que a demanda muda e as tecnologias evoluem. O uso de várias zonas de disponibilidade não aumenta a eficiência do desempenho.  
  [Saiba mais sobre a eficiência de desempenho.](https://docs.aws.amazon.com/wellarchitected/latest/framework/performance-efficiency.html)

- **B** Confiabilidade  
  _Correto._ O pilar de confiabilidade engloba a capacidade de uma carga de trabalho de executar sua função pretendida corretamente e de forma consistente quando é esperado. A implantação do Amazon RDS em várias zonas de disponibilidade é compatível com a meta de confiabilidade, pois reduz pontos únicos de falha.  
  [Saiba mais sobre confiabilidade.](https://docs.aws.amazon.com/wellarchitected/latest/framework/reliability.html)

- **C** Otimização de custos  
  _Incorreto._ O pilar Otimização de custos inclui a capacidade de executar sistemas para proporcionar valor comercial pelo menor preço. A confiabilidade é compatível com o uso de recursos em várias zonas de disponibilidade. O uso de várias zonas de disponibilidade para recursos aumentará o custo.  
  [Saiba mais sobre a otimização de custos.](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-optimization.html)

- **D** Segurança  
  _Incorreto._ O pilar Segurança refere-se à capacidade de proteger dados, sistemas e ativos para utilizar as tecnologias de nuvem a fim de melhorar sua segurança. O uso de várias zonas de disponibilidade para recursos não torna um aplicativo mais seguro.  
  [Saiba mais sobre segurança.](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html)

**Resposta correta:** B

---

12. **Cada departamento de uma empresa tem sua própria conta independente da AWS e seu próprio método de pagamento. A empresa precisa centralizar a governança departamental e consolidar pagamentos.**

**Como a empresa pode atingir esses objetivos usando serviços ou recursos da AWS?**

- **A** Usando o AWS Cloud Map em cada conta departamental.  
  _Incorreto._ O AWS Cloud Map cria e mantém um mapa de serviços de back-end. O AWS Cloud Map não lidará com a governança nem a consolidação de pagamentos.  
  [Saiba mais sobre o AWS Cloud Map.](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html)

- **B** Criando uma organização no AWS Organizations com todos os recursos habilitados em uma conta. Convidando todas as contas para ingressar na organização.  
  _Correto._ O Organizations fornece governança e faturamento centralizados para um ambiente da AWS, incluindo várias contas.  
  [Saiba mais sobre o Organizations.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html)

- **C** Usando o AWS Systems Manager OpsCenter.  
  _Incorreto._ O OpsCenter fornece um local central para os profissionais de TI visualizarem, investigarem e resolverem itens de trabalho operacionais. O OpsCenter não consolida o faturamento.  
  [Saiba mais sobre o OpsCenter.](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)

- **D** Usando a página AWS Cost and Usage Reports do Console do AWS Billing and Cost Management.  
  _Incorreto._ Esta solução consolida o faturamento em um relatório, mas funcionará apenas para as contas individuais (sem faturamento entre contas). Esta solução não aborda a governança central.  
  [Saiba mais sobre os relatórios de uso e custo.](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

**Resposta correta:** B

---

13. **Um usuário precisa descobrir, classificar e proteger automaticamente dados sigilosos armazenados no Amazon S3.**

**Qual serviço da AWS pode atender a esses requisitos?**

- **A** Amazon Inspector  
  _Incorreto._ O Amazon Inspector é um serviço automatizado de avaliação de segurança que ajuda a aprimorar a segurança e a conformidade dos aplicativos implantados em instâncias do EC2. O Amazon Inspector não executa a classificação de dados do S3 e a descoberta automática.  
  [Saiba mais sobre o Amazon Inspector.](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)

- **B** Amazon Macie  
  _Correto._ O Macie é um serviço automatizado de avaliação de segurança que ajuda a aprimorar a segurança e a conformidade dos aplicativos implantados na AWS.  
  [Saiba mais sobre o Macie.](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

- **C** Amazon GuardDuty  
  _Incorreto._ O GuardDuty é um serviço de detecção de ameaças que monitora continuamente atividades mal-intencionadas e comportamentos não autorizados para proteger cargas de trabalho e contas da AWS. O GuardDuty não executa a classificação de dados S3.  
  [Saiba mais sobre o GuardDuty.](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

- **D** AWS Secrets Manager  
  _Incorreto._ O Secrets Manager ajuda você a proteger os segredos necessários para acessar aplicativos, serviços e recursos de TI. O Secrets Manager não executa a classificação de dados do S3 e a descoberta automática.  
  [Saiba mais sobre o Secrets Manager.](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

**Resposta correta:** B

---

14. **Quais das funcionalidades são características do Amazon S3?** (Selecione **DUAS**.)

- **A** Um sistema de arquivos global  
  _Incorreto._ O Amazon S3 não é um sistema de arquivos global. O Amazon S3 é um serviço de armazenamento de objetos.  
  [Saiba mais sobre o Amazon S3.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

- **B** Um armazenamento de objetos  
  _Correto._ O Amazon S3 é um serviço de armazenamento de objetos.  
  [Saiba mais sobre o Amazon S3.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

- **C** Um armazenamento de arquivos local  
  _Incorreto._ O Amazon S3 não é um armazenamento de arquivos local. O Amazon S3 é um serviço de armazenamento de objetos.  
  [Saiba mais sobre o Amazon S3.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

- **D** Um sistema de arquivos de rede  
  _Incorreto._ O Amazon S3 não é um sistema de arquivos de rede. O Amazon S3 é um serviço de armazenamento de objetos.  
  [Saiba mais sobre o Amazon S3.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

- **E** Um sistema de armazenamento durável  
  _Correto._ O Amazon S3 é um serviço de armazenamento de objetos durável.  
  [Saiba mais sobre a proteção de dados no Amazon S3.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html)

**Resposta correta:** B, E

---

15. **Uma empresa exige uma conexão criptografada entre os servidores on-premises da empresa e a AWS. A conexão deve usar a conexão de internet existente da empresa.**

**Qual solução atenderá a esses requisitos?**

- **A** AWS Direct Connect  
  _Incorreto._ O Direct Connect vincula sua rede interna a um local do Direct Connect por meio de uma conexão de rede. Uma extremidade da conexão se conecta ao seu roteador on-premises. A outra extremidade se conecta a um roteador do Direct Connect. Com essa conexão, você pode ignorar os ISPs em seu caminho de rede. No entanto, a empresa deve usar uma conexão de internet existente nesse cenário.  
  [Saiba mais sobre o Direct Connect.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

- **B** Amazon Connect  
  _Incorreto._ O Amazon Connect é uma central de atendimento na nuvem para todos os tipos de canais. O Amazon Connect ajuda você a oferecer atendimento ao cliente a um custo baixo. O Amazon Connect usa um design para todos os tipos de canais para fornecer uma experiência perfeita em voz e bate-papo para seus clientes e agentes. O Amazon Connect não fornece uma conexão de rede.  
  [Saiba mais sobre o Amazon Connect.](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html)

- **C** Amazon CloudFront  
  _Incorreto._ O CloudFront é um serviço da web que acelera a distribuição de seu conteúdo web estático e dinâmico para seus usuários. O CloudFront distribui o conteúdo por meio de uma rede global de data centers denominados locais de borda. Quando um usuário solicita conteúdo disponibilizado com o CloudFront, ele é roteado para o local de borda com a menor latência. No entanto, o CloudFront não fornece uma conexão de rede.  
  [Saiba mais sobre o CloudFront.](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)

- **D** AWS Site-to-Site VPN  
  _Correto._ O Site-to-Site VPN cria um caminho de rede criptografado entre sua rede on-premises e sua rede na nuvem AWS. Essa conexão entre sua rede on-premises e sua rede na nuvem AWS usa a internet.  
  [Saiba mais sobre o Site-to-Site VPN.](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

**Resposta correta:** D


---

16. **Uma empresa precisa monitorar e receber alertas sobre eventos de login do Console de Gerenciamento da AWS que envolvem o usuário-raiz da conta da AWS.**

**Qual serviço da AWS a empresa pode usar para atender a esses requisitos?**

- **A** Amazon CloudWatch  
  _Correto._ O CloudWatch monitora os recursos da AWS e os aplicativos executados em tempo real na AWS. Você pode usar o CloudWatch com o AWS CloudTrail para monitorar e receber alertas sobre eventos de login do console que envolvem o usuário-raiz da conta da AWS.  
  [Saiba mais sobre o CloudWatch.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)  
  [Saiba mais sobre o CloudTrail.](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

- **B** AWS Config  
  _Incorreto._ Você pode usar o AWS Config para avaliar, auditar e verificar as configurações dos recursos da AWS. O AWS Config não pode alertá-lo sobre eventos de login no console que envolvam o usuário-raiz da conta da AWS.  
  [Saiba mais sobre o AWS Config.](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)

- **C** AWS Trusted Advisor  
  _Incorreto._ Você pode usar o Trusted Advisor para fornecer orientações em tempo real para ajudar a provisionar seus recursos de acordo com as práticas recomendadas da AWS. O Trusted Advisor não pode alertá-lo sobre eventos de login no console que envolvam o usuário-raiz da conta da AWS.  
  [Saiba mais sobre o Trusted Advisor.](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)

- **D** AWS Identity and Access Management (IAM)  
  _Incorreto._ Com o IAM, você pode gerenciar o acesso aos recursos e serviços da AWS com segurança. O IAM não pode alertá-lo sobre eventos de login no console que envolvam o usuário-raiz da conta da AWS.  
  [Saiba mais sobre o IAM.](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

**Resposta correta:** A

---

17. **Uma empresa quer estabelecer uma conexão consistente e privada do data center on-premises da empresa com a nuvem AWS.**

**Qual serviço da AWS atenderá a esses requisitos?**

- **A** AWS Client VPN  
  _Incorreto._ O Client VPN é um serviço gerenciado de VPN baseado no cliente que permite acessar de forma segura seus recursos da AWS e os recursos na sua rede on-premises. Com o Client VPN, você pode acessar seus recursos de qualquer local usando um cliente de VPN com base no OpenVPN. Você usa o Client VPN para conectar notebooks individuais à AWS, não um data center inteiro.  
  [Saiba mais sobre o Client VPN.](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

- **B** Amazon Connect  
  _Incorreto._ O Amazon Connect é uma central de atendimento na nuvem para todos os tipos de canais, que ajuda a oferecer um atendimento superior a um custo menor. O Amazon Connect oferece uma experiência perfeita em voz e bate-papo para seus clientes e agentes. O Amazon Connect não é um serviço que conecta uma rede on-premises à AWS.  
  [Saiba mais sobre o Amazon Connect.](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html)

- **C** AWS Direct Connect  
  _Correto._ O Direct Connect vincula sua rede interna a um local do Direct Connect por meio de um cabo de fibra óptica Ethernet padrão. Uma extremidade do cabo se conecta ao seu roteador. A outra extremidade do cabo se conecta a um roteador do Direct Connect. O AWS Direct Connect é consistente e privado porque sua empresa é a única usuária do cabo.  
  [Saiba mais sobre o Direct Connect.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

- **D** AWS Site-to-Site VPN  
  _Incorreto._ O Site-to-Site VPN cria um caminho de rede criptografado entre sua rede on-premises e sua rede na nuvem AWS. Essa conexão usa a internet, então você não pode esperar consistência. Embora o tráfego seja criptografado, a conexão não é privada porque a internet é um recurso compartilhado.  
  [Saiba mais sobre o Site-to-Site VPN.](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)

**Resposta correta:** C


---

18. **Quais são as vantagens de implantar um aplicativo com instâncias do Amazon EC2 em várias zonas de disponibilidade?** (Selecione **DUAS**.)

- **A** Prevenção de um único ponto de falha  
  _Correto._ A implantação das instâncias do EC2 em várias zonas de disponibilidade evita um único ponto de falha. As zonas de disponibilidade são projetadas para redundância física e para fornecer resiliência com desempenho ininterrupto.  
  [Saiba mais sobre as zonas de disponibilidade.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

- **B** Redução dos custos operacionais do aplicativo  
  _Incorreto._ Várias zonas de disponibilidade evitam pontos únicos de falha. Como resultado, a disponibilidade geral do aplicativo melhora. Várias zonas de disponibilidade não reduzirão os custos operacionais do aplicativo.

- **C** O aplicativo pode atender aos usuários entre regiões com baixa latência  
  _Incorreto._ A melhor opção para atender usuários com baixa latência entre regiões é executar outra instância do EC2 na segunda região mais próxima da localização do usuário.

- **D** Aumento da disponibilidade do aplicativo  
  _Correto._ Se você hospedar todas as suas instâncias em um único local afetado por uma falha, nenhuma delas ficará disponível. As zonas de disponibilidade são projetadas para redundância física e para fornecer resiliência com desempenho ininterrupto.  
  [Saiba mais sobre as zonas de disponibilidade.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

- **E** Aumento da carga do aplicativo  
  _Incorreto._ Várias zonas de disponibilidade evitarão pontos únicos de falha. Como resultado, a disponibilidade geral do aplicativo melhorará. No entanto, duas instâncias do EC2 executadas na mesma zona de disponibilidade ou em zonas de disponibilidade diferentes não alterarão a carga geral do aplicativo.

**Resposta correta:** A, D

---

19. **Quais são os benefícios de usar a Nuvem AWS para empresas com clientes em muitos países ao redor do mundo?** (Selecione **DUAS**.)

- **A** As empresas podem implantar aplicativos em várias regiões AWS para reduzir a latência.  
  _Correto._ O uso de regiões em todo o mundo melhorará o desempenho global de um aplicativo e reduzirá a latência para os usuários.  
  [Saiba mais sobre a infraestrutura global da AWS.](https://aws.amazon.com/about-aws/global-infrastructure/)  
  [Saiba mais sobre as regiões AWS.](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html)

- **B** O Amazon Translate traduz automaticamente interfaces de sites de terceiros em vários idiomas.  
  _Incorreto._ O Amazon Translate não fornece tradução automática de interfaces de sites de terceiros.  
  [Saiba mais sobre o Amazon Translate.](https://docs.aws.amazon.com/translate/latest/dg/how-it-works.html)

- **C** O Amazon CloudFront tem vários locais de borda em todo o mundo para reduzir a latência.  
  _Correto._ O CloudFront é um serviço da rede de entrega de conteúdo (CDN) global que envia dados, vídeos, aplicativos e APIs aos visualizadores, de forma segura, com baixa latência e alta velocidade de transferência.  
  [Saiba mais sobre como o CloudFront fornece conteúdo.](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html)  
  [Saiba mais sobre a rede de borda do CloudFront.](https://aws.amazon.com/cloudfront/features/)

- **D** O Amazon Comprehend permite que os usuários criem aplicativos que podem responder às solicitações de usuários em vários idiomas.  
  _Incorreto._ O Amazon Comprehend é um serviço de processamento de linguagem natural (NLP) que usa machine learning para encontrar insights e inter-relações no texto. Amazon Comprehend não traduz texto.  
  [Saiba mais sobre o Amazon Comprehend.](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)

- **E** O Elastic Load Balancing pode distribuir o tráfego na Web de aplicativos para várias regiões AWS em todo o mundo, o que reduz a latência.  
  _Incorreto._ Um balanceador de carga aceita o tráfego de entrada de clientes e roteia solicitações para seus destinos registrados (como instâncias do EC2) em uma ou mais zonas de disponibilidade. No entanto, ele não aceita destinos entre regiões.  
  [Saiba mais sobre o Elastic Load Balancing.](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)

**Resposta correta:** A, C

---

20. **Uma empresa está transferindo todas as suas atividades de desenvolvimento para a AWS. A empresa quer uma solução para armazenar e gerenciar o código-fonte de seus desenvolvedores.**

**Qual serviço de codificação da AWS atenderá a esse requisito?**

- **A** AWS CodeArtifact  
  _Incorreto._ O CodeArtifact é um serviço gerenciado de repositório de artefatos que armazena e compartilha software pronto para implantação. O CodeArtifact não é um serviço de gerenciamento de código-fonte.  
  [Saiba mais sobre o CodeArtifact.](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html)

- **B** AWS CodeBuild  
  _Incorreto._ O CodeBuild é um serviço que ajuda os usuários a compilar automaticamente o código-fonte, executar testes de unidade e produzir pacotes de software prontos para implantação. O CodeBuild não é um serviço de gerenciamento de código.  
  [Saiba mais sobre o CodeBuild.](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)

- **C** AWS CodePipeline  
  _Incorreto._ O CodePipeline é um serviço que gerencia a movimentação do código entre os serviços individuais. O CodePipeline não é um serviço de armazenamento de código-fonte.  
  [Saiba mais sobre o CodePipeline.](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)

- **D** AWS CodeCommit  
  _Correto._ O CodeCommit é um serviço de controle de versão do código-fonte. O CodeCommit ajuda os usuários a armazenar e gerenciar o código-fonte dos desenvolvedores na AWS.  
  [Saiba mais sobre o CodeCommit.](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)

**Resposta correta:** D