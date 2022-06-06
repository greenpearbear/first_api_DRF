from datetime import date
from rest_framework import serializers


def no_children_on_site(value):
    today = date.today()

    if today.year - value.year < 9:
        raise serializers.ValidationError("Нельзя регистрироваться пользователям младше 9 лет")


def no_rambler_on_my_site(value):
    if value.find("@rambler.ru") != -1:
        raise serializers.ValidationError("Пошел прочь человек с рамблера!")
