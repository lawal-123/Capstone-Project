Capstone Project: Ecommerce API

Ecommerce is a robust RESTful API built with Django and Django REST Framework, designed to power a modern ecommerce platform. It features full product management, category organization with SEO-friendly slugs, and a secure shopping cart system.

Features:-
JWT Authentication: Secure user login and registration using SimpleJWT.

Product Management: Full CRUD functionality for products including stock tracking.

Category System: Organized product grouping with auto-generating Slugs for readable URLs.

Shopping Cart: Authenticated users can add, update, and remove items from their personal carts.

TECH STACK

Language: Python 3.13

Framework: Django 5.x

API Engine: Django REST Framework (DRF)

Authentication: SimpleJWT (JSON Web Tokens)

Database: SQLite (Development)


 API Endpoints
 Method      Endpoint                Description
 POST       /api/token/             Obtain Access & Refresh Tokens
 GET       /api/v1/products/       List all available products
 POST      /api/v1/cart/           Add a product to the cart (Auth Required)
 GET       /api/v1/categories/     List all product categories

 Why Lawal Mart?
Lawal Mart is specifically designed for the Construction and Interior Decor industry in Nigeria. Unlike general stores, it handles specific measurements for products like Paints and wall Finishes Which provides a specialized experience for contractors, engineers and homeowners.
