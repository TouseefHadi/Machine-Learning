If you want a direct result on your local host than first of all run the "web_page_Detection.py" file.

###############################################################################
if you want to check the web-page created in this project for detection of spam and not-spam msgs on your local host, than simply open pycharm,
and open the file with its name sms-spam-classifier-main and than in terminal type:

########COMMOND FOR EXECUTION THE WEB-PAGE ON LOCAL HOST IS #############

streamlit run web_page_Detection.py 

#######################################################################

And it will open the web page at your local host and than predict spam and not-spam by entering msgs and click on "click-predict" button.

#######################################################################
i provide comment with each line of code in details as much as possible for better understanding the code.
#######################################################################

==> here are four files one is main  with name "email-sms-spam-notspam-detection.ipynb"

==> and the other is for creating a simple website with named "web_page_Detection.py"

==> "model_file.pkl"  and  "vectorizer_file.pkl" are the two files which are use in "web_page_Detection.py" for website and these two files,
     contain on the results and information we collect from the training as for "MultinomialNB" classifier accuracy and precision values.   


################################################################################################################################
Thats all thank you have a nice day.