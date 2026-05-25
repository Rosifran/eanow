"""
E Agora? — Motor de Matching
==============================
Recebe o perfil da usuária e devolve o padrão comportamental mais relevante.
Equivalente ao definir_estrategia() do RBC Scanner — mesma lógica, outro domínio.

Autora da pesquisa: Rosilaine Francisco — UMass Boston
"""

from data.research_data import PATTERNS, CONCEPTS


# ─────────────────────────────────────────────────────────────────────────────
# PERFIL DA USUÁRIA
# ─────────────────────────────────────────────────────────────────────────────

class UserProfile:
    """
    Perfil construído a partir das respostas da usuária na interface.
    Equivalente ao vol_data + gate do scanner.
    """
    def __init__(
        self,
        trigger: str,           # "sobra_mensal" | "heranca" | "aposentadoria" | "mudanca_vida"
        situation: str,         # "estabilidade" | "transicao" | "acumulando"
        has_reserve: bool,      # tem reserva de emergência?
        monthly_amount: float,  # quanto sobra por mês (R$)
        age: int = None,        # idade (opcional)
    ):
        self.trigger        = trigger
        self.situation      = situation
        self.has_reserve    = has_reserve
        self.monthly_amount = monthly_amount
        self.age            = age

    def to_dict(self):
        return {
            "trigger":        self.trigger,
            "situation":      self.situation,
            "has_reserve":    self.has_reserve,
            "monthly_amount": self.monthly_amount,
            "age":            self.age,
        }


# ─────────────────────────────────────────────────────────────────────────────
# MOTOR DE MATCHING
# ─────────────────────────────────────────────────────────────────────────────

class MatchingEngine:
    """
    Dado um perfil, encontra o padrão mais relevante da base de dados.
    Pontuação de relevância por critério — mesmo princípio do IV Rank no scanner.
    """

    def __init__(self):
        self.patterns = PATTERNS
        self.concepts = CONCEPTS

    def score_pattern(self, pattern: dict, profile: UserProfile) -> int:
        """
        Pontua um padrão contra o perfil da usuária.
        Maior score = melhor match.
        """
        score = 0

        # Trigger (critério mais importante — peso 4)
        if pattern["trigger"] == profile.trigger:
            score += 4
        elif pattern["trigger"] == "qualquer":
            score += 1

        # Situação (peso 3)
        if pattern["situation"] == profile.situation:
            score += 3
        elif pattern["situation"] == "qualquer":
            score += 1

        # Reserva (peso 2)
        if pattern["has_reserve"] is None:
            score += 1  # agnóstico — neutro
        elif pattern["has_reserve"] == profile.has_reserve:
            score += 2

        # Faixa etária (peso 2 se especificada)
        if pattern["age_range"] and profile.age:
            lo, hi = pattern["age_range"]
            if lo <= profile.age <= hi:
                score += 2

        # Confiança da pesquisa (peso 1)
        if pattern["confidence"] == "alta":
            score += 1

        return score

    def match(self, profile: UserProfile) -> dict:
        """
        Encontra o melhor padrão e monta o resultado completo.
        Retorna dict com padrão, score, conceitos relevantes e próxima pergunta.
        """
        scored = [
            (self.score_pattern(p, profile), p)
            for p in self.patterns
        ]
        scored.sort(key=lambda x: x[0], reverse=True)

        best_score, best_pattern = scored[0]

        # Conceitos relevantes para esse padrão
        relevant_concepts = {
            key: self.concepts[key]
            for key in best_pattern.get("concepts", [])
            if key in self.concepts
        }

        return {
            "profile":         profile.to_dict(),
            "pattern":         best_pattern,
            "match_score":     best_score,
            "max_score":       12,  # score máximo possível
            "confidence_pct":  round(best_score / 12 * 100),
            "concepts":        relevant_concepts,
            "alternatives":    [p for s, p in scored[1:3]],  # 2 alternativas
        }

    def build_analysis(self, profile: UserProfile) -> dict:
        """
        Monta a análise completa para exibição na interface.
        Equivalente ao print_relatorio() do scanner — mas estruturado para web.
        """
        result = self.match(profile)
        pattern = result["pattern"]

        # Estima meses para reserva com base no valor mensal
        # Hipótese: reserva ideal = 3x despesas fixas ≈ 2x sobra mensal (heurística)
        months_to_reserve = None
        if not profile.has_reserve and profile.monthly_amount > 0:
            estimated_reserve = profile.monthly_amount * 2 * 3  # 3 meses de despesas ≈ 6x sobra
            months_to_reserve = round(estimated_reserve / profile.monthly_amount)

        return {
            # Cabeçalho
            "headline":        pattern["headline"],
            "source":          pattern["source"],

            # Achado principal
            "finding":         pattern["finding"],

            # O que pessoas como ela fizeram
            "what_they_did":   pattern["what_they_did"],

            # O que acontece sem isso
            "what_happens_without": pattern["what_happens_without"],

            # Próxima pergunta
            "next_question":   pattern["next_question"],

            # Contextual: estimativa de prazo
            "months_to_reserve": months_to_reserve,

            # Glossário inline
            "concepts":        result["concepts"],

            # Metadados
            "pattern_id":      pattern["id"],
            "confidence":      pattern["confidence"],
            "match_score":     result["match_score"],
        }


# ─────────────────────────────────────────────────────────────────────────────
# TESTE LOCAL — equivalente ao main() do scanner
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    engine = MatchingEngine()

    test_profiles = [
        UserProfile(
            trigger="sobra_mensal",
            situation="estabilidade",
            has_reserve=False,
            monthly_amount=1200,
            age=35
        ),
        UserProfile(
            trigger="sobra_mensal",
            situation="estabilidade",
            has_reserve=True,
            monthly_amount=2000,
            age=42
        ),
        UserProfile(
            trigger="sobra_mensal",
            situation="transicao",
            has_reserve=False,
            monthly_amount=800,
            age=38
        ),
        UserProfile(
            trigger="heranca",
            situation="qualquer",
            has_reserve=True,
            monthly_amount=0,
            age=61
        ),
    ]

    SEP = "─" * 60

    for profile in test_profiles:
        analysis = engine.build_analysis(profile)
        print(f"\n{'═'*60}")
        print(f"  Perfil: {profile.trigger} | {profile.situation} | reserva={profile.has_reserve} | R${profile.monthly_amount}/mês | idade={profile.age}")
        print(f"  Match score: {analysis['match_score']}/12 | Confiança: {analysis['confidence']}")
        print(f"{SEP}")
        print(f"  HEADLINE: {analysis['headline']}")
        print(f"\n  ACHADO: {analysis['finding'][:120]}...")
        print(f"\n  PRÓXIMA PERGUNTA: {analysis['next_question']}")
        print(f"\n  CONCEITOS: {list(analysis['concepts'].keys())}")
        if analysis['months_to_reserve']:
            print(f"\n  ESTIMATIVA RESERVA: ~{analysis['months_to_reserve']} meses")
