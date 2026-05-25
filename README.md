# e agora?
**Plataforma de inteligência para decisão patrimonial**

Você já pagou o que tinha para pagar. Sobrou alguma coisa. E agora?

A plataforma mostra o que pessoas em situações parecidas fizeram — baseado em dados reais. Você decide.

---

## Origem

Desenvolvida a partir da pesquisa aplicada em Finance and Investments (UMass Boston) usando dados da **Survey of Consumer Finances** do Federal Reserve americano.

A pesquisa identificou padrões de comportamento patrimonial em mulheres Baby Boomers — especialmente a relação entre expectativa de herança e participação em investimentos na faixa de 58–65 anos.

Esta plataforma generaliza essa lógica para outros gatilhos patrimoniais — começando pelo mais comum: **dinheiro sobrando sem destino**.

---

## Estrutura

```
eanow/
├── core/
│   └── matching_engine.py   # Motor de matching — lógica central
├── data/
│   └── research_data.py     # Base de padrões comportamentais e glossário
├── api/
│   └── app.py               # API Flask
├── web/
│   └── index.html           # Interface web
├── requirements.txt
└── README.md
```

---

## Como rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Testar o motor de matching diretamente
PYTHONPATH=. python core/matching_engine.py

# Rodar a aplicação web
PYTHONPATH=. python api/app.py
# Acesse: http://localhost:5050
```

---

## Lógica do motor

Mesmo princípio do scanner de opções — só que o domínio é comportamento patrimonial:

| Scanner RBC | Plataforma e agora? |
|---|---|
| IV Rank + tendência | gatilho + situação + reserva |
| `definir_estrategia()` | `MatchingEngine.match()` |
| PUT SPREAD / CALL SPREAD | padrão comportamental |
| Regras de saída | próxima pergunta |
| Risk Gate | confiança do match |

---

## Roadmap

- [ ] MVP: gatilho `sobra_mensal` com 4 padrões
- [ ] Validação com usuários reais (10 entrevistas)
- [ ] Base de dados brasileira equivalente à SCF
- [ ] Módulo herança (pesquisa central já validada)
- [ ] Módulo aposentadoria
- [ ] Módulo filho nascendo

---

## Pesquisa base

**Autora:** Rosilaine Francisco  
**Instituição:** University of Massachusetts Boston — Master's in Finance and Investments  
**Fonte de dados:** Survey of Consumer Finances, Federal Reserve (2019–2022)  
**Reconhecimentos:** Beacon Graduate Student Leadership Award (UMass Boston) · CFA Program Student Scholarship (CFA Institute)

---

*Dados educacionais. Não são recomendações de investimento.*
