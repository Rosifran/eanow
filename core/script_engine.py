"""
E Agora? — Script Engine
=========================
Diagnóstico comportamental → Perfil → Mapa de produtos.

5 perguntas. 4 perfis. 1 mapa claro.
A plataforma mostra. A usuária decide.

Autora da pesquisa: Rosilaine Francisco — UMass Boston
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.products_br import PRODUCTS, PROFILE_PRODUCT_MAP, GOALS


# ─────────────────────────────────────────────────────────────────────────────
# AS 5 PERGUNTAS DO DIAGNÓSTICO
# Baseadas nas variáveis da pesquisa SCF / UMass Boston
# ─────────────────────────────────────────────────────────────────────────────

QUESTIONS = [
    {
        "id": "q1",
        "text": "Você tem um objetivo financeiro claro agora — mesmo que vago?",
        "insight": "Mede presença de gatilho/objetivo — variável central da pesquisa",
        "options": [
            {"id": "a", "text": "Sim, tenho um objetivo claro", "scores": {"independent": 2, "accumulator": 2}},
            {"id": "b", "text": "Tenho uma ideia, mas vaga", "scores": {"follower": 1, "independent": 1}},
            {"id": "c", "text": "Não, ainda não sei o que quero", "scores": {"preserver": 2, "follower": 1}},
        ]
    },
    {
        "id": "q2",
        "text": "Se você recebesse R$ 10.000 hoje, o que faria nas primeiras 48 horas?",
        "insight": "Mede comportamento real vs declarado — revela script patrimonial",
        "options": [
            {"id": "a", "text": "Deixaria na conta até decidir com calma", "scores": {"preserver": 2}},
            {"id": "b", "text": "Perguntaria para alguém de confiança o que fazer", "scores": {"follower": 2}},
            {"id": "c", "text": "Pesquisaria as melhores opções antes de agir", "scores": {"independent": 2}},
            {"id": "d", "text": "Já sei onde colocaria — tenho um plano", "scores": {"accumulator": 2}},
        ]
    },
    {
        "id": "q3",
        "text": "Você espera ter acesso a patrimônio nos próximos anos? (herança, venda de imóvel, bônus, FGTS, outros)",
        "insight": "Variável central da pesquisa — expectativa de evento patrimonial futuro",
        "options": [
            {"id": "a", "text": "Sim, tenho uma expectativa concreta", "scores": {"accumulator": 2, "independent": 1}},
            {"id": "b", "text": "Talvez, mas não tenho certeza", "scores": {"independent": 1, "follower": 1}},
            {"id": "c", "text": "Não espero nada específico", "scores": {"preserver": 1, "follower": 1}},
        ]
    },
    {
        "id": "q4",
        "text": "Quando você pensa em dinheiro, o que aparece primeiro?",
        "insight": "Mede orientação temporal e perfil emocional com dinheiro",
        "options": [
            {"id": "a", "text": "Segurança — preciso me proteger", "scores": {"preserver": 2}},
            {"id": "b", "text": "Medo de errar — não quero perder o que tenho", "scores": {"preserver": 1, "follower": 1}},
            {"id": "c", "text": "Crescimento — quero multiplicar", "scores": {"accumulator": 2}},
            {"id": "d", "text": "Liberdade — quero ter escolhas", "scores": {"independent": 2, "accumulator": 1}},
        ]
    },
    {
        "id": "q5",
        "text": "Você já tomou alguma decisão financeira que orgulha — mesmo pequena?",
        "insight": "Mede literacia ativa vs passiva — preditor de participação nos dados",
        "options": [
            {"id": "a", "text": "Sim, tenho exemplos concretos", "scores": {"independent": 2, "accumulator": 1}},
            {"id": "b", "text": "Sim, mas foram decisões simples", "scores": {"follower": 1, "independent": 1}},
            {"id": "c", "text": "Não tenho certeza — acho que não", "scores": {"preserver": 1, "follower": 2}},
        ]
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# MOTOR DE DIAGNÓSTICO
# ─────────────────────────────────────────────────────────────────────────────

class ScriptEngine:
    """
    Recebe as respostas do diagnóstico + o sonho da usuária.
    Devolve o perfil, o mapa de produtos e os insights.
    """

    def __init__(self):
        self.questions = QUESTIONS
        self.products = PRODUCTS
        self.profile_map = PROFILE_PRODUCT_MAP
        self.goals = GOALS

    def score(self, answers: dict) -> str:
        """
        answers = {"q1": "a", "q2": "c", "q3": "b", "q4": "d", "q5": "a"}
        Retorna o perfil com maior pontuação.
        """
        scores = {"preserver": 0, "follower": 0, "independent": 0, "accumulator": 0}

        for question in self.questions:
            qid = question["id"]
            answer_id = answers.get(qid)
            if not answer_id:
                continue
            for option in question["options"]:
                if option["id"] == answer_id:
                    for profile, points in option["scores"].items():
                        scores[profile] += points

        return max(scores, key=scores.get), scores

    def build_result(self, answers: dict, goal_id: str) -> dict:
        """
        Monta o resultado completo:
        - Perfil identificado
        - Descrição do perfil
        - Mensagem personalizada
        - Mapa de produtos primários e secundários
        - Insight do objetivo
        """
        profile, scores = self.score(answers)
        profile_data = self.profile_map[profile]
        goal_data = self.goals.get(goal_id, {})

        # Produtos primários completos
        primary = [
            self.products[pid]
            for pid in profile_data["primary_products"]
            if pid in self.products
        ]

        # Produtos secundários completos
        secondary = [
            self.products[pid]
            for pid in profile_data["secondary_products"]
            if pid in self.products
        ]

        # Produtos do objetivo
        goal_product_ids = goal_data.get("products", [])
        goal_products = [
            self.products[pid]
            for pid in goal_product_ids
            if pid in self.products
        ]

        # Universo completo para o mapa visual risco × liquidez
        universe_products = self.build_product_universe(profile, goal_product_ids)

        return {
            "profile": profile,
            "profile_label": {
                "preserver": "Preserver",
                "follower": "Follower",
                "independent": "Independent",
                "accumulator": "Accumulator",
            }[profile],
            "profile_description": profile_data["description"],
            "profile_message": profile_data["message"],
            "scores": scores,
            "goal": goal_id,
            "goal_label": goal_data.get("label", ""),
            "goal_insight": goal_data.get("insight", ""),
            "primary_products": primary,
            "secondary_products": secondary,
            "goal_products": goal_products,
            "universe_products": universe_products,
            "not_yet": profile_data.get("not_yet", []),
            "source": "Survey of Consumer Finances · Federal Reserve · Pesquisa de mestrado RF/UMass Boston",
        }

    def build_product_universe(self, profile: str, goal_product_ids: list) -> list:
        """
        Converte a base de produtos em bolhas para o mapa risco × liquidez.
        X = risco percebido. Y = liquidez/acessibilidade do dinheiro.
        A adequação combina perfil comportamental + objetivo escolhido.
        """
        profile_data = self.profile_map[profile]
        primary_ids = set(profile_data.get("primary_products", []))
        secondary_ids = set(profile_data.get("secondary_products", []))
        not_yet_ids = set(profile_data.get("not_yet", []))
        goal_ids = set(goal_product_ids or [])

        risk_axis = {
            "muito_baixo": 12,
            "baixo": 28,
            "medio": 54,
            "alto": 82,
            "variavel": 64,
        }
        liquidity_axis = {
            "baixa": 22,
            "media": 52,
            "alta": 84,
            "variavel": 62,
        }

        # Pequenos deslocamentos para evitar sobreposição perfeita no gráfico.
        offsets = {
            "tesouro_selic": (-4, 5),
            "cdb": (2, -4),
            "lci_lca": (-3, -3),
            "fundo_renda_fixa": (4, 2),
            "tesouro_ipca": (-2, 1),
            "fundo_multimercado": (5, -2),
            "fiis": (-4, 4),
            "etf_brasil": (2, 0),
            "acoes": (7, 5),
            "previdencia_pgbl_vgbl": (5, -5),
        }

        universe = []
        for pid, product in self.products.items():
            if pid in primary_ids:
                fit = "primary"
                fit_label = "Iluminado para seu perfil"
                fit_score = 100
            elif pid in secondary_ids:
                fit = "secondary"
                fit_label = "Pode explorar depois"
                fit_score = 72
            elif pid in goal_ids:
                fit = "goal"
                fit_label = "Conecta com seu sonho"
                fit_score = 64
            elif pid in not_yet_ids:
                fit = "not_yet"
                fit_label = "Talvez ainda não"
                fit_score = 24
            else:
                fit = "neutral"
                fit_label = "Neutro no seu mapa"
                fit_score = 42

            dx, dy = offsets.get(pid, (0, 0))
            x = min(94, max(6, risk_axis.get(product.get("risk"), 50) + dx))
            y = min(94, max(6, liquidity_axis.get(product.get("liquidity"), 50) + dy))

            item = dict(product)
            item.update({
                "x": x,
                "y": y,
                "fit": fit,
                "fit_label": fit_label,
                "fit_score": fit_score,
                "matches_goal": pid in goal_ids,
                "matches_profile": pid in primary_ids or pid in secondary_ids,
            })
            universe.append(item)

        return sorted(universe, key=lambda p: p["fit_score"], reverse=True)

    def get_questions(self) -> list:
        return self.questions

    def get_goals(self) -> dict:
        return self.goals


# ─────────────────────────────────────────────────────────────────────────────
# TESTE LOCAL
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    engine = ScriptEngine()

    # Simula uma usuária: objetivo claro, pesquisa antes de agir,
    # espera patrimônio futuro, pensa em liberdade, tem decisões financeiras
    test_answers = {
        "q1": "a",  # objetivo claro → independent/accumulator
        "q2": "c",  # pesquisa antes → independent
        "q3": "a",  # espera patrimônio → accumulator
        "q4": "d",  # liberdade → independent
        "q5": "a",  # decisões próprias → independent
    }

    result = engine.build_result(test_answers, "liberdade")

    print(f"\n{'='*60}")
    print(f"  PERFIL: {result['profile_label']}")
    print(f"  SCORES: {result['scores']}")
    print(f"  OBJETIVO: {result['goal_label']}")
    print(f"{'='*60}")
    print(f"\n  {result['profile_message']}")
    print(f"\n  INSIGHT DO OBJETIVO: {result['goal_insight']}")
    print(f"\n  PRODUTOS PRIMÁRIOS:")
    for p in result['primary_products']:
        print(f"    → {p['name']} ({p['risk_label']}) — {p['liquidity_label']}")
    print(f"\n  PRODUTOS SECUNDÁRIOS:")
    for p in result['secondary_products']:
        print(f"    → {p['name']}")
    print(f"\n  FONTE: {result['source']}")
    print(f"{'='*60}\n")
