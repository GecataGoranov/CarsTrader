from accounts.models import TraderUser, TraderProfile
from trader.models import Car, CarPictures

def create_user_and_profile():
    valid_user_credentials = {
        "email":"test@gosho.store",
        "password":"test1234"}
    user = TraderUser.objects.create(**valid_user_credentials)
    valid_profile_credentials = {
        "user":user,
        "slug":"testgoshostore",
        "profile_picture":"some_picture.png",
        "phone_number":"0909090909",
        "first_name":"Test",
        "last_name":"User",
        "place_of_living":"TestLand"
    }

    profile = TraderProfile.objects.create(**valid_profile_credentials)
    return user, profile

def create_car(model="306 Phase I"):
    car_data = {
        'manufacturer': "Peugeot",
        'model': model,
        'category': "SED",
        'gearbox_type': "M",
        'engine_type': "P",
        'engine_power': 88,
        'engine_volume': 1600,
        'eurostandard': 1,
        'mileage': 176000,
        'production_date':"1997-12-12",
        'color': "G",
        'condition': "U",
        'price':2000,
    }

    try:
        user = TraderUser.objects.get(email="test@gosho.store")
    except:
        user ,_ = create_user_and_profile()

    car = Car.objects.create(seller=user, **car_data)
    return car

def create_another_user(**credentials):
    if not credentials:
        credentials = {
            "email":"another_test@gosho.store",
            "password":"test1234"}
    user = TraderUser.objects.create(**credentials)
    return user