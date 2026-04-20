from transformers import pipeline

summarizer = None
paraphraser = None
grammar = None

# =========================
# LOAD MODELS
# =========================
def load_models():
    global summarizer, paraphraser, grammar

    summarizer = pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

    paraphraser = pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

    grammar = pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

# =========================
# FUNCTIONS
# =========================
def summarize(text):
    prompt = "summarize: " + text
    result = summarizer(prompt, max_length=150, do_sample=False)
    return result[0]["generated_text"]

def paraphrase(text):
    prompt = "paraphrase: " + text
    result = paraphraser(prompt, max_length=150, do_sample=False)
    return result[0]["generated_text"]

def correct(text):
    prompt = "grammar: " + text
    result = grammar(prompt, max_length=150, do_sample=False)
    return result[0]["generated_text"]