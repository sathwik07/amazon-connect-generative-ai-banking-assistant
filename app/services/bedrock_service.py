class BedrockService:
    def __init__(self, knowledge_base=None):
        self.knowledge_base = knowledge_base or []

    def generate_response(self, question):
        question = question.lower().strip()

        for item in self.knowledge_base:
            if any(
                word in item["question"].lower()
                for word in question.split()
                if len(word) > 3
            ):
                return item["answer"]

        return (
            "I couldn't find a matching answer in the banking "
            "knowledge base. Please contact a banking representative."
        )
