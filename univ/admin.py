from django.contrib import admin
from .models import University
from django.urls import path
from django.shortcuts import render
from django import forms
from itertools import count

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('UniversityName', 'GREscore', 'GPA', 'IELTSscore', 'ResearchPaper', 'UniversityRanking', 'AdmitProbability', 'country', 'course')
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload_csv/', self.upload_csv),
        ]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split("\n")

            # Skip the header row
            csv_data = csv_data[1:]

            for i, row in enumerate(csv_data, start=1):
                if not row.strip():  # Skip empty rows
                    continue
                
                fields = row.split(',')
                if len(fields) == 9:  # Ensure all fields are present
                    university_data = {
                        'GREscore': int(fields[0]),
                        'GPA': float(fields[1]),
                        'IELTSscore': float(fields[2]),
                        'ResearchPaper': int(fields[3]),
                        'UniversityRanking': int(fields[4]),
                        'UniversityName': fields[5],  # Reordered as per CSV
                        'AdmitProbability': float(fields[6]),
                        'country': fields[7],
                        'course': fields[8].strip()  # Strip the newline character
                    }
                    # Generate UniversityIndex
                    university_data['UniversityIndex'] = i

                    # Update or create the university entry
                    University.objects.update_or_create(UniversityIndex=i, defaults=university_data)

        form = CsvImportForm()
        data = {'form': form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(University, UniversityAdmin)
