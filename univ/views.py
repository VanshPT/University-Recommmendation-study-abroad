from django.shortcuts import render
import pickle
import pandas as pd

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

# def toprank(request):
#     if request.method == 'GET':
#         # Retrieve form data
#         gre_score = float(request.GET.get('gre_score'))
#         gpa = float(request.GET.get('gpa'))
#         language_exam = request.GET.get('language_exam')
#         toefl_ielts_score = float(request.GET.get('toefl_ielts_score'))
#         research_papers = int(request.GET.get('research_papers'))

#         # Convert TOEFL score to IELTS scale if TOEFL is selected
#         if language_exam == 'toefl':
#             toefl_ielts_score = toefl_to_ielts(toefl_ielts_score)

#         # Perform any necessary calculations or predictions here
#         # Replace this with your actual prediction logic

#         # Placeholder response, replace with your logic
#         result = f"Top universities prediction based on input data: GRE {gre_score}, GPA {gpa}, Language Exam {language_exam}, {language_exam} Score {toefl_ielts_score}, Research Papers {research_papers}"

#         # Pass the result to the template
#         context = {'result': result, 'gre_score':gre_score, 'gpa':gpa, 'language_exam':language_exam, 'toefl_ielts_score': toefl_ielts_score, 'research_papers':research_papers}
#         return render(request, 'toprank.html', context)
#     else:
#         # Handle GET request if needed
#         return render(request, 'error_page.html', {'error_message': 'Invalid request method'})

def toprank(request):
    if request.method == 'GET':
        # Retrieve form data
        gre_score = float(request.GET.get('gre_score'))
        gpa = float(request.GET.get('gpa'))
        language_exam = request.GET.get('language_exam')
        toefl_ielts_score = float(request.GET.get('toefl_ielts_score'))
        research_papers = int(request.GET.get('research_papers'))
        selected_country = request.GET.get('selected_country')

        # Convert TOEFL score to IELTS scale if TOEFL is selected
        if language_exam == 'toefl':
            toefl_ielts_score = toefl_to_ielts(toefl_ielts_score)

        # Load the saved models and preprocessing objects based on the selected country
        model_file_path = f'model{selected_country.upper()}.pkl'
        label_encoder_file_path = f'label_encoder{selected_country.upper()}.pkl'

        with open(model_file_path, 'rb') as model_file:
            model = pickle.load(model_file)

        with open(label_encoder_file_path, 'rb') as label_encoder_file:
            label_encoder = pickle.load(label_encoder_file)

        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'GRE Score': [gre_score],
            'GPA': [gpa],
            'IELTS Score': [toefl_ielts_score],
            'Research Paper': [research_papers],
        })

        # Make prediction
        admission_probabilities = model.predict_proba(input_data)


        # Get the indices of top 10 probabilities
        top_10_indices = (-admission_probabilities).argsort()[:10]
        top_10_indices = top_10_indices.reshape(-1, 1)

        # Get the names of top 10 universities
        top_10_universities = label_encoder.inverse_transform(top_10_indices.flatten())[:10]

        # Prepare the response
        context = {
            'admission_probability': admission_probabilities[0],
            'top_10_universities': list(top_10_universities),
            'gre_score': gre_score,
            'gpa': gpa,
            'language_exam': language_exam,
            'toefl_ielts_score': toefl_ielts_score,
            'research_papers': research_papers,
            'selected_country': selected_country,
        }

        return render(request, 'toprank.html', context)
    else:
        # Handle GET request if needed
        return render(request, 'error_page.html', {'error_message': 'Invalid request method'})

