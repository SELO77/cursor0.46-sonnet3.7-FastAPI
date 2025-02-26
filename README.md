# AI Generated boilerplate - FastAPI

```json
Create a REST API backend project of AI-genereated text micro service

# Project overview
This project is a micro service that serves LLM generated text. The REST API server is to response a message and add system prompting through LLMs provider(OpenRouter). It is responsible for creating text in diverse chat services. In order to create text suitable for the concept of various chat services, we manage the system prompt and LLM models list(in OpenRouter)

# Technical Requirements
The technology stack uses the latest fastAPI and selects the most universal folder structure and the rest of the technology stack.

Language: Python
Framework: FastAPI
Database: Postgres(Supabase)
Authentication: without authentication

# Cloud and Deployment considerations
Cloud: Google cloud platform, Cloud function(gen2)
CI/CD: github action

# Main Features
1. Text generation API. Receive a message creation request from the client and select the system prompt and the appropriate model from the requested prompt(messages list). And, request for text generation to OpenRouter. 
2. Management of system prompts in the Database

# Data Models
- Message
- System Prompt

# API Endpoints
- POST /messages
```
