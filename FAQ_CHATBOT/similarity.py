from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQMatcher:
    def __init__(self, questions):
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(questions)

    def find_best_match(self, user_question):
        user_vec = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vec, self.question_vectors)

        best_index = similarities.argmax()
        best_score = similarities[0][best_index]

        return best_index, best_score
