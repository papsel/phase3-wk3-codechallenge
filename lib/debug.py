from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant,Customer,Review


if __name__ == '__main__':
    engine = create_engine('sqlite:///restuarants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
# test review methods
print("REVIEWS")
review = session.query(Review).filter_by(id=5).first() # change id to desired review
print("Customer:")
print( review.review_customer())
print("Restaurant:")
print(review.review_restaurant())
print("full review:")
print(review.full_review())


# test restaurant methods
print("RESTAURANTS")
restaurant = session.query(Restaurant).filter_by(id=9).first() # change id to desired restaurant
print(" Reviews:")
print(restaurant.restaurant_reviews())
print(" Customers making reviews:")
print(restaurant.restaurant_customers())
print("formatted reviews:")
print(restaurant.all_reviews())
print("Fanciest restaurant:")
print(Restaurant.fanciest_restaurants())

# test customer method 
print("CUSTOMERS")
customer = session.query(Customer).filter_by(id=5).first() # change id to desired customer
print ("Customers full name:")
print(customer.full_name())  
print("Reviews made:")
print(customer.customer_reviews())
print("Reviewed restaurants:")
print(customer.customer_restaurants())
print("favorite restaurant:")
print(customer.favorite_restaurant())
