# BEDTE (Bridging Endangered Dialects with Tagalog and English)
#### Video Demo:  [https://youtu.be/U29eSCOVaYU]
#### Description:
BEDTE (Bridging Endangered Dialects with Tagalog and English)
Project Overview

BEDTE is a web-based application designed to preserve and promote the Casiguran Agta language, an endangered language spoken by the Agta community in the Philippines. This platform provides a practical way for users to translate between Casiguran Agta, Tagalog, and English using a rule-based translation system. Users can interact with the platform through voice or text input, allowing for real-time translation, pronunciation assistance, and educational content.

The primary goal of BEDTE is to help maintain the cultural heritage of the Agta community by making their language accessible to both native speakers and learners. By offering interactive features, the application bridges the communication gap and supports language documentation, learning, and preservation.

Key Features

Translation Interface: Users can type or speak in Casiguran Agta, Tagalog, or English and receive translations into their chosen language.
Rule-Based Translation: Uses a dictionary and pattern-matching system to provide accurate translations without relying on complex AI models.
Pronunciation Assistance: Guides users on how to pronounce Casiguran Agta words correctly.
Voice Input & Output: Users can interact with the platform using their microphone or keyboard input.
Interactive Learning: Includes stories, phrases, and games to support engaging language learning.
User Profiles: Users can create accounts, manage profiles, and track their learning progress.
Teacher & User Dashboards: Tailored dashboards for teachers and students to manage content and learning activities.

User Flow

Landing Page:
Users arrive at homepage.html, where they can choose to learn, translate, or access their account.

Registration/Login:
Users can create a new account or log in to an existing one. Registered users gain access to personalized dashboards and additional features.

Language Translation:
Select the input language (Casiguran Agta, Tagalog, or English).
Provide input via text or microphone.
System performs rule-based translation and displays the result along with pronunciation guidance.

Interactive Learning:

Access stories and phrases for practice.
Play educational games to reinforce vocabulary.

Dashboards:
User Dashboard: View learning progress, translated phrases, and history.

Teacher Dashboard: Add/edit phrases, manage educational content, and monitor user engagement.
Profile Management:
Users can update their profile, change passwords, and manage personal settings.
Additional Features:
Users can navigate to About Us, Contact, and other sections for more information about the project and its creators.

File Structure
BEDTE/
├─ .venv/                  # Python virtual environment for managing dependencies
├─ aboutus/                # Pages and scripts related to the About Us section
├─ audio/                  # Audio files, recordings, or speech assets
├─ chatbot/                # Chatbot scripts, dialogue rules, and backend logic
├─ contact/                # Contact page scripts and form handling
├─ game/                   # Educational or language-related games
├─ img/                    # Images used across the application
├─ js/                     # JavaScript files for front-end functionality
├─ phpsql/                 # PHP scripts for database operations and backend logic
├─ phrase/                 # Dictionary or phrase files used for translations
├─ profile/                # User profile management and account features
├─ sql/                    # SQL scripts for creating tables, queries, and seeding data
├─ story/                  # Story content to assist language learning
├─ style/                  # CSS files for styling and layouts
├─ teacherdashboard/       # Dashboard and interface for teachers/admins
├─ userdashboard/          # Dashboard and interface for general users
├─ vendor/                 # Composer-managed PHP dependencies
├─ venv/                   # Optional Python virtual environment if used
├─ composer.json           # Composer configuration file for PHP dependencies
├─ composer.lock           # Composer lock file to maintain consistent package versions
├─ homepage.html           # Main landing page for the application
└─ README.md               # Project documentation

Technologies Used

HTML, CSS, JavaScript: Front-end interface and interactive features.
PHP & MySQL: Backend server-side logic and database management.
Rule-Based Dictionary System: For accurate translation between Casiguran Agta, Tagalog, and English.
Audio & Speech Handling: Microphone input and audio playback for pronunciation guidance.

Design Decisions

Rule-Based Translation vs AI: A dictionary and pattern-based approach was chosen for predictability, simplicity, and faster performance without requiring complex AI/NLP models.
Separate Dashboards: Teacher and user dashboards allow clear separation of administrative functions and student learning features.
Voice & Text Input: Voice input makes the platform more accessible, while text input allows for learning and reference.
Modular File Structure: Organized folders and scripts improve maintainability and allow future enhancements without major restructuring.

Conclusion

BEDTE is a comprehensive tool designed to preserve Casiguran Agta while providing users an intuitive platform for translation and learning. With its interactive dashboards, rule-based translation system, and educational features, BEDTE empowers the Agta community and learners alike to engage with the language, ensuring its preservation for future generations.
