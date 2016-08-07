"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""
from flask_sqlalchemy import SQLAlchemy
from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

brand_eight = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

corvette_chevy = Model.query.filter_by(name='Corvette',brand_name='Chevrolet').all()

# Get all models that are older than 1960.

old_models = Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.

new_brands = Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".

cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

current_brands = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

current_brands = Brand.query.filter(Brand.founded==1903, Brand.discontinued == None).all()

# Get any model whose brand_name is not Chevrolet.

not_chevy = Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model).join(Brand).filter(Model.year == year).all()
    for model in model_info:
        print "%s, %s, %s" % (model.name, model.brand_name, model.brands.headquarters)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_brands = db.session.query(Model.brand_name, Model.name).group_by(Model.name, Model.brand_name).order_by(Model.brand_name, Model.name).all()
    for model in all_brands:
        print "%s, %s" % (model[0], model[1])


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

Datatype is a query
Returned value is : 
SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued 
FROM brands 
WHERE brands.name = :name_1

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
