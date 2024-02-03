from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def study(request):
    if request.method == 'POST':
        # Handle form submission
        selected_country = request.POST.get('country', 'default')

        # You can perform additional processing here based on the form data

        # Send the selected country to the study.html template
        return render(request, 'study.html', {'selected_country': selected_country})

    return render(request, 'index.html')

def toefl_to_ielts(toefl_score):
    # This is a very basic conversion, and it may not be accurate for all cases
    # You should consult official conversion tables or sources for a more accurate conversion
    if toefl_score >= 120:
        return 9.0
    elif toefl_score >= 110:
        return 8.5
    elif toefl_score >= 100:
        return 8.0
    elif toefl_score >= 90:
        return 7.0
    elif toefl_score >= 80:
        return 6.5
    elif toefl_score >= 70:
        return 6.0
    elif toefl_score >= 60:
        return 5.5
    else:
        return 0.0  # Adjust as needed for scores below 60

def toprank(request):
    if request.method == 'POST':
        # Retrieve form data
        gre_score = float(request.POST.get('gre_score'))
        gpa = float(request.POST.get('gpa'))
        language_exam = request.POST.get('language_exam')
        toefl_ielts_score = float(request.POST.get('toefl_ielts_score'))
        research_papers = int(request.POST.get('research_papers'))

        # Convert TOEFL score to IELTS scale if TOEFL is selected
        if language_exam == 'toefl':
            toefl_ielts_score = toefl_to_ielts(toefl_ielts_score)

        # Perform any necessary calculations or predictions here
        # Replace this with your actual prediction logic

        # Placeholder response, replace with your logic
        result = f"Top universities prediction based on input data: GRE {gre_score}, GPA {gpa}, Language Exam {language_exam}, {language_exam} Score {toefl_ielts_score}, Research Papers {research_papers}"

        # Pass the result to the template
        context = {'result': result}
        return render(request, 'toprank.html', context)
    else:
        # Handle GET request if needed
        return render(request, 'error_page.html', {'error_message': 'Invalid request method'})