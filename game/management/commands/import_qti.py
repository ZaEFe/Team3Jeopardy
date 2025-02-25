import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from game.models import Question, Category

class Command(BaseCommand):
    help = 'Import questions from a QTI XML file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the QTI file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        tree = ET.parse(file_path)
        root = tree.getroot()

        for item in root.findall(".//item"):
            category_name = item.find("category").text
            category, _ = Category.objects.get_or_create(name=category_name)

            question_text = item.find("questiontext").text
            answer = item.find("answer").text
            value = int(item.find("value").text)

            Question.objects.create(
                category=category,
                question_text=question_text,
                answer=answer,
                value=value
            )

        self.stdout.write(self.style.SUCCESS("QTI Import Complete"))