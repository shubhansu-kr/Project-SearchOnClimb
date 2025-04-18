# Search On Climb 🏔️

A Django-based web application for exploring and discovering trekking destinations, with a focus on providing detailed information about various trek routes, locations, and travel experiences.

## 🚀 Project Overview

Search On Climb is a comprehensive trekking information platform built with Django that helps adventure enthusiasts discover and learn about various trekking destinations. The platform includes detailed information about multiple trek routes, travel guides, and destination details.

## 🛠️ Technical Stack

- **Backend Framework:** Django
- **Frontend:** HTML, CSS (with Django Templates)
- **Programming Language:** Python
- **Template Engine:** Django Template Language (DTL)


## 🌟 Features

- **Multiple Trek Routes:** Detailed information about various trek destinations including:
  - Brahmatal
  - Dayara
  - Hampta
  - Kedarkantha
  - Rupin
  - And many more

- **Content Pages:**
  - Home page with trek overview
  - Detailed trek-specific pages
  - Blog section for travel stories
  - About page
  - Contact information
  - Privacy policy

- **Utility Features:**
  - Template quote fixing script for maintaining code quality
  - Modular view structure for easy maintenance
  - Static file management for assets

## 🔧 Development Tools

### Template Management
The project includes a custom script (`script.py`) that helps maintain template integrity by:
- Scanning template files for quote inconsistencies
- Automatically fixing template URL tags
- Ensuring proper HTML syntax

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd Project-SearchOnClimb
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   cd src
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 🔍 Code Quality

The project maintains code quality through:
- Consistent view naming conventions
- Organized template structure
- Automated template fixing scripts
- Clear separation of concerns

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For any queries or suggestions, please reach out through the contact page on the website.

---
Made with ❤️ for trekking enthusiasts