# E-Commerce Backend System(Storedeal)

This project implements a basic backend system for an e-commerce platform using **Python** and **Django**. It provides key functionalities such as user authentication, product management, and a shopping cart system.

---

## Features

### **User Authentication**
- User registration and login using **Djoser** and **JWT tokens**.
- Endpoints for token creation, refresh, and verification.

### **Product Management**
- Create, Read, Update, and Delete (CRUD) products.
- Each product includes:
  - Name
  - Price
  - Stock Quantity
  - Category

### **Shopping Cart**
- Add products to the shopping cart.
- View items in the shopping cart with details (name, price, quantity).

---

## Installation and Setup

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd <repository_name>
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Create a Superuser**
```bash
python manage.py createsuperuser
```

### **6. Run the Development Server**
```bash
python manage.py runserver
```

---

## API Endpoints

### **Authentication Endpoints** (Powered by Djoser)

#### Token-Based Authentication
- **Login:** `POST /auth/jwt/create/`
  - Request Body: `{ "username": "<username>", "password": "<password>" }`
  - Response: `{ "access": "<access_token>", "refresh": "<refresh_token>" }`

- **Refresh Token:** `POST /auth/jwt/refresh/`
  - Request Body: `{ "refresh": "<refresh_token>" }`
  - Response: `{ "access": "<new_access_token>" }`

- **Verify Token:** `POST /auth/jwt/verify/`
  - Request Body: `{ "token": "<access_token>" }`

- **Register User:** `POST /auth/users/`
  - Request Body: `{ "username": "<username>", "password": "<password>", "re_password": "<password>" }`
  - Response: `{ "id": 1, "username": "<username>" }`

### **Product Endpoints**
- **List Products:** `GET /products/`
- **Create Product:** `POST /products/`
  - Request Body: `{ "name": "<name>", "price": <price>, "stock": <stock>, "category": <category_id> }`
- **Retrieve Product:** `GET /products/<id>/`
- **Update Product:** `PUT /products/<id>/`
  - Request Body: `{ "name": "<name>", "price": <price>, "stock": <stock>, "category": <category_id> }`
- **Delete Product:** `DELETE /products/<id>/`

### **Shopping Cart Endpoints**
- **View Cart Items:** `GET /cart/`
- **Add/Update Cart Item:** `POST /cart/`
  - Request Body: `{ "product_id": <product_id>, "quantity": <quantity> }`

---

## Assumptions
- Categories must be created before associating them with products.
- Only authenticated users can access the shopping cart endpoints.

---