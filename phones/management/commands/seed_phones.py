from django.core.management.base import BaseCommand
from phones.models import Phone


PHONES_DATA = [
    {
        "name": "Redmi Note 13",
        "price": 3200000,
        "ram": "6GB",
        "storage": "128GB",
        "camera": "108MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Arzon narxda kuchli akkumulyator va yaxshi kamera.",
    },
    {
        "name": "Samsung Galaxy A54",
        "price": 5500000,
        "ram": "8GB",
        "storage": "256GB",
        "camera": "50MP asosiy kamera",
        "battery": "5000mAh",
        "description": "O'rta narxda sifatli ekran va kamera.",
    },
    {
        "name": "Samsung Galaxy A34",
        "price": 4200000,
        "ram": "6GB",
        "storage": "128GB",
        "camera": "48MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Kundalik foydalanish uchun optimal variant.",
    },
    {
        "name": "iPhone 13",
        "price": 9500000,
        "ram": "4GB",
        "storage": "128GB",
        "camera": "12MP dual kamera",
        "battery": "3240mAh",
        "description": "iOS ekotizimi va yuqori sifat.",
    },
    {
        "name": "iPhone 15",
        "price": 12800000,
        "ram": "6GB",
        "storage": "128GB",
        "camera": "48MP dual kamera",
        "battery": "3349mAh",
        "description": "Eng so'nggi iPhone, kuchli protsessor.",
    },
    {
        "name": "Redmi 13C",
        "price": 1800000,
        "ram": "4GB",
        "storage": "128GB",
        "camera": "50MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Eng arzon variant, oddiy foydalanish uchun.",
    },
    {
        "name": "Poco X6",
        "price": 4700000,
        "ram": "8GB",
        "storage": "256GB",
        "camera": "64MP asosiy kamera",
        "battery": "5100mAh",
        "description": "O'yin va tez ishlash uchun yaxshi tanlov.",
    },
    {
        "name": "Samsung Galaxy S23",
        "price": 11000000,
        "ram": "8GB",
        "storage": "256GB",
        "camera": "50MP triple kamera",
        "battery": "3900mAh",
        "description": "Flagman daraja, professional kamera.",
    },
    {
        "name": "Redmi Note 13 Pro",
        "price": 4800000,
        "ram": "8GB",
        "storage": "256GB",
        "camera": "200MP asosiy kamera",
        "battery": "5100mAh",
        "description": "Yuqori piksel kamera bilan o'rta segment.",
    },
    {
        "name": "Vivo Y36",
        "price": 3600000,
        "ram": "8GB",
        "storage": "128GB",
        "camera": "50MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Yengil va nozik dizayn, kunlik foydalanish uchun.",
    },
    {
        "name": "Realme C67",
        "price": 2500000,
        "ram": "6GB",
        "storage": "128GB",
        "camera": "108MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Arzon narxda yuqori piksel kamera.",
    },
    {
        "name": "Samsung Galaxy A15",
        "price": 3000000,
        "ram": "4GB",
        "storage": "128GB",
        "camera": "50MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Ishonchli brend, boshlang'ich segment.",
    },
    {
        "name": "iPhone 14",
        "price": 10500000,
        "ram": "6GB",
        "storage": "128GB",
        "camera": "12MP dual kamera",
        "battery": "3279mAh",
        "description": "Yaxshi kamera sifati va uzun qo'llab-quvvatlash muddati.",
    },
    {
        "name": "Poco M6 Pro",
        "price": 3400000,
        "ram": "8GB",
        "storage": "256GB",
        "camera": "64MP asosiy kamera",
        "battery": "5000mAh",
        "description": "Narx-sifat nisbati yuqori model.",
    },
    {
        "name": "Samsung Galaxy S24",
        "price": 14500000,
        "ram": "8GB",
        "storage": "256GB",
        "camera": "50MP triple kamera",
        "battery": "4000mAh",
        "description": "Eng so'nggi flagman, AI funksiyalari bilan.",
    },
]


class Command(BaseCommand):
    help = "Bazaga namuna telefon ma'lumotlarini qo'yadi"

    def handle(self, *args, **kwargs):
        Phone.objects.all().delete()

        for data in PHONES_DATA:
            Phone.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(PHONES_DATA)} ta telefon bazaga muvaffaqiyatli qo'shildi."
            )
        )