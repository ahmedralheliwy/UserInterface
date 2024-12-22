# Django Authentication Project

This project demonstrates a basic implementation of user authentication using Django. It includes features such as user registration, login, logout, viewing account details, and a simple landing page. The project also incorporates authentication-based access control and basic input validation.

## Features

1. **User Registration**  
   - Users can create an account by providing a username, email, password, and profile picture.  
   - Validation ensures valid input and secure password handling.  

2. **User Login**  
   - Authenticated users can log in using their username and password.  
   - Invalid login attempts are handled with appropriate error messages.

3. **User Logout**  
   - Authenticated users can log out securely, clearing their session.

4. **View Account Details**  
   - Users can view their personal account details such as username, email, and optional profile picture.  
   - Membership date and last login details are also displayed.

5. **Landing Page**  
   - A simple, welcoming landing page accessible to both authenticated and unauthenticated users.

6. **Authentication-Based Access Control**  
   - Protected views (like account details) are accessible only to authenticated users.  
   - Users are redirected to the login page if they attempt to access protected resources without authentication.

7. **Validation**  
   - Basic validation for input fields during registration and login to ensure data integrity and a smooth user experience.

## Technologies Used

- **Django**: A Python web framework for building robust and scalable web applications.
- **Tailwind CSS**: For creating a responsive and visually appealing user interface.
- **SQLite**: Default database for development and testing.

## How to Run the Project

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/ahmedralheliwy/UserInterface.git
   cd UserInterface
   ```

2. **Install Dependencies**  
   Ensure you have Python installed and then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**  
   Open your browser and navigate to:  
   `http://127.0.0.1:8000/`

## Project Structure

- **accounts/**: Contains views, forms, and models for user authentication.
- **templates/**: HTML templates for rendering the frontend.
- **static/**: Contains static files like CSS and JavaScript.
- **media/**: Directory for uploaded media files, such as profile pictures.

---

Feel free to modify this text to better fit your project!


![Screenshot_2024-12-22_21-12-42](https://github.com/user-attachments/assets/6c76221a-719f-43db-a5f7-976e34a9fc5a)

![Screenshot_2024-12-22_21-13-33](https://github.com/user-attachments/assets/1e311246-b54c-4781-98a6-414177fa6ba4)

![Screenshot_2024-12-22_21-10-24](https://github.com/user-attachments/assets/fba80972-619e-4c66-897b-c603337b991a)


![Screenshot_2024-12-22_21-11-23](https://github.com/user-attachments/assets/30fd096d-ae8b-4135-bc08-deff489e0dbb)


![Screenshot_2024-12-22_21-11-39](https://github.com/user-attachments/assets/17f092ab-f6b0-4be8-95b1-2d5d6033ef2a)
