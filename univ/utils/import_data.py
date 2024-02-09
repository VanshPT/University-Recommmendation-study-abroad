# your_django_app/utils/import_data.py
import csv
from univ.models import University
import logging

logger = logging.getLogger(__name__)

def import_data_from_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                university = University.objects.create(
                    UniversityName=row['University Name'],
                    GREscore=int(row['GRE Score']),
                    GPA=float(row['GPA']),
                    IELTSscore=float(row['IELTS Score']),
                    ResearchPaper=int(row['Research Paper']),
                    UniversityRanking=int(row['University Ranking']),
                    AdmitProbability=float(row['Admit Probability']),
                    country=row['country'],
                    course=row['course']
                )
            logger.info('Data imported successfully')
    except Exception as e:
        logger.error(f'Error occurred while importing data: {str(e)}')
