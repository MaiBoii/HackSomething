from faker import Faker

fake = Faker("ko-KR")
for _ in range(10):
    print(fake.name())
    print(fake.job())
    print(fake.address())
    print(fake.phone_number())