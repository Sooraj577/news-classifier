from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import pickle
from .forms import NewsForm
from django.conf import settings
import os
import warnings
warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
# Create your views here.

def get_news(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("inside POST")
        # create a form instance and populate it with data from the request:
        form = NewsForm(request.POST)
        print('Form', form)
        # check whether it's valid:
        if form.is_valid():
            print("Inside form valid")
            print(request.POST.get("news_text"))
            # getting news text from the request
            news_text = request.POST.get("news_text")
            # Vectorization
            cv_path = os.path.join(settings.MODEL_ROOT, "cv_vec.pickle")
            with open(cv_path, "rb") as vect:
                cv = pickle.load(vect)
            news_text_v = cv.transform([news_text])
            clf_path = os.path.join(settings.MODEL_ROOT, "news_clf")
            with open(clf_path, 'rb') as model:
                clf = pickle.load(model)
            new_pred = clf.predict(news_text_v)
            result = ''''''
            if new_pred == [0]:
                result = "Business News"
            elif new_pred == [1]:
                result = "Entertainment News"
            elif new_pred == [2]:
                result = "Politics News"
            elif new_pred == [3]:
                result = "Sports News"
            elif new_pred == [1]:
                result = "Tech News"

            result_dict = {
                'Text': "",
                'Result': "",
            }

            result_dict['Text'] = news_text
            result_dict['Result'] = result
            return render(request, 'index.html', {'result': result_dict})
            # return HttpResponse(result)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewsForm()

    return render(request, 'index.html', {'form': form})
