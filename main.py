from app.services.banking_service import BankingService
from app.services.conversation_service import ConversationService


def main():
    banking = BankingService()
    assistant = ConversationService(banking)

    print("\nBanking Virtual Assistant")
    print("-------------------------")
    print("Ask about your account balance or recent transactions.")
    print("Type 'exit' to close the assistant.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in ("exit", "quit", "bye"):
            print("Assistant: Thank you for using our banking service.")
            break

        if not question:
            print("Assistant: Please enter a question.")
            continue

        answer = assistant.get_response(question)
        print(f"Assistant: {answer}")


if __name__ == "__main__":
    main()
