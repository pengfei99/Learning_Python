from _ast import List

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Invoice(Base):
    __tablename__ = 'invoices'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    custid = Column(Integer, ForeignKey('customers.id'))
    invno = Column(Integer)
    amount = Column(Integer)
    customer = relationship("Customer", back_populates="invoices")


# this line is very important, this will add an attribute invoice into class customer
#
Customer.invoices = relationship("Invoice", order_by=Invoice.id, back_populates="customer")

base_path = "../../../data/orm_test.db"
db_url = f"sqlite:///{base_path}"
engine = create_engine(db_url, echo=True)


def add_customer(customer: Customer):
    Session = sessionmaker(bind=engine)
    session = Session()
    # add one customer
    session.add(customer)
    session.commit()
    session.close()


def add_customers(customers: List(Customer)):
    Session = sessionmaker(bind=engine)
    session = Session()
    # add a list of customers
    session.add_all(customers)
    session.commit()
    session.close()


# we can define a customer without invoices
c1 = Customer(name="Gopal Krishna", address="Bank Street Hydarebad", email="gk@gmail.com")
# we add inovice after the creation
c1.invoices = [Invoice(invno=10, amount=15000), Invoice(invno=14, amount=3850)]

# add_customer(c1)

# we can define a customer with invoices
c2 = Customer(
    name="Toto titi",
    address="the mother land",
    email="titi@gmail.com",
    invoices=[Invoice(invno=3, amount=10000),
              Invoice(invno=4, amount=5000)]
)
# add_customer(c2)

# we can also do a bulk upload

rows = [
   Customer(
      name = "Govind Kala",
      address = "Gulmandi Aurangabad",
      email = "kala@gmail.com",
      invoices = [Invoice(invno = 7, amount = 12000), Invoice(invno = 8, amount = 18500)]),

   Customer(
      name = "Abdul Rahman",
      address = "Rohtak",
      email = "abdulr@gmail.com",
      invoices = [Invoice(invno = 9, amount = 15000),
      Invoice(invno = 11, amount = 6000)
   ])
]

add_customers(rows)
