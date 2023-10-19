from django.shortcuts import render


blog_post = [
    {
        'title': "সেই বিশ্বকাপ, সেই ভারত, অন্য তামিম",
        'content': ("তামিম ইকবালকে ক্রিকেট–বিশ্ব কিভাবে চিনেছিল? চিনেছিল বিশ্বকাপে ভারতের বিপক্ষে "
                    "৫১ রানের একটা ইনিংসে, ২০০৭ বিশ্বকাপে পোর্ট"),
        'author': "মাশরাফি",
        "post_create datetime": " ১৯ অক্টোবর ২০২৩, ১৯: ২৭",
    }


]


def home(request):
    return render(request, "home.html", {"blog_post": blog_post})
