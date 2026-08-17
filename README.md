# 🎬 Cinematic Roaster AI

An advanced, full-stack AI web application that goes beyond standard sentiment analysis. It detects negative movie reviews using a fine-tuned NLP model and triggers a generative AI to sarcastically roast the reviewer.

---

## 🏗️ Architecture & Tech Stack

This project is built on a modern split-stack architecture.

### Backend — Python

- Django
- Django REST Framework (DRF)
- Hugging Face Transformers
- PyTorch
- Django CORS Headers

### Frontend — TypeScript

- Next.js 15
- React
- TypeScript
- Tailwind CSS
- Framer Motion

### AI Models

| Component | Technology | Purpose |
|---|---|---|
| Classifier | DistilBERT | Fine-tuned for sentiment analysis |
| Generator | Flan-T5 | Prompt-engineered for sarcasm |

### Database

- SQLite — Development
- PostgreSQL — Production Ready

### External API

- TMDB API

---

## 🤖 AI Architecture

Cinematic Roaster AI uses a dual-model AI pipeline.

### DistilBERT — Sentiment Classifier

A fine-tuned DistilBERT model analyzes the submitted movie review and determines whether the review is positive or negative.

### Flan-T5 — Roast Generator

When the review is classified as negative, the review is passed to Flan-T5, which generates a sarcastic and humorous roast using prompt engineering.

### Dual-Model Pipeline

```text
                         Movie Review
                              │
                              ▼
                    ┌──────────────────┐
                    │    DistilBERT    │
                    │ Sentiment Model  │
                    └────────┬─────────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
                POSITIVE          NEGATIVE
                    │                 │
                    ▼                 ▼
             Normal Response    ┌─────────────┐
                                │   Flan-T5   │
                                │  Generator  │
                                └──────┬──────┘
                                       │
                                       ▼
                               Sarcastic Roast
```

---

## 🌟 Key Features

### 🤖 Dual-Model AI Pipeline

The application chains classification and text-generation models sequentially.

1. **DistilBERT** analyzes the sentiment of the movie review.
2. The model determines whether the review is positive or negative.
3. If the review is negative, it is passed to **Flan-T5**.
4. **Flan-T5** generates a sarcastic roast.
5. The generated response is returned to the user through the frontend.

This creates an AI pipeline where one model understands the sentiment while another model generates the final response.

---

### 🎬 Real-Time Movie Data

The application integrates the TMDB API to fetch live movie information and posters.

Features include:

- Movie titles
- Movie posters
- Movie information
- Live movie data
- Movie metadata
- Movie search functionality

---

### 🎨 Modern User Interface

The frontend provides a modern cinematic interface using:

- Glassmorphism
- Responsive design
- Tailwind CSS
- Framer Motion
- Smooth animations
- Interactive components
- Modern React architecture

---

### 🔌 RESTful API

The Django backend provides RESTful API endpoints using Django REST Framework.

The API handles:

- Review submission
- Sentiment classification
- AI inference
- Roast generation
- Communication between frontend and backend
- Model processing

---

### ⚡ Full-Stack Architecture

The frontend and backend are separated into independent services.

```text
┌──────────────────────────────────┐
│            Frontend              │
│                                  │
│      Next.js + React             │
│      TypeScript + Tailwind       │
│      Framer Motion               │
└───────────────┬──────────────────┘
                │
                │ REST API
                ▼
┌──────────────────────────────────┐
│             Backend              │
│                                  │
│      Django + Django REST        │
│      Framework                   │
└───────────────┬──────────────────┘
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
┌──────────────┐  ┌──────────────┐
│  DistilBERT  │  │   Flan-T5    │
│  Classifier  │  │  Generator   │
└──────────────┘  └──────────────┘
```

---

## 📂 Project Structure

```text
Cinematic-Roaster-AI/
│
├── backend/
│   │
│   ├── api/
│   │   ├── migrations/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── models.py
│   │   └── urls.py
│   │
│   ├── manage.py
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── movies/
│   │   │       └── route.js
│   │   ├── components/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   └── ...
│   │
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── ...
│
├── .gitignore
└── README.md
```

---

## 🚀 Local Setup & Installation

To run this application locally, you need to start both the backend and frontend servers.

---

## 1. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install django djangorestframework django-cors-headers torch transformers
```

Run database migrations:

```bash
python manage.py migrate
```

Start the Django development server:

```bash
python manage.py runserver
```

The backend will run on:

```text
http://127.0.0.1:8000
```

---

## 2. Frontend Setup

Open a **new terminal** and navigate to the frontend directory:

```bash
cd frontend
```

Install Node.js dependencies:

```bash
npm install
```

Start the Next.js development server:

```bash
npm run dev
```

The frontend will run on:

```text
http://localhost:3000
```

---

## 🔑 TMDB API Configuration

The application uses the TMDB API to fetch live movie information and posters.

Add your TMDB API key inside:

```text
frontend/app/api/movies/route.js
```

Example:

```javascript
const TMDB_API_KEY = "YOUR_TMDB_API_KEY";
```

Replace:

```text
YOUR_TMDB_API_KEY
```

with your actual TMDB API key.

> **Important:** Never expose private API keys in frontend code or commit them directly to a public GitHub repository. For production, use environment variables.

---

## 🔗 Backend & Frontend Communication

The frontend communicates with the Django backend through REST API requests.

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Next.js       │
                    │ Frontend      │
                    └───────┬───────┘
                            │
                       HTTP Request
                            │
                            ▼
                    ┌───────────────┐
                    │ Django REST   │
                    │ API           │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  DistilBERT   │
                    │  Classifier   │
                    └───────┬───────┘
                            │
                     Sentiment Result
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
             Positive               Negative
                 │                     │
                 ▼                     ▼
          Normal Response        ┌─────────────┐
                                 │   Flan-T5   │
                                 └──────┬──────┘
                                        │
                                        ▼
                                 Sarcastic Roast
                                        │
                                        ▼
                                Django REST API
                                        │
                                        ▼
                                Next.js Frontend
                                        │
                                        ▼
                                      User
```

---

## 🧠 How It Works

### Step 1 — User Review

The user submits a movie review through the Next.js frontend.

### Step 2 — API Request

The frontend sends the review to the Django REST API.

### Step 3 — Sentiment Analysis

The backend passes the review to the fine-tuned DistilBERT model.

### Step 4 — Classification

DistilBERT determines whether the review is positive or negative.

### Step 5 — Roast Generation

If the review is negative, it is passed to Flan-T5.

Flan-T5 generates a sarcastic response based on the submitted review.

### Step 6 — API Response

The generated roast is returned through the Django REST API.

### Step 7 — Frontend Display

The Next.js frontend displays the generated response to the user.

---

## 🛠️ Development Workflow

The project follows a modern development workflow:

```text
Development
     │
     ▼
Frontend Development
     │
     ▼
REST API Integration
     │
     ▼
AI Model Integration
     │
     ▼
Testing
     │
     ▼
Docker Containerization
     │
     ▼
Production Deployment
```

---

## 📊 Technology Breakdown

### Frontend

#### Next.js 15

Used to build the modern React-based frontend and application structure.

#### React

Used to create reusable and interactive UI components.

#### TypeScript

Provides type safety and improves the overall developer experience.

#### Tailwind CSS

Used for responsive styling and modern UI development.

#### Framer Motion

Used for smooth animations and interactive visual effects.

---

### Backend

#### Django

Provides the main Python backend framework.

#### Django REST Framework

Provides RESTful API functionality for communication between the frontend and backend.

#### Django CORS Headers

Handles cross-origin communication between the Next.js frontend and Django backend.

---

### AI / Machine Learning

#### Hugging Face Transformers

Used to load and work with transformer-based NLP models.

#### PyTorch

Used as the deep learning framework for model inference.

#### DistilBERT

Used for sentiment classification.

#### Flan-T5

Used for generating sarcastic responses.

---

## 🗄️ Database

### Development

SQLite is used during local development because it is lightweight and requires minimal configuration.

### Production

The application is designed to be production-ready with PostgreSQL.

Planned production architecture:

```text
Next.js Frontend
       │
       ▼
Django REST API
       │
       ▼
PostgreSQL Database
```

---

## 🔐 Security Considerations

For production deployment:

- Store API keys in environment variables.
- Never expose secret keys in frontend code.
- Configure Django CORS properly.
- Use HTTPS.
- Configure secure Django settings.
- Use PostgreSQL instead of SQLite.
- Protect authentication endpoints.
- Validate API input.
- Apply rate limiting where required.
- Secure sensitive environment variables.

---

## 🐳 Future Docker Architecture

Docker and Docker Compose are planned for containerized deployment.

```text
                    Docker Compose
                          │
            ┌─────────────┴─────────────┐
            │                           │
            ▼                           ▼
    ┌───────────────┐           ┌───────────────┐
    │   Frontend    │           │    Backend    │
    │   Next.js     │           │    Django     │
    └───────────────┘           └───────┬───────┘
                                        │
                              ┌─────────┴─────────┐
                              │                   │
                              ▼                   ▼
                       ┌─────────────┐     ┌─────────────┐
                       │  DistilBERT │     │   Flan-T5   │
                       │  Classifier │     │  Generator  │
                       └─────────────┘     └─────────────┘
                                        │
                                        ▼
                                  PostgreSQL
```

## 💡 What This Project Demonstrates

Cinematic Roaster AI demonstrates practical experience across modern AI and full-stack development.

### AI & Machine Learning

- Natural Language Processing
- Sentiment Analysis
- Transformer Models
- Fine-Tuning
- Text Classification
- Generative AI
- Prompt Engineering
- Model Inference
- Hugging Face Transformers
- PyTorch

### Backend Development

- Python
- Django
- Django REST Framework
- REST APIs
- API Integration
- Database Integration
- AI Model Integration

### Frontend Development

- Next.js
- React
- TypeScript
- Tailwind CSS
- Framer Motion
- Responsive UI
- API Integration
- Component-Based Development

### Software Engineering

- Full-Stack Architecture
- Separation of Concerns
- RESTful Architecture
- Modular Development
- Database Design
- AI Application Development
- Production-Oriented Architecture
- Containerization Planning

---

## 🚀 Production Deployment Plan

### Frontend

The Next.js application can be deployed using Vercel.

### Backend

The Django REST API can be deployed on AWS EC2 or another cloud infrastructure.

### Database

PostgreSQL can be used as the production database.

### Containerization

Docker and Docker Compose can be used to simplify deployment and environment management.

```text
                         Production
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
           Vercel                         AWS EC2
              │                             │
              ▼                             ▼
        Next.js App                    Django API
                                            │
                                  ┌─────────┴─────────┐
                                  │                   │
                                  ▼                   ▼
                             DistilBERT           Flan-T5
                                  │                   │
                                  └─────────┬─────────┘
                                            │
                                            ▼
                                       PostgreSQL
```

---

## 🎯 Project Goals

The main goal of Cinematic Roaster AI is to demonstrate how multiple AI models can be combined with a modern full-stack application to create an engaging and practical AI-powered product.

The project focuses on:

- Combining classification and generation models.
- Building AI-powered REST APIs.
- Integrating AI inference into web applications.
- Creating modern AI user interfaces.
- Working with real-time external APIs.
- Designing scalable full-stack architecture.
- Applying NLP and generative AI to a real-world application.

---

## 📈 Project Highlights

### AI Engineering

- Fine-tuned NLP classification
- Transformer-based models
- Sequential AI model pipeline
- Generative AI
- Prompt engineering
- Model inference

### Full-Stack Engineering

- Next.js frontend
- Django backend
- REST API architecture
- Database integration
- External API integration
- Responsive UI

### Production Readiness

- PostgreSQL support
- Docker-ready architecture
- AWS deployment planning
- Vercel deployment planning
- Environment-based configuration

---

## 👩‍💻 Built By

**Syeda Sumayya**

**Robotics Engineer | AI Engineer | Full-Stack Developer**

Cinematic Roaster AI combines AI, NLP, generative models, and modern web development into one interactive application.

Built with ❤️, AI, and a little cinematic sarcasm. 🎬🔥

## 📜 License

This project is developed for educational, portfolio, and demonstration purposes.
