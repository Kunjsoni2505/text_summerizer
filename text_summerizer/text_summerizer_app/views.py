from django.shortcuts import render
import os
import requests
import google.generativeai as genai  # Import the Gemini API library
from .forms import TextForm  # Updated to use a TextForm for general text input

# Set up Gemini API
GOOGLE_API_KEY = "AIzaSyAz2e2mKPepUUkUWwQkoD41zCjcKqvjL0s"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to call Gemini API for summarization
def get_summary(text):
    prompt = f"Summarize the following text: {text}"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Main view to handle user input and generate summary
def summarize_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['text']
            summary = get_summary(data)  # Call the Gemini API for text summarization

            context = {
                'form': form,
                'summary': summary,
            }
            return render(request, 'result.html', context)
    else:
        form = TextForm()

    return render(request, 'Text.html', {'form': form})

def result(request):
    return render(request, 'result.html')
