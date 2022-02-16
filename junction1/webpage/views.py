from django.shortcuts import render

posts=[
{
	'author':'korean',
	'title':'junction post',
	'content':'1st post',
},
{
	'author':'bbbborean',
	'title':'junction postttttt',
	'content':'2st post',
}

]




def home(request):
	context = {
	'posts':posts
	}
	return render(request,'webpage/home.html',context)



def about(request):
	return render(request,'webpage/about.html',{'title':'about'})	