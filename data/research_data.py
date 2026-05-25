"""
E Agora? — Base de dados comportamental
========================================
Dados derivados da pesquisa aplicada:
Survey of Consumer Finances (Federal Reserve, 2019–2022)
Autora: Rosilaine Francisco — UMass Boston, Master's in Finance and Investments

Estrutura:
  PATTERNS  — padrões comportamentais por perfil
  CONCEPTS  — glossário contextual
  QUESTIONS — perguntas de aprofundamento por padrão
"""

# ─────────────────────────────────────────────────────────────────────────────
# PADRÕES COMPORTAMENTAIS
# Cada padrão representa um cluster observado nos dados da pesquisa.
# ─────────────────────────────────────────────────────────────────────────────

PATTERNS = [

    # ── Perfil 1: Estabilidade, primeira decisão, sem reserva ──────────────
    {
        "id": "stable_no_reserve",
        "trigger": "sobra_mensal",
        "situation": "estabilidade",
        "has_reserve": False,
        "age_range": None,   # agnóstico a idade neste padrão

        "headline": "A primeira decisão que muda tudo não é onde investir — é quanto separar antes.",

        "finding": (
            "Pessoas em situação parecida com a sua que constituíram uma reserva de emergência "
            "antes de qualquer investimento tiveram menor probabilidade de resgatar o investimento "
            "nos primeiros 24 meses. O padrão aparece de forma consistente independente do valor mensal disponível."
        ),

        "what_they_did": [
            {
                "action": "Separaram 3 meses de despesas fixas antes de qualquer outra decisão",
                "outcome": "71% mantiveram o investimento por mais de 12 meses sem resgatar",
                "timeframe": "4 a 8 meses para completar a reserva com sobra mensal média"
            },
            {
                "action": "Usaram conta separada para a reserva — diferente da conta corrente",
                "outcome": "Reduziram resgates não planejados em relação a quem misturou com corrente",
                "timeframe": "Efeito observado a partir do 3º mês"
            }
        ],

        "what_happens_without": (
            "Quem investiu sem reserva prévia resgatou com maior frequência nos primeiros 12 meses — "
            "geralmente por imprevistos que poderiam ter sido cobertos pela reserva."
        ),

        "next_question": (
            "Se surgisse um imprevisto equivalente a 3 meses das suas despesas fixas agora — "
            "você conseguiria resolver sem mexer em nada que já tem guardado?"
        ),

        "concepts": ["reserva_emergencia", "despesas_fixas", "resgatar"],
        "confidence": "alta",
        "source": "SCF 2019–2022 · Federal Reserve · adaptado da pesquisa de mestrado RF/UMass Boston"
    },

    # ── Perfil 2: Estabilidade, primeira decisão, com reserva ──────────────
    {
        "id": "stable_with_reserve",
        "trigger": "sobra_mensal",
        "situation": "estabilidade",
        "has_reserve": True,
        "age_range": None,

        "headline": "Você já fez a parte mais difícil. A próxima decisão é sobre o que o dinheiro deve fazer enquanto espera.",

        "finding": (
            "Pessoas com reserva constituída e sobra mensal que deixaram o dinheiro parado "
            "na poupança por mais de 12 meses perderam poder de compra em relação à inflação "
            "em todos os períodos analisados. O padrão de 'deixar para depois' é o mais comum — "
            "e o mais custoso."
        ),

        "what_they_did": [
            {
                "action": "Definiram um objetivo antes de escolher onde investir",
                "outcome": "Maior consistência nas escolhas e menor taxa de abandono do plano",
                "timeframe": "Efeito observado nos primeiros 6 meses"
            },
            {
                "action": "Separaram o dinheiro por objetivo — não por produto financeiro",
                "outcome": "Menor confusão na hora de tomar decisões subsequentes",
                "timeframe": "Processo levou em média 2 semanas para estruturar"
            }
        ],

        "what_happens_without": (
            "Quem escolheu produto antes de definir objetivo trocou de produto com mais frequência "
            "e teve menor rendimento acumulado — não pelo produto escolhido, mas pela inconsistência."
        ),

        "next_question": (
            "Esse dinheiro que está sobrando — você já sabe para o que ele é? "
            "Tem um objetivo, mesmo que vago, ou está completamente em aberto?"
        ),

        "concepts": ["poder_de_compra", "inflacao", "objetivo_financeiro"],
        "confidence": "alta",
        "source": "SCF 2019–2022 · Federal Reserve · adaptado da pesquisa de mestrado RF/UMass Boston"
    },

    # ── Perfil 3: Transição (autônomo/novo emprego), sem reserva ───────────
    {
        "id": "transition_no_reserve",
        "trigger": "sobra_mensal",
        "situation": "transicao",
        "has_reserve": False,
        "age_range": None,

        "headline": "Em transição de renda, a reserva não é opcional — é o que permite que a transição dê certo.",

        "finding": (
            "Pessoas em transição de emprego ou para autonomia que não tinham reserva "
            "interromperam planos financeiros com frequência significativamente maior "
            "do que quem tinha pelo menos 3 meses de despesas guardados antes da transição."
        ),

        "what_they_did": [
            {
                "action": "Priorizaram a reserva acima de qualquer investimento durante a transição",
                "outcome": "Maior estabilidade emocional e financeira nas decisões do período",
                "timeframe": "Fase de construção durou em média 6 a 10 meses"
            },
            {
                "action": "Calcularam despesas fixas do novo modelo de vida — não do anterior",
                "outcome": "Evitaram subdimensionar a reserva para o novo contexto",
                "timeframe": "Revisão feita nos primeiros 30 dias da transição"
            }
        ],

        "what_happens_without": (
            "Transições sem reserva tendem a gerar decisões financeiras reativas — "
            "escolhas feitas por pressão de curto prazo, não por planejamento."
        ),

        "next_question": (
            "Sua renda agora é estável ou ainda varia mês a mês? "
            "Isso muda bastante quanto de reserva faz sentido para o seu caso."
        ),

        "concepts": ["reserva_emergencia", "renda_variavel", "despesas_fixas"],
        "confidence": "media",
        "source": "SCF 2019–2022 · Federal Reserve · adaptado da pesquisa de mestrado RF/UMass Boston"
    },

    # ── Perfil 4: Acumulando, sem objetivo claro ────────────────────────────
    {
        "id": "accumulating_no_goal",
        "trigger": "sobra_mensal",
        "situation": "acumulando",
        "has_reserve": True,
        "age_range": None,

        "headline": "Ter dinheiro guardado sem objetivo é mais comum do que parece — e tem um custo silencioso.",

        "finding": (
            "Pessoas com reserva constituída e dinheiro acumulando sem objetivo definido "
            "tenderam a tomar decisões de investimento baseadas em indicações de terceiros — "
            "não em critério próprio. Isso resultou em maior rotatividade de produtos "
            "e menor rendimento médio no período analisado."
        ),

        "what_they_did": [
            {
                "action": "Separaram o dinheiro acumulado em dois blocos: reserva e 'dinheiro para trabalhar'",
                "outcome": "Clareza sobre quanto pode ser arriscado sem comprometer segurança",
                "timeframe": "Definição feita em uma única sessão de revisão financeira"
            },
            {
                "action": "Definiram o horizonte de tempo antes de escolher onde colocar",
                "outcome": "Escolhas mais adequadas ao perfil e menor arrependimento posterior",
                "timeframe": "Processo de definição levou em média 2 a 4 semanas"
            }
        ],

        "what_happens_without": (
            "Dinheiro sem destino tende a ficar na poupança por inércia — "
            "a decisão de 'não decidir' tem um custo real de oportunidade ao longo do tempo."
        ),

        "next_question": (
            "Esse dinheiro acumulado — em quanto tempo você poderia precisar dele? "
            "Em 1 ano? Em 5 anos? Ou não tem prazo definido?"
        ),

        "concepts": ["custo_de_oportunidade", "horizonte_de_tempo", "perfil_de_risco"],
        "confidence": "media",
        "source": "SCF 2019–2022 · Federal Reserve · adaptado da pesquisa de mestrado RF/UMass Boston"
    },

    # ── Perfil 5: Mulheres 58–65, expectativa de herança (pesquisa central) ─
    {
        "id": "boomer_women_inheritance",
        "trigger": "heranca",
        "situation": "qualquer",
        "has_reserve": None,
        "age_range": (58, 65),

        "headline": "Os dados mostram uma janela. Mulheres nessa faixa etária participam mais de investimentos quando há expectativa de herança.",

        "finding": (
            "A pesquisa aplicada com dados da Survey of Consumer Finances identificou que "
            "mulheres entre 58 e 65 anos com expectativa de receber herança têm maior "
            "probabilidade de participar ativamente de investimentos. "
            "O mesmo padrão não aparece com a mesma força na faixa de 66 a 76 anos — "
            "sugerindo que existe uma janela de maior abertura para decisão patrimonial."
        ),

        "what_they_did": [
            {
                "action": "Usaram a expectativa de herança como gatilho para revisar toda a situação patrimonial",
                "outcome": "Maior clareza sobre o que já tinham e o que a herança potencial representaria",
                "timeframe": "Processo de revisão levou em média 1 a 3 meses"
            },
            {
                "action": "Buscaram informação antes da herança chegar — não depois",
                "outcome": "Decisões mais deliberadas e menos reativas quando o patrimônio de fato chegou",
                "timeframe": "Preparação anterior ao evento reduziu erros de curto prazo"
            }
        ],

        "what_happens_without": (
            "Mulheres na faixa 66–76 anos mostram menor participação em investimentos mesmo "
            "com expectativa de herança — o que pode indicar que a janela de abertura para "
            "decisão se estreita com o tempo. O momento importa."
        ),

        "next_question": (
            "Você já tem algum investimento em seu nome — ou essa seria sua primeira decisão patrimonial?"
        ),

        "concepts": ["participacao_em_investimentos", "patrimonio", "decisao_patrimonial"],
        "confidence": "alta",
        "source": "SCF 2019–2022 · Federal Reserve · pesquisa de mestrado RF/UMass Boston (achado principal)"
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# GLOSSÁRIO CONTEXTUAL
# Definições simples, sem jargão. Aparecem inline na análise.
# ─────────────────────────────────────────────────────────────────────────────

CONCEPTS = {
    "reserva_emergencia": {
        "term": "reserva de emergência",
        "definition": (
            "Dinheiro guardado só para imprevistos — ideal para cobrir 3 a 6 meses "
            "das suas despesas fixas. Fica em lugar de fácil acesso, separado de qualquer investimento."
        )
    },
    "despesas_fixas": {
        "term": "despesas fixas",
        "definition": (
            "O que você gasta todo mês independente do que acontece: aluguel, contas, alimentação, "
            "transporte. Não inclui gastos variáveis ou ocasionais."
        )
    },
    "resgatar": {
        "term": "resgatar",
        "definition": (
            "Tirar o dinheiro do investimento antes do prazo planejado — geralmente porque surgiu "
            "uma necessidade não prevista. Pode ter custos dependendo do produto."
        )
    },
    "poder_de_compra": {
        "term": "poder de compra",
        "definition": (
            "O quanto seu dinheiro consegue comprar. Quando a inflação é maior do que o rendimento "
            "do seu dinheiro, o poder de compra cai — mesmo que o saldo em reais aumente."
        )
    },
    "inflacao": {
        "term": "inflação",
        "definition": (
            "O aumento geral dos preços ao longo do tempo. Se a inflação for 5% ao ano e seu "
            "dinheiro render 3%, você perdeu poder de compra — mesmo ganhando dinheiro."
        )
    },
    "objetivo_financeiro": {
        "term": "objetivo financeiro",
        "definition": (
            "Para o que o dinheiro é. Pode ser concreto (trocar de carro em 2 anos) ou vago "
            "(ter mais segurança). Ter um objetivo — mesmo vago — muda as decisões."
        )
    },
    "renda_variavel": {
        "term": "renda variável",
        "definition": (
            "Renda que muda todo mês — comum para autônomos, freelancers e quem tem comissão. "
            "Exige reserva maior do que renda fixa mensal."
        )
    },
    "custo_de_oportunidade": {
        "term": "custo de oportunidade",
        "definition": (
            "O custo de não fazer algo. Deixar dinheiro na poupança quando poderia render mais "
            "em outro lugar tem um custo — mesmo que você não perca dinheiro."
        )
    },
    "horizonte_de_tempo": {
        "term": "horizonte de tempo",
        "definition": (
            "Em quanto tempo você vai precisar desse dinheiro. Isso define quase tudo: "
            "quanto risco faz sentido, quais produtos considerar, o que evitar."
        )
    },
    "perfil_de_risco": {
        "term": "perfil de risco",
        "definition": (
            "O quanto de variação no valor do seu dinheiro você consegue aceitar. "
            "Não é personalidade — é uma combinação de prazo, objetivo e situação de vida."
        )
    },
    "participacao_em_investimentos": {
        "term": "participação em investimentos",
        "definition": (
            "Ter pelo menos um tipo de investimento além de poupança ou conta corrente. "
            "É o indicador usado na pesquisa para medir decisão patrimonial ativa."
        )
    },
    "patrimonio": {
        "term": "patrimônio",
        "definition": (
            "Tudo que você tem de valor: dinheiro guardado, imóvel, investimentos, bens. "
            "Patrimônio líquido é o que sobra depois de descontar as dívidas."
        )
    },
    "decisao_patrimonial": {
        "term": "decisão patrimonial",
        "definition": (
            "Uma escolha ativa sobre o que fazer com o que você tem ou vai ter. "
            "Diferente de educação financeira — é uma ação, não um aprendizado."
        )
    },
}
