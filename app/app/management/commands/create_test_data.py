# your_app/management/commands/create_test_data.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
from adoption.models import Questionnaire, Question, QuestionType, Option
from pet.models import Specie, Characteristic, Gender, Size, Pet, PetImage
from shelter.models import Shelter, State
from blog.models import BlogCategory, BlogPost, Comment, Tag
import random
from faker import Faker
import requests
from django.core.files.base import ContentFile
import os
from django.core.exceptions import ValidationError

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
        self.create_questionnaires()
        self.stdout.write(self.style.SUCCESS('Test data created successfully'))

    def create_species(self, count):
        species_names = ["Perro", "Gato", "Hamster", "Conejo", "Ave"]
        for name in species_names:
            Specie.objects.get_or_create(name=name, description=fake.text())

    def create_characteristics(self, count):
        characteristics = [fake.word() for _ in range(count)]
        for name in characteristics:
            Characteristic.objects.get_or_create(name=name)

    def create_genders(self, count):
        genders = ["Macho", "Hembra"]
        for name in genders:
            Gender.objects.get_or_create(name=name)

    def create_sizes(self, count):
        sizes = ["Pequeño", "Mediano", "Grande"]
        for name in sizes:
            Size.objects.get_or_create(name=name)

    def create_states(self):
        states = ["California", "Texas", "New York", "Florida", "Illinois"]
        for state_name in states:
            State.objects.get_or_create(name=state_name)


    def create_shelters(self, count):
        states = State.objects.all()
        if not states.exists():
            self.create_states()
            states = State.objects.all()

        for _ in range(count):
            shelter = Shelter.objects.create(
                name=fake.company(),
                city=fake.city(),
                address=fake.address(),
                phone=fake.phone_number(),
                state=random.choice(states)
            )
            image_url = "https://adoptasalvaunavida.com/imas/animales/_2878/a_28781713357321.jpg"
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

            image_url = random.choice([
                "https://adoptasalvaunavida.com/imas/animales/_2893/a_28931715778094.jpg",
                "https://adoptasalvaunavida.com/imas/animales/_2892/a_28921715777769.jpg",
                "https://adoptasalvaunavida.com/imas/animales/_2889/a_28891715202896.jpg",
                "https://adoptasalvaunavida.com/imas/animales/_2887/a_28871714857048.jpg",
                "https://adoptasalvaunavida.com/imas/animales/_2882/a_28821713790894.jpg",
                "https://adoptasalvaunavida.com/imas/animales/_2878/a_28781713357321.jpg",
            ])
            pet_image = PetImage.objects.create()
            self.download_and_save_image(pet_image, image_url, 'image', 'pets/gallery/')
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
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_name = url.split('/')[-1]
                # Ensure the file name is valid
                file_name = os.path.basename(file_name)
                if not file_name:
                    raise ValidationError(f"Invalid file name extracted from URL: {url}")
                file_content = ContentFile(response.content)
                getattr(instance, field_name).save(file_name, file_content, save=True)
                print(f"Image saved: {file_name}")
            else:
                print(f"Failed to download image from {url}: HTTP {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading or saving the image: {e}")

    def create_questionnaires(self):
        shelters = Shelter.objects.all()
        for shelter in shelters:
            questionnaire = Questionnaire.objects.create(
                title=f'Adoption Questionnaire for {shelter.name}',
                shelter=shelter
            )
            self.create_questions(questionnaire)
            questionnaire.save()

    def create_questions(self, questionnaire):
        question_texts = [
            'Why do you want to adopt a pet?',
            'Do you have experience with pets?',
            'Do you have a suitable living environment for a pet?',
            'How many hours will the pet be alone each day?'
        ]

        for text in question_texts:
            question = Question.objects.create(
                text=text,
                question_type=fake.random_element([QuestionType.TEXT, QuestionType.SELECT, QuestionType.CHECKBOX]),
                value=fake.random_int(min=1, max=5),
                parent_question=None,
                questionnaire=questionnaire
            )
            if question.question_type in [QuestionType.SELECT, QuestionType.CHECKBOX]:
                self.create_options(question)
            question.save()

    def create_options(self, question):
        option_texts = [
            'Yes',
            'No',
            'Maybe',
            'Not applicable'
        ]

        for text in option_texts:
            option = Option.objects.create(
                question=question,
                text=text,
                value=fake.random_int(min=1, max=5)
            )
            option.save()
