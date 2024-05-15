# your_app/management/commands/create_test_data.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
from pet.models import Specie, Characteristic, Gender, Size, Pet, PetImage
from shelter.models import Shelter
from blog.models import BlogCategory, BlogPost, Comment, Tag
import random
from faker import Faker
import requests
from django.core.files.base import ContentFile

User = get_user_model()

fake = Faker()

class Command(BaseCommand):
    help = 'Create test data for the application'

    def add_arguments(self, parser):
        parser.add_argument('--species', type=int, help='Number of species to create')
        parser.add_argument('--characteristics', type=int, help='Number of characteristics to create')
        parser.add_argument('--genders', type=int, help='Number of genders to create')
        parser.add_argument('--sizes', type=int, help='Number of sizes to create')
        parser.add_argument('--shelters', type=int, help='Number of shelters to create')
        parser.add_argument('--pets', type=int, help='Number of pets to create')
        parser.add_argument('--categories', type=int, help='Number of blog categories to create')
        parser.add_argument('--posts', type=int, help='Number of blog posts to create')
        parser.add_argument('--comments', type=int, help='Number of comments per post to create')
        parser.add_argument('--tags', type=int, help='Number of tags to create')

    def handle(self, *args, **options):
        if options['species']:
            self.create_species(options['species'])
        if options['characteristics']:
            self.create_characteristics(options['characteristics'])
        if options['genders']:
            self.create_genders(options['genders'])
        if options['sizes']:
            self.create_sizes(options['sizes'])
        if options['shelters']:
            self.create_shelters(options['shelters'])
        if options['pets']:
            self.create_pets(options['pets'])
        if options['categories'] or options['posts'] or options['comments'] or options['tags']:
            self.create_blog_data(
                options['categories'],
                options['posts'],
                options['comments'],
                options['tags']
            )
        self.stdout.write(self.style.SUCCESS('Test data created successfully'))

    def create_species(self, count):
        species_names = [fake.word() for _ in range(count)]
        for name in species_names:
            Specie.objects.get_or_create(name=name, description=fake.text())

    def create_characteristics(self, count):
        characteristics = [fake.word() for _ in range(count)]
        for name in characteristics:
            Characteristic.objects.get_or_create(name=name)

    def create_genders(self, count):
        genders = [fake.word() for _ in range(count)]
        for name in genders:
            Gender.objects.get_or_create(name=name)

    def create_sizes(self, count):
        sizes = [fake.word() for _ in range(count)]
        for name in sizes:
            Size.objects.get_or_create(name=name)

    def create_shelters(self, count):
        for _ in range(count):
            shelter = Shelter.objects.create(
                name=fake.company(),
                city=fake.city(),
                address=fake.address(),
                phone=fake.phone_number(),
            )
            image_url = "https://themebeyond.com/pre/petco-prev/petco-live/img/blog/blog_thumb01.jpg"
            self.download_and_save_image(shelter, image_url, 'image', 'shelters/')

    def create_pets(self, count):
        species = list(Specie.objects.all())
        genders = list(Gender.objects.all())
        sizes = list(Size.objects.all())
        shelters = list(Shelter.objects.all())
        characteristics = list(Characteristic.objects.all())
        
        for _ in range(count):
            pet = Pet.objects.create(
                name=fake.first_name(),
                specie=random.choice(species),
                gender=random.choice(genders),
                size=random.choice(sizes),
                health=fake.text(max_nb_chars=50),
                description=fake.text(max_nb_chars=100),
                shelter=random.choice(shelters),
                weight=random.uniform(1.0, 30.0),
                birth_date=fake.date_time_this_decade(),
                slug=slugify(fake.first_name()),
            )
            pet.characteristics.set(random.sample(characteristics, k=min(2, len(characteristics))))
            pet.save()

            image_url = "https://themebeyond.com/pre/petco-prev/petco-live/img/product/adoption_shop_thumb01.jpg"
            pet_image = PetImage.objects.create()
            self.download_and_save_image(pet_image, image_url, 'images', 'pets/gallery/')
            pet.images.add(pet_image)

    def create_blog_data(self, category_count, post_count, comment_count, tag_count):
        authors = list(User.objects.all())
        if not authors:
            authors.append(User.objects.create_user(
                username='testuser', password='password', email='test@example.com'
            ))

        if category_count:
            for _ in range(category_count):
                BlogCategory.objects.get_or_create(title=fake.word(), description=fake.text())

        if tag_count:
            for _ in range(tag_count):
                Tag.objects.get_or_create(name=fake.word())

        if post_count:
            for _ in range(post_count):
                post = BlogPost.objects.create(
                    author=random.choice(authors),
                    title=fake.sentence(),
                    short_description=fake.text(max_nb_chars=150),
                    content=fake.text(),
                    category=random.choice(BlogCategory.objects.all()),
                    slug=slugify(fake.sentence()),
                    is_published=True,
                    is_page=False
                )
                if tag_count:
                    post.tags.set(random.sample(list(Tag.objects.all()), k=min(2, len(Tag.objects.all()))))
                post.save()

                if comment_count:
                    for _ in range(comment_count):
                        Comment.objects.create(
                            post=post,
                            user=random.choice(authors),
                            content=fake.text(),
                            is_approved=True,
                        )

    def download_and_save_image(self, instance, url, field_name, upload_to):
        response = requests.get(url)
        if response.status_code == 200:
            file_name = url.split('/')[-1]
            file_content = ContentFile(response.content)
            getattr(instance, field_name).save(file_name, file_content, save=True)
