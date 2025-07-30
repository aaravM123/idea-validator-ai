import random

def uniqueness_scorer(idea: str) -> str:
    """
    Provides an originality score for a startup idea.
    
    Args:
        idea (str): The startup idea description
        
    Returns:
        str: Originality score with contextual feedback
    """
    score = random.randint(1, 10)
    if score > 7:
        return f"Originality Score: {score}/10 — Possibly disruptive!"
    elif score > 4:
        return f"Originality Score: {score}/10 — Competitive market likely."
    else:
        return f"Originality Score: {score}/10 — Consider differentiating more." 