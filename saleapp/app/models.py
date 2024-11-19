from email.policy import default

from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Float, String, ForeignKey

from app import db, app


class Category(db.Model):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(50), unique=True, nullable=False)
    products = relationship("Product", backref="category", lazy=True)


class Product(db.Model):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(50), unique=True, nullable=False)
    description = db.Column(String(255), nullable=True)
    price = db.Column(Float, default=0)
    image = db.Column(String(150), nullable=True)
    category_id = db.Column(Integer, ForeignKey('category.id'), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name = 'Mobile')
        # c2 = Category(name = 'Tablet')
        # c3 = Category(name = 'Desktop')
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        data = [{
            "id": 1,
            "name": "iPhone 7 Plus",
            "description": "Apple, 32GB, RAM: 3GB, iOS13",
            "price": 17000000,
            "image": "https://cdn-v2.didongviet.vn/files/products/2024/5/6/1/1717610646368_samsung_a15_lte_didongviet_5.png",
            "category_id": 1
        }, {
            "id": 2,
            "name": "iPad Pro 2020",
            "description": "Apple, 128GB, RAM: 6GB",
            "price": 37000000,
            "image": "https://cdn2.fptshop.com.vn/unsafe/256x0/filters:quality(100)/2023_12_11_638379104038503416_samsung-galaxy-a15-den-5.jpg",
            "category_id": 2
        }, {
            "id": 3,
            "name": "Galaxy Note 10 Plus",
            "description": "Samsung, 64GB, RAML: 6GB",
            "price": 24000000,
            "image": "https://file.hstatic.net/1000190136/file/3_result_0af7ed26e9554c409cfc0e5ca61f338b_grande.png",
            "category_id": 1
        },
            {
                "id": 4,
                "name": "Galaxy Note 11 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image": "https://file.hstatic.net/1000190136/file/3_result_0af7ed26e9554c409cfc0e5ca61f338b_grande.png",
                "category_id": 1
            },
            {
                "id": 5,
                "name": "Galaxy Note 12 Plus",
                "description": "Samsung, 64GB, RAML: 6GB",
                "price": 24000000,
                "image": "https://file.hstatic.net/1000190136/file/3_result_0af7ed26e9554c409cfc0e5ca61f338b_grande.png",
                "category_id": 1
            }
        ]

        for p in data:
            prod = Product(name=p['name'], description=p['description'], price=p['price'], image=p['image'],
                           category_id=p['category_id'])
            db.session.add(prod)
        db.session.commit()

