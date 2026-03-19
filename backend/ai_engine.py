from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def complexity_score(code):

    score = 10

    if "for" in code or "while" in code:
        score -= 2

    if "if" in code:
        score -= 1

    if len(code) > 200:
        score -= 2

    if score < 1:
        score = 1

    return f"Code Quality Score: {score}/10"


def analyze_code(code, task):

    if task == "score":
        return complexity_score(code)

    prompts = {
        "explain": f"Explain the following code:\n{code}",
        "bugs": f"Find possible bugs in this code:\n{code}",
        "improve": f"Suggest improvements for this code:\n{code}",
        "commit": f"Write a git commit message for these code changes:\n{code}"
    }

    result = generator(prompts[task], max_length=120)

    return result[0]["generated_text"]