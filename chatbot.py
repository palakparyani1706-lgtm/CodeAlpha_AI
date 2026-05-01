import json
from preprocess import preprocess
from similarity import FAQMatcher

with open("data/faqs.json") as f:
    faqs = json.load(f)

questions = [preprocess(faq["question"]) for faq in faqs]
matcher = FAQMatcher(questions)

def get_response(user_input):
    processed = preprocess(user_input)
    index, score = matcher.find_best_match(processed)

    if score < 0.3:
        return "Sorry, I didn't understand that."

    return faqs[index]["answer"]