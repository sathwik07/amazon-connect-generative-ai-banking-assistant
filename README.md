# Banking Virtual Assistant using Amazon Connect

## About

This project is a Python-based banking virtual assistant. It handles basic customer queries such as account balance, recent transactions, account information, and general banking questions.

The application uses separate Python services for banking operations, authentication, conversation handling, and customer interaction. The project also includes handler examples for Amazon Connect and Amazon Lex V2.

## What it does

- Handles account balance and transaction inquiries.
- Maintains sample customer account information.
- Provides a basic OTP verification flow.
- Identifies common banking requests through keyword-based intent handling.
- Retrieves answers from a small banking knowledge base.
- Includes a separate handler for Amazon Connect contact events.
- Includes an Amazon Lex V2 handler example.

## Technologies

- Python
- Amazon Connect
- Amazon Lex V2
- Amazon Bedrock
- AWS Lambda
- FastAPI
- Git and GitHub

## Project Structure

```text
app/
    services/
        authentication_service.py
        banking_service.py
        bedrock_service.py
        connect_service.py
        conversation_service.py
        knowledge_base.py

lambda/
    __init__.py
    connect_handler.py
    lex_handler.py

main.py
requirements.txt
README.md
```

## How the application works

A customer submits a banking-related question. The conversation service identifies the request and calls the banking service when account information is needed.

For general questions, the application checks its banking knowledge base and returns a matching response.

The authentication service contains a basic OTP verification flow. Separate handler modules demonstrate how the application can be connected to Amazon Connect and Amazon Lex V2.

## Running the project

The Python application is being developed with sample customer records and local service implementations.

AWS credentials and live service configuration are not included in this repository. The Amazon Connect, Lex V2, and Bedrock components require additional integration and testing before live deployment.

## Current Scope

This is a demonstration project using mock banking data. It does not connect to real customer accounts or process actual banking transactions.

## Future Work

- Add live Amazon Bedrock model integration.
- Configure Amazon Lex V2 intents and fulfillment.
- Connect Amazon Connect contact flows with Lambda.
- Add automated tests for banking and authentication services.
- Improve conversation logging and error handling.
- ## Application Architecture

The application is organized into separate services:

- **Conversation Service:** Handles customer messages and manages the conversation flow.
- **Banking Service:** Provides sample account details, balance information, and transaction history.
- **Authentication Service:** Generates and verifies demo OTPs.
- **Knowledge Base:** Stores common banking questions and answers.
- **Bedrock Service:** Performs local FAQ matching as a placeholder for future Bedrock integration.
- **Connect Service:** Handles sample contact events and chat messages.
- **Lambda Handlers:** Provide example entry points for Connect and Lex-style events.

GitHub Actions runs the automated tests whenever changes are pushed to the main branch.
