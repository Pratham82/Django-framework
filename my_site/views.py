# this file was created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')


def about(request):
	return HttpResponse('This is about page')

# This will be the main endpoint
def analyze(request):
	#* for printing the data that we get from the input
	#* print(request.GET.get('text', 'default'))
	inputText = request.GET.get('text', 'default')
	print(f'This is the input text provied :{inputText}')

	#*  For checking if the specified checkbox value is selected
	remmovePuncVal = request.GET.get('removePunc', 'default')

	#* This will return "on" if selected 
	print(remmovePuncVal) # on
	print(remmovePuncVal == 'on')  # if the return value sis true then it will return true
	
	
	
	if remmovePuncVal == 'on':
		#* Method for removing punctuations
		def remPunc(str):
			punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
			val = ''
			for char in str:
				if char not in punctuations:
					val += char 
			return val
		outputText = remPunc(inputText)
		message = 'Remove Punctuations'
	else:
		outputText = inputText
		message = 'Operation not selected'

	output = {'input': inputText, 'result': outputText, 'message': message }
	return render(request, 'output.html',output )
	# return HttpResponse('''
	# <a href="/">Go to Home</a>
	# <br/>
	# Remove punctuations{{}}
	# ''')

# def removePunctuation(request):
# 	#for printing the data that we get from the input
# 	# print(request.GET.get('text', 'default'))

# 	inputText = request.GET.get('text', 'default')
# 	print(f'This is the input text provied :{inputText}')
# 	return HttpResponse('''
# 	<a href="/">Go to Home</a>
# 	<br/>
# 	Remove punctuations
# 	''')


def capFirst(request):
	return HttpResponse('Capitalize')

def removeNewLine(request):
	return HttpResponse('Remove new lines')

def removeSpace(request):
	return HttpResponse('Remove space')

def charCount(request):
	return HttpResponse('Char Count')

def templateExample(request):
	obj = {'name': 'Prathamesh', 'age': '23', 'location': 'Mumbai'}
	return render(request, 'index.html',obj)

def favourites(request):
	return HttpResponse("""
		<!DOCTYPE html>
		<html lang="en">
			<head>
				<meta charset="UTF-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
				<title>Favourites page</title>
			</head>
			<body >
				<div style="display:flex; height: 100vh;justify-content:center; align-items:center">
				<div
					class="container"
					style="
						display: grid;
						place-items: center;
						font-family: Fira code;
						text-decoration: none;
						border: 1px solid;
						border-radius: 15px;
						padding: 15px;
						width:400px;
					"
				>
					<h1>My favourite sites</h1>
					<div class="page-1">
						<a
							href="https://www.github.com"
							style="
								text-decoration: none;
								color: rgb(75, 74, 74);
								font-size: 25px;
							"
							target="_"
							>Github</a
						>
					</div>
					<div class="page-2">
						<a
							href="https://www.youtube.com"
							style="
								text-decoration: none;
								color: rgb(75, 74, 74);
								font-size: 25px;
							"
							target="_"
							>YouTube</a
						>
					</div>
					<div class="page-3">
						<a
							href="https://www.edabit.com"
							style="
								text-decoration: none;
								color: rgb(75, 74, 74);
								font-size: 25px;
							"
							target="_"
							>Edabit</a
						>
					</div>
					<div class="page-4">
						<a
							href="https://www.stackoverflow.com"
							style="
								text-decoration: none;
								color: rgb(75, 74, 74);
								font-size: 25px;
							"
							target="_"
							>StackOverflow</a
						>
					</div>
					<div class="page-5">
						<a
							href="https://www.twitter.com"
							style="
								text-decoration: none;
								color: rgb(75, 74, 74);
								font-size: 25px;
							"
							target="_"
							>Twitter</a
						>
					</div>
				</div>
				</div>
			</body>
		</html>
	""")