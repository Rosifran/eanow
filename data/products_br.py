"""
E Agora? — Mapa de Produtos Financeiros Brasileiros
=====================================================
Base de dados de produtos por perfil comportamental.
Linguagem humana. Sem jargão. Sem recomendação.

A plataforma mostra. A usuária decide.

Autora da pesquisa: Rosilaine Francisco — UMass Boston
"""

# ─────────────────────────────────────────────────────────────────────────────
# PRODUTOS FINANCEIROS BRASILEIROS
# Cada produto tem: o que é, como funciona, para quem faz sentido,
# o que considerar, onde encontrar e qual perfil se beneficia mais.
# ─────────────────────────────────────────────────────────────────────────────

PRODUCTS = {

    # ── RENDA FIXA ────────────────────────────────────────────────────────────

    "tesouro_selic": {
        "id": "tesouro_selic",
        "name": "Tesouro Selic",
        "category": "renda_fixa",
        "category_label": "Renda Fixa",
        "risk": "muito_baixo",
        "risk_label": "Muito baixo",
        "liquidity": "alta",
        "liquidity_label": "Alta — resgata quando quiser",
        "minimum": 100,
        "minimum_label": "A partir de R$ 100",

        "what_is": (
            "É um título emitido pelo governo federal brasileiro. "
            "Quando você compra, está emprestando dinheiro ao governo — "
            "e ele te paga de volta com juros."
        ),
        "how_it_works": (
            "Rende de acordo com a taxa Selic — a taxa básica de juros do Brasil. "
            "Se a Selic está em 13% ao ano, seu dinheiro rende próximo disso. "
            "Você pode resgatar a qualquer momento sem perder o rendimento acumulado."
        ),
        "makes_sense_when": (
            "Você quer guardar dinheiro com segurança e poder resgatar quando precisar. "
            "É o produto mais indicado para reserva de emergência ou dinheiro "
            "que você pode precisar no curto prazo."
        ),
        "watch_out": (
            "Rende bem quando a Selic está alta. Quando cai, o rendimento cai junto. "
            "Há cobrança de IR sobre o rendimento — alíquota diminui quanto mais tempo você deixa."
        ),
        "where_to_find": "Tesouro Direto (tesourodireto.gov.br) ou qualquer corretora.",
        "profiles": ["preserver", "follower"],
        "goals": ["reserva_emergencia", "seguranca", "curto_prazo"],
    },

    "tesouro_ipca": {
        "id": "tesouro_ipca",
        "name": "Tesouro IPCA+",
        "category": "renda_fixa",
        "category_label": "Renda Fixa",
        "risk": "baixo",
        "risk_label": "Baixo",
        "liquidity": "media",
        "liquidity_label": "Média — melhor manter até o vencimento",
        "minimum": 100,
        "minimum_label": "A partir de R$ 100",

        "what_is": (
            "Também é um título do governo. A diferença é que rende a inflação "
            "(IPCA) mais uma taxa fixa. Protege seu dinheiro da inflação e ainda dá um ganho real."
        ),
        "how_it_works": (
            "Se o IPCA for 5% e a taxa contratada for 6%, você ganha 11% no ano. "
            "Quanto mais longo o prazo, maior costuma ser a taxa fixa oferecida. "
            "Tem vencimentos de 2 a 35 anos."
        ),
        "makes_sense_when": (
            "Você tem um objetivo de médio ou longo prazo — aposentadoria, "
            "compra de imóvel, independência financeira. Quer garantir que seu "
            "dinheiro vai crescer acima da inflação."
        ),
        "watch_out": (
            "Se resgatar antes do vencimento, o valor pode ser menor do que o investido "
            "dependendo do momento do mercado. É para dinheiro que você não vai precisar no curto prazo."
        ),
        "where_to_find": "Tesouro Direto (tesourodireto.gov.br) ou qualquer corretora.",
        "profiles": ["follower", "independent", "accumulator"],
        "goals": ["aposentadoria", "independencia_financeira", "medio_prazo", "longo_prazo"],
    },

    "cdb": {
        "id": "cdb",
        "name": "CDB",
        "category": "renda_fixa",
        "category_label": "Renda Fixa",
        "risk": "muito_baixo",
        "risk_label": "Muito baixo (coberto pelo FGC até R$ 250 mil)",
        "liquidity": "variavel",
        "liquidity_label": "Varia — alguns diários, outros com prazo",
        "minimum": 1,
        "minimum_label": "A partir de R$ 1 (em alguns bancos)",

        "what_is": (
            "Certificado de Depósito Bancário. Você empresta dinheiro para um banco "
            "e ele te paga de volta com juros. "
            "É a versão bancária do Tesouro — em vez do governo, é o banco que deve para você."
        ),
        "how_it_works": (
            "Rende um percentual do CDI (que anda junto com a Selic). "
            "Um CDB que paga 100% do CDI rende o equivalente à taxa básica de juros. "
            "Bancos menores costumam pagar mais — 110%, 120% do CDI — para atrair clientes."
        ),
        "makes_sense_when": (
            "Você quer algo simples, seguro, com rentabilidade previsível. "
            "CDBs diários são ótimos para reserva de emergência. "
            "CDBs com prazo fixo rendem mais, mas o dinheiro fica travado."
        ),
        "watch_out": (
            "Verifique a liquidez antes de aplicar. Alguns CDBs só pagam no vencimento. "
            "O FGC garante até R$ 250 mil por CPF por instituição — distribua se tiver mais."
        ),
        "where_to_find": "Bancos e corretoras. Nubank, Inter, XP, BTG, Rico, entre outros.",
        "profiles": ["preserver", "follower", "independent"],
        "goals": ["reserva_emergencia", "seguranca", "curto_prazo", "medio_prazo"],
    },

    "lci_lca": {
        "id": "lci_lca",
        "name": "LCI e LCA",
        "category": "renda_fixa",
        "category_label": "Renda Fixa",
        "risk": "muito_baixo",
        "risk_label": "Muito baixo (coberto pelo FGC até R$ 250 mil)",
        "liquidity": "baixa",
        "liquidity_label": "Baixa — prazo mínimo de 90 dias",
        "minimum": 1000,
        "minimum_label": "A partir de R$ 1.000 (varia por banco)",

        "what_is": (
            "Letras de Crédito Imobiliário (LCI) e do Agronegócio (LCA). "
            "Funcionam como CDB — você empresta para o banco — mas são isentas de IR "
            "para pessoa física. Isso faz toda a diferença no rendimento líquido."
        ),
        "how_it_works": (
            "Por serem isentas de imposto de renda, mesmo pagando menos que um CDB, "
            "o rendimento líquido pode ser equivalente ou maior. "
            "Uma LCI que paga 90% do CDI pode valer mais do que um CDB que paga 100% do CDI."
        ),
        "makes_sense_when": (
            "Você não vai precisar do dinheiro no curto prazo e quer maximizar "
            "o rendimento líquido. Ótimo para objetivos de médio prazo — 1 a 3 anos."
        ),
        "watch_out": (
            "Prazo mínimo de carência — não pode resgatar antes. "
            "Verifique sempre o rendimento líquido, não o bruto. "
            "Coberto pelo FGC até R$ 250 mil por CPF por instituição."
        ),
        "where_to_find": "Corretoras e bancos. XP, BTG, Nubank, Inter, entre outros.",
        "profiles": ["follower", "independent"],
        "goals": ["medio_prazo", "otimizacao_rendimento"],
    },

    # ── FUNDOS ────────────────────────────────────────────────────────────────

    "fundo_renda_fixa": {
        "id": "fundo_renda_fixa",
        "name": "Fundo de Renda Fixa",
        "category": "fundos",
        "category_label": "Fundos",
        "risk": "baixo",
        "risk_label": "Baixo",
        "liquidity": "media",
        "liquidity_label": "Média — resgate em D+1 a D+30",
        "minimum": 100,
        "minimum_label": "A partir de R$ 100 (varia por fundo)",

        "what_is": (
            "Um fundo onde vários investidores colocam dinheiro junto e um gestor "
            "profissional decide onde investir — sempre em produtos de renda fixa. "
            "Você compra cotas do fundo, não o produto diretamente."
        ),
        "how_it_works": (
            "O gestor compra títulos públicos, CDBs, LCIs e outros produtos de renda fixa "
            "com o dinheiro do fundo. Você se beneficia da diversificação e da gestão profissional "
            "sem precisar escolher cada produto."
        ),
        "makes_sense_when": (
            "Você quer diversificação automática sem precisar acompanhar cada título. "
            "Boa opção para quem está começando e quer simplicidade."
        ),
        "watch_out": (
            "Taxa de administração come o rendimento — compare fundos. "
            "Alguns cobram taxa de performance. Verifique o come-cotas (antecipação de IR) "
            "que ocorre em maio e novembro."
        ),
        "where_to_find": "Bancos e corretoras. Compare taxas antes de escolher.",
        "profiles": ["preserver", "follower"],
        "goals": ["simplicidade", "diversificacao", "curto_prazo", "medio_prazo"],
    },

    "fundo_multimercado": {
        "id": "fundo_multimercado",
        "name": "Fundo Multimercado",
        "category": "fundos",
        "category_label": "Fundos",
        "risk": "medio",
        "risk_label": "Médio — varia muito entre fundos",
        "liquidity": "media",
        "liquidity_label": "Média — resgate em D+1 a D+30",
        "minimum": 500,
        "minimum_label": "A partir de R$ 500 (varia por fundo)",

        "what_is": (
            "Um fundo que investe em vários tipos de ativos ao mesmo tempo — "
            "renda fixa, ações, câmbio, derivativos. O gestor tem liberdade para "
            "montar a carteira que achar melhor dentro das regras do fundo."
        ),
        "how_it_works": (
            "Dependendo da estratégia do fundo, pode render muito mais que a renda fixa "
            "em períodos bons — mas também pode perder em períodos ruins. "
            "O histórico do gestor importa muito nessa escolha."
        ),
        "makes_sense_when": (
            "Você quer potencial de retorno maior que a renda fixa simples, "
            "aceita alguma variação no saldo e prefere deixar nas mãos de um gestor "
            "em vez de escolher ativos sozinha."
        ),
        "watch_out": (
            "Rentabilidade passada não garante resultado futuro. "
            "Pesquise o histórico do gestor em diferentes cenários de mercado. "
            "Taxas de administração e performance podem ser altas."
        ),
        "where_to_find": "Corretoras. XP, BTG, Nu Invest, entre outros.",
        "profiles": ["independent", "accumulator"],
        "goals": ["crescimento", "diversificacao", "medio_prazo", "longo_prazo"],
    },

    # ── RENDA VARIÁVEL ────────────────────────────────────────────────────────

    "fiis": {
        "id": "fiis",
        "name": "Fundos Imobiliários (FIIs)",
        "category": "renda_variavel",
        "category_label": "Renda Variável",
        "risk": "medio",
        "risk_label": "Médio",
        "liquidity": "alta",
        "liquidity_label": "Alta — negocia na bolsa todos os dias",
        "minimum": 10,
        "minimum_label": "A partir de R$ 10 (uma cota)",

        "what_is": (
            "Você investe em imóveis sem precisar comprar um imóvel. "
            "O fundo possui shoppings, galpões, escritórios ou imóveis residenciais "
            "e distribui o aluguel entre os cotistas todo mês."
        ),
        "how_it_works": (
            "Você compra cotas na bolsa como se fossem ações. "
            "Todo mês recebe uma parte do aluguel dos imóveis — isento de IR para pessoa física. "
            "O valor da cota também pode subir ou cair conforme o mercado."
        ),
        "makes_sense_when": (
            "Você quer renda passiva mensal, tem interesse no mercado imobiliário "
            "mas não quer a dor de cabeça de ser proprietária. "
            "Bom para quem pensa em complementar renda no futuro."
        ),
        "watch_out": (
            "O valor da cota oscila — pode cair. Os dividendos não são garantidos. "
            "Pesquise o portfólio do fundo: quais imóveis tem, taxa de vacância, histórico de pagamento."
        ),
        "where_to_find": "Qualquer corretora com acesso à B3. XP, Nu Invest, Rico, Clear, entre outros.",
        "profiles": ["independent", "accumulator"],
        "goals": ["renda_passiva", "independencia_financeira", "longo_prazo"],
    },

    "etf_brasil": {
        "id": "etf_brasil",
        "name": "ETF Brasileiro",
        "category": "renda_variavel",
        "category_label": "Renda Variável",
        "risk": "alto",
        "risk_label": "Alto — acompanha o mercado, sobe e desce",
        "liquidity": "alta",
        "liquidity_label": "Alta — negocia na bolsa todos os dias",
        "minimum": 10,
        "minimum_label": "A partir de R$ 10 (uma cota)",

        "what_is": (
            "Um fundo que replica um índice — como o Ibovespa ou o S&P 500. "
            "Em vez de escolher ações individuais, você investe no índice inteiro. "
            "É a forma mais simples de entrar na bolsa."
        ),
        "how_it_works": (
            "Quando o Ibovespa sobe, sua cota sobe. Quando cai, cai junto. "
            "Taxa de administração muito baixa — alguns custam 0,05% ao ano. "
            "Não precisa escolher empresa por empresa."
        ),
        "makes_sense_when": (
            "Você quer exposição à bolsa sem precisar analisar empresas. "
            "Estratégia de longo prazo — quanto mais tempo, maior a probabilidade de ganho. "
            "Boa para quem quer começar simples na renda variável."
        ),
        "watch_out": (
            "No curto prazo pode perder muito. É para dinheiro que você não vai precisar "
            "em pelo menos 5 anos. Não olhe o saldo todo dia."
        ),
        "where_to_find": "Qualquer corretora. BOVA11 (Ibovespa), IVVB11 (S&P 500), entre outros.",
        "profiles": ["accumulator"],
        "goals": ["crescimento", "longo_prazo", "independencia_financeira"],
    },

    "acoes": {
        "id": "acoes",
        "name": "Ações",
        "category": "renda_variavel",
        "category_label": "Renda Variável",
        "risk": "alto",
        "risk_label": "Alto — pode perder parte do valor investido",
        "liquidity": "alta",
        "liquidity_label": "Alta — negocia na bolsa todos os dias",
        "minimum": 5,
        "minimum_label": "A partir de R$ 5 (uma fração de ação)",

        "what_is": (
            "Quando você compra uma ação, vira sócia de uma empresa. "
            "Se a empresa vai bem, o valor da ação sobe e ela pode distribuir dividendos. "
            "Se vai mal, o valor cai."
        ),
        "how_it_works": (
            "Você escolhe empresas em que acredita, compra ações na bolsa e "
            "acompanha o desempenho. Pode receber dividendos — parte do lucro da empresa — "
            "isentos de IR para pessoa física."
        ),
        "makes_sense_when": (
            "Você quer aprender sobre empresas, tem interesse em acompanhar o mercado "
            "e aceita volatilidade em troca de potencial de retorno maior. "
            "É para o dinheiro que você pode deixar parado por anos."
        ),
        "watch_out": (
            "Exige estudo e acompanhamento. Não diversifique em poucas empresas. "
            "Nunca invista em ações o dinheiro que pode precisar. "
            "Emoção é o maior inimigo do investidor em ações."
        ),
        "where_to_find": "Qualquer corretora com acesso à B3.",
        "profiles": ["independent", "accumulator"],
        "goals": ["crescimento", "longo_prazo", "renda_passiva"],
    },

    # ── PREVIDÊNCIA ───────────────────────────────────────────────────────────

    "previdencia_pgbl_vgbl": {
        "id": "previdencia_pgbl_vgbl",
        "name": "Previdência Privada (PGBL / VGBL)",
        "category": "previdencia",
        "category_label": "Previdência",
        "risk": "variavel",
        "risk_label": "Varia — depende do fundo escolhido",
        "liquidity": "baixa",
        "liquidity_label": "Baixa — pensado para longo prazo",
        "minimum": 100,
        "minimum_label": "A partir de R$ 100/mês",

        "what_is": (
            "Um produto de longo prazo para construir patrimônio para a aposentadoria. "
            "PGBL permite deduzir até 12% da renda bruta no IR anual. "
            "VGBL é melhor para quem faz declaração simplificada."
        ),
        "how_it_works": (
            "Você contribui mensalmente ou faz aportes. O dinheiro é investido em "
            "fundos dentro do plano. No futuro, resgata o valor acumulado ou "
            "converte em renda mensal."
        ),
        "makes_sense_when": (
            "Você pensa em aposentadoria e quer um benefício fiscal agora. "
            "PGBL faz sentido se você tem renda tributável e declara o IR completo. "
            "Bom para planejamento de longo prazo com disciplina de aporte regular."
        ),
        "watch_out": (
            "Compare as taxas de administração e carregamento — podem ser abusivas em alguns bancos. "
            "Pesquise os fundos disponíveis dentro do plano. "
            "Resgate antecipado tem alíquotas altas de IR."
        ),
        "where_to_find": "Bancos e corretoras. Compare planos em diferentes instituições antes de contratar.",
        "profiles": ["preserver", "follower", "independent"],
        "goals": ["aposentadoria", "longo_prazo", "beneficio_fiscal"],
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# MAPA DE PERFIL → PRODUTOS
# Baseado nos achados da pesquisa SCF / UMass Boston
# ─────────────────────────────────────────────────────────────────────────────

PROFILE_PRODUCT_MAP = {

    "preserver": {
        "description": (
            "Prioriza segurança e preservação. "
            "Patrimônio presente mas movimento ausente. "
            "Precisa de clareza e previsibilidade antes de agir."
        ),
        "primary_products": ["tesouro_selic", "cdb", "fundo_renda_fixa"],
        "secondary_products": ["previdencia_pgbl_vgbl", "tesouro_ipca"],
        "not_yet": ["fiis", "acoes", "etf_brasil", "fundo_multimercado"],
        "message": (
            "Seu perfil valoriza segurança — e isso é uma força, não uma fraqueza. "
            "Os produtos abaixo preservam seu patrimônio e rendem acima da poupança "
            "sem te expor a variações que causam ansiedade."
        ),
    },

    "follower": {
        "description": (
            "Age por influência externa. "
            "Literacia financeira em desenvolvimento. "
            "Precisa de simplicidade e confiança antes de decidir sozinha."
        ),
        "primary_products": ["tesouro_selic", "cdb", "lci_lca"],
        "secondary_products": ["fundo_renda_fixa", "tesouro_ipca", "previdencia_pgbl_vgbl"],
        "not_yet": ["acoes", "fundo_multimercado"],
        "message": (
            "Antes de seguir indicações de outros, entenda o que cada produto faz. "
            "Os produtos abaixo são simples, transparentes e adequados para "
            "quem está construindo sua própria base de decisão."
        ),
    },

    "independent": {
        "description": (
            "Alta literacia, objetivo definido, mas ainda sem gatilho para agir. "
            "Sabe o que quer mas busca confirmação antes de se mover."
        ),
        "primary_products": ["tesouro_ipca", "lci_lca", "fiis"],
        "secondary_products": ["fundo_multimercado", "cdb", "acoes"],
        "not_yet": [],
        "message": (
            "Você já tem o conhecimento. O que os dados mostram é que "
            "o próximo passo é definir um objetivo concreto — não aprender mais. "
            "Os produtos abaixo alinham com quem pensa em médio e longo prazo."
        ),
    },

    "accumulator": {
        "description": (
            "Expectativa de evento ou gatilho presente. "
            "Disposição para agir. Maior abertura para crescimento. "
            "O perfil de maior participação em investimentos nos dados da pesquisa."
        ),
        "primary_products": ["etf_brasil", "fiis", "acoes"],
        "secondary_products": ["fundo_multimercado", "tesouro_ipca", "lci_lca"],
        "not_yet": [],
        "message": (
            "Você está na janela de maior abertura para decisão patrimonial. "
            "Os dados mostram que esse momento tende a se fechar. "
            "Os produtos abaixo são para quem quer crescimento real no longo prazo."
        ),
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# OBJETIVOS — MAPA SONHO → PRODUTOS
# A pessoa escolhe o sonho, a plataforma conecta ao produto
# ─────────────────────────────────────────────────────────────────────────────

GOALS = {
    "viagem": {
        "label": "Fazer uma viagem dos sonhos",
        "horizon": "curto_medio",
        "products": ["tesouro_selic", "cdb", "lci_lca"],
        "insight": "Para objetivos de 1 a 3 anos, segurança e liquidez importam mais que retorno.",
    },
    "aposentadoria": {
        "label": "Aposentadoria com autonomia",
        "horizon": "longo",
        "products": ["tesouro_ipca", "fiis", "previdencia_pgbl_vgbl", "etf_brasil"],
        "insight": "Para aposentadoria, o tempo é o maior ativo. Quanto antes começar, menos precisa guardar por mês.",
    },
    "renda_passiva": {
        "label": "Ter renda sem depender de salário",
        "horizon": "longo",
        "products": ["fiis", "acoes", "tesouro_ipca"],
        "insight": "Renda passiva é construída com tempo e consistência. FIIs pagam mensalmente. Ações pagam dividendos.",
    },
    "empresa": {
        "label": "Abrir um negócio ou startup",
        "horizon": "medio",
        "products": ["tesouro_selic", "cdb", "lci_lca"],
        "insight": "O capital para o negócio precisa estar protegido e acessível. Guarde em produtos seguros e líquidos.",
    },
    "imovel": {
        "label": "Comprar um imóvel",
        "horizon": "medio_longo",
        "products": ["tesouro_ipca", "lci_lca", "cdb"],
        "insight": "Para imóvel, o Tesouro IPCA+ protege da inflação enquanto você acumula o valor necessário.",
    },
    "filhos": {
        "label": "Futuro dos filhos — educação e patrimônio",
        "horizon": "longo",
        "products": ["tesouro_ipca", "etf_brasil", "previdencia_pgbl_vgbl"],
        "insight": "Tempo é o maior presente que você pode dar para os filhos. Começar cedo, mesmo com pouco, faz diferença enorme.",
    },
    "seguranca": {
        "label": "Ter segurança financeira — dormir tranquila",
        "horizon": "curto",
        "products": ["tesouro_selic", "cdb", "fundo_renda_fixa"],
        "insight": "Segurança começa com reserva de emergência de 3 a 6 meses de despesas fixas. Isso muda tudo.",
    },
    "liberdade": {
        "label": "Liberdade para escolher — trabalhar porque quer, não porque precisa",
        "horizon": "longo",
        "products": ["tesouro_ipca", "fiis", "etf_brasil", "acoes"],
        "insight": "Liberdade financeira é um número — o dia em que seus rendimentos cobrem seus gastos. Esse número tem um caminho.",
    },
}
