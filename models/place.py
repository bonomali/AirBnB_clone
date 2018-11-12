#!/usr/bin/python3
"""This module defines a class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines a City
    Attributes:
    city_id (string): City.id
    user_id (string): User.id
    name (string): Place name
    description (string): a description of the place
    number_rooms (integer): the number of rooms
    number_bathrooms (integer): the number of bathrooms
    max_guest (integer): the maximum number of guests
    price_by_night (integer): the cost of the room per night
    latitude (float): the latitude of the place
    longitude (float): the longitude of the place
    amenity_ids (list of strings): the list of Amenity.id's
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
