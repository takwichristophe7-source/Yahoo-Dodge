# Yahoo Dodge 🛡️

**Yahoo Dodge** is a production-quality Minimum Viable Product (MVP) for a modern AI-powered cybersecurity and digital citizenship platform designed specifically for Cameroon.

## 🎯 Vision

Empower Cameroon's citizens to:
- Identify and avoid scams
- Detect fake content
- Learn cybersecurity best practices
- Report fraud effectively
- Become responsible digital citizens

## 🚀 Features

### Core Platform
- **User Authentication**: Secure sign-up, login, email verification, and session management
- **Dashboard**: Protection score, cyber XP, learning progress, and activity tracking
- **AI Shield**: Analyze text, emails, URLs, and messages for scam detection
- **Caller ID Checker**: Verify phone numbers and check scam risk
- **Scam Reporter**: Report various types of scams with evidence
- **Cameroon Scam Heat Map**: Visualize scam hotspots by region
- **Learning Center**: Cybersecurity lessons with progress tracking
- **Quiz System**: Interactive quizzes with XP rewards
- **Leaderboard**: Rank users by XP, achievements, and contributions
- **Certificates**: Generate downloadable achievement certificates
- **User Profile**: Manage profile, achievements, and learning history
- **Notifications**: Real-time alerts for achievements and scam warnings
- **Live Feed**: Trending scams in Cameroon
- **PWA Support**: Offline access and installable app experience

### Admin Panel
- User management
- Report moderation
- Lesson and quiz creation
- Analytics dashboard
- Leaderboard management
- Notification broadcasting

## 📋 Tech Stack

### Frontend
- HTML5, CSS3, Vanilla JavaScript
- Progressive Web App (PWA)
- Responsive design (mobile-first)
- Glassmorphism and modern UI patterns
- Dark/Light mode support

### Backend
- Python with FastAPI
- Supabase (Authentication, PostgreSQL Database, Storage)
- REST API architecture
- Secure API endpoints with input validation

### Database
- PostgreSQL (via Supabase)
- Tables: Users, Lessons, Quiz Questions, Quiz Results, Scam Reports, Phone Reports, Certificates, Notifications, Leaderboard, Badges

## 📁 Project Structure

```
yahoo-dodge/
├── frontend/
│   ├── index.html
│   ├── css/
│   │   ├── styles.css
│   │   ├── theme.css
│   │   └── responsive.css
│   ├── js/
│   │   ├── app.js
│   │   ├── auth.js
│   │   ├── dashboard.js
│   │   ├── api.js
│   │   └── utils/
│   ├── assets/
│   │   ├── icons/
│   │   ├── images/
│   │   └── fonts/
│   └── manifest.json
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── api/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── shield.py
│   │   ├── reports.py
│   │   ├── lessons.py
│   │   ├── quizzes.py
│   │   └── admin.py
│   ├── models/
│   │   ├── user.py
│   │   ├── lesson.py
│   │   ├── report.py
│   │   └── quiz.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── email_service.py
│   │   └── notification_service.py
│   └── utils/
│       ├── validators.py
│       ├── security.py
│       └── helpers.py
│
├── supabase/
│   ├── schema.sql
│   └── policies.sql
│
├── .env.example
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for frontend tooling, optional)
- Supabase account
- Modern web browser

### Installation

#### 1. Clone the repository
```bash
git clone https://github.com/takwichristophe7-source/yahoo-dodge.git
cd yahoo-dodge
```

#### 2. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your Supabase credentials
```

#### 3. Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### 4. Set up Supabase database
```bash
# Execute schema.sql and policies.sql in Supabase SQL editor
```

#### 5. Run the backend server
```bash
cd backend
uvicorn main:app --reload
```

#### 6. Serve the frontend
```bash
# Option 1: Using Python
cd frontend
python -m http.server 8000

# Option 2: Using Node.js
npx http-server frontend -p 8000
```

Access the app at `http://localhost:8000`

## 🛡️ Security Features

- JWT-based authentication
- Email verification for new accounts
- Secure password hashing (bcrypt)
- CORS protection
- Input validation and sanitization
- Rate limiting on API endpoints
- Role-based access control (User/Admin)
- Encrypted sensitive data storage

## 🌍 Multilingual Support

The platform is designed to support 110+ languages, including:
- English (default for MVP)
- French
- Cameroon Pidgin English
- Regional languages of Cameroon

Translations can be added via the `/frontend/js/i18n/` module.

## 📱 Progressive Web App

- Installable on mobile and desktop
- Offline functionality with service worker
- Cached lessons and dashboard
- Automatic sync when connection returns
- Push notifications support

## 📊 Database Schema

Key tables:
- **users**: User profiles and authentication
- **lessons**: Cybersecurity educational content
- **quiz_questions**: Multiple-choice quiz questions
- **quiz_results**: User quiz performance
- **scam_reports**: Community-submitted scam reports
- **phone_reports**: Phone number scam checks
- **certificates**: Achievement certificates
- **notifications**: User alerts and messages
- **leaderboard**: User rankings and scores
- **badges**: Achievement badges

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

Built for the national innovation competition in Cameroon. Special thanks to all contributors and the cybersecurity community.

## 📞 Support

For support, contact: support@yahodge.cm (placeholder)

---

**Yahoo Dodge** - Protecting Cameroon's Digital Future 🇨🇲
